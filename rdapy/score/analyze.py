"""
ANALYZE ("SCORE") A PLAN
- There are 5 types of datasets -- census, VAP, CVAP, election, and shapes.
- Input "data" can include multiple datasets of the same type -- e.g., multiple elections.
- Because a plan can be scored against more than one dataset of a given type,
  scores are always in the context of the dataset used in the scoring.

- For plan-level metrics, multiple sets of scores are disambiguated with prefixes
  that identify the dataset.
- For district-level metrics, each set of scores is wrapped in a dictionary with the dataset key.

NOTE - This file takes its name from the Analyze tab in DRA.
"""

from typing import Any, List, Dict, Tuple, Optional, TextIO

import sys, json

from ..base import (
    get_dataset,
    get_datasets,
    get_fields,
    DatasetKey,
    Aggregates,
    Precinct,
    District,
)
from ..rate import (
    rate_proportionality,
    rate_competitiveness,
    rate_minority_opportunity,
    rate_reock,
    rate_polsby,
    rate_compactness,
    rate_county_splitting,
    rate_district_splitting,
    rate_splitting,
)
from ..compactness import (
    calc_cut_score,
    calc_energy,
)
from ..minority import calculate_mmd_simple
from .categories import (
    calc_general_category,
    calc_partisan_category,
    calc_minority_category,
    calc_compactness_category,
    calc_splitting_category,
)

#####


def score_plans(
    input_stream: TextIO,
    output_stream: TextIO,
    input_data: List[Dict[str, Any]],
    data_map: Dict[str, Any],
    adjacency_graph: Dict[str, List[str]],
    metadata: Dict[str, Any],
    *,
    mode: str,
    precomputed: Dict[str, Any],
) -> None:
    """
    Read plans & district aggregates as JSONL from the input stream.
    Score each plan.
    Write the scores along with the aggregates to the output stream.
    Pass through metadata records.
    Skip any other records.
    """

    i: int = 0
    for line in input_stream:
        try:
            parsed_line: Dict[str, Any] = json.loads(line)

            # Case 1: Has "_tag_" key with value "metadata" - pass it along

            if "_tag_" in parsed_line and parsed_line["_tag_"] == "metadata":
                print(json.dumps(parsed_line), file=output_stream)
                continue

            # Case 2: Has "_tag_" key with value "plan"

            if "_tag_" in parsed_line and parsed_line["_tag_"] == "plan":
                name = parsed_line["name"]
                assignments = {str(k): int(v) for k, v in parsed_line["plan"].items()}
                aggs: Aggregates = parsed_line["aggregates"]

                scores: Dict[str, Any]
                updated_aggs: Aggregates
                scores, updated_aggs = score_plan(
                    assignments,
                    aggs,
                    data=input_data,
                    graph=adjacency_graph,
                    metadata=metadata,
                    data_map=data_map,
                    mode=mode,
                    precomputed=precomputed,
                )

                scores_with_aggs: Dict[str, Any] = {
                    "_tag_": "scores",
                    "name": name,
                    "scores": scores,
                    "aggregates": updated_aggs,
                }

                print(json.dumps(scores_with_aggs), file=output_stream)
                continue

            # Case 3: Something else - skip the line, e.g., adjacency graph, etc.

            continue

        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON: {e}", file=sys.stderr)
        except Exception as e:
            print(f"Error processing record: {e}", file=sys.stderr)


### SCORE ONE PLAN ###


def score_plan(
    assignments: Dict[Precinct, District],
    aggs: Aggregates,
    *,
    data: List[Dict[str, Any]],
    graph: Dict[str, List[str]],
    metadata: Dict[str, Any],
    data_map: Dict[str, Any],
    #
    mode: str = "all",  # Or one of "general", "partisan", "minority", "compactness", "splitting"
    precomputed: Dict[str, Any],
    #
    mmd_scoring: bool = True,  # If False, don't do MMD scoring for backwards compatibility w/ tests.
) -> Tuple[Dict[str, Any], Aggregates]:
    """Score a plan."""

    # Pulled 'extended' scoring out separately
    assert mode in [
        "all",
        "general",
        "partisan",
        "minority",
        "compactness",
        "splitting",
    ]

    n_districts: int = metadata["D"]
    n_counties: int = metadata["C"]

    census_dataset: DatasetKey = get_dataset(data_map, "census")
    vap_dataset: DatasetKey = get_dataset(data_map, "vap")
    cvap_dataset: DatasetKey = get_dataset(data_map, "cvap")
    election_datasets: List[DatasetKey] = get_datasets(data_map, "election")
    shapes_dataset: DatasetKey = get_dataset(data_map, "shapes")

    scorecard: Dict[str, Any] = {
        "census": {census_dataset: {}},
        "vap": {vap_dataset: {}},
        "cvap": {cvap_dataset: {}},
        "election": {e: {} for e in election_datasets},
        "shapes": {shapes_dataset: {}},
    }

    if mode in ["all", "general"]:
        general_metrics: Dict[str, Any] = calc_general_category(
            aggs["census"][census_dataset],
            n_districts,
        )
        deviation: float = general_metrics.pop("population_deviation")
        scorecard["census"][census_dataset]["population_deviation"] = deviation

    if mode in ["all", "partisan"]:
        for election_dataset in election_datasets:
            geographic_baselines: Dict[str, Any] = dict()
            if (
                precomputed
                and "geographic_baseline" in precomputed
                and election_dataset in precomputed["geographic_baseline"]
            ):
                geographic_baselines = precomputed["geographic_baseline"][
                    election_dataset
                ]
            partisan_metrics: Dict[str, Optional[float]] = calc_partisan_category(
                aggs["election"][election_dataset], n_districts, geographic_baselines
            )
            # estimated_seat_pct = partisan_metrics.pop("estimated_seat_pct")
            estimated_seats = partisan_metrics["estimated_seats"]
            assert estimated_seats is not None
            estimated_seat_pct: float = estimated_seats / n_districts
            assert estimated_seat_pct is not None
            scorecard["election"][election_dataset].update(partisan_metrics)

            scorecard["election"][election_dataset]["proportionality"] = (
                _rate_proportionality(
                    scorecard["election"][election_dataset]["pr_deviation"],
                    scorecard["election"][election_dataset]["estimated_vote_pct"],
                    estimated_seat_pct,
                )
            )
            scorecard["election"][election_dataset]["competitiveness"] = (
                _rate_competitiveness(
                    scorecard["election"][election_dataset]["competitive_districts"]
                    / n_districts
                )
            )

    if mode in ["all", "minority"]:
        vap_dataset: DatasetKey = get_dataset(data_map, "vap")
        vap_keys: List[str] = list(get_fields(data_map, "vap", vap_dataset).keys())

        if mmd_scoring:
            mmd_counts: Dict[str, int] = calculate_mmd_simple(
                aggs["cvap"][cvap_dataset]
            )
            scorecard["cvap"][cvap_dataset].update(mmd_counts)

        # Revised minority ratings that don't click Black VAP % below 37%

        alt_minority_metrics: Dict[str, float] = (
            calc_minority_category(  # Was: calc_alt_minority_metrics(
                aggs["vap"][vap_dataset], n_districts, vap_keys
            )
        )
        scorecard["vap"][vap_dataset].update(alt_minority_metrics)

        scorecard["vap"][vap_dataset]["minority"] = _rate_minority_opportunity(
            alt_minority_metrics["opportunity_districts"],
            alt_minority_metrics["proportional_opportunities"],
            alt_minority_metrics["coalition_districts"],
            alt_minority_metrics["proportional_coalitions"],
        )

    if mode in ["all", "compactness"]:
        compactness_by_district: Dict[str, List[float]] = calc_compactness_category(
            aggs["shapes"][shapes_dataset], n_districts
        )
        compactness_metrics: Dict[str, float] = {
            "reock": compactness_by_district["reock"][0],
            "polsby_popper": compactness_by_district["polsby_popper"][0],
        }

        # Additional discrete compactness metrics
        cut_score: int = calc_cut_score(assignments, graph)
        compactness_metrics["cut_score"] = cut_score

        # NOTE - Too expensive for scoring plans in bulk.
        # if add_spanning_tree_score:
        #     district_graphs = _split_graph_by_districts(graph, assignments)
        #     spanning_tree_by_district: List[Dict[str, float]] = [
        #         {"spanning_tree_score": calc_spanning_tree_score(g)}
        #         for g in district_graphs.values()
        #     ]
        #     spanning_tree_score: float = sum(
        #         d["spanning_tree_score"] for d in spanning_tree_by_district
        #     )
        #     compactness_metrics["spanning_tree_score"] = spanning_tree_score

        # Population compactness
        census_dataset: DatasetKey = get_dataset(data_map, "census")
        pop_field: str = get_fields(data_map, "census", census_dataset)["total_pop"]
        energy: float = calc_energy(assignments, data, pop_field)  # type: ignore
        compactness_metrics["population_compactness"] = energy

        scorecard["shapes"][shapes_dataset].update(compactness_metrics)

        scorecard["shapes"][shapes_dataset]["compactness"] = _rate_compactness(
            scorecard["shapes"][shapes_dataset]["reock"],
            scorecard["shapes"][shapes_dataset]["polsby_popper"],
        )

    if mode in ["all", "splitting"]:
        splitting_metrics: Dict[str, float]
        splitting_by_district: Dict[str, List[float]]
        splitting_metrics, splitting_by_district = calc_splitting_category(
            aggs["census"][census_dataset], n_districts
        )
        scorecard["census"][census_dataset].update(splitting_metrics)
        scorecard["census"][census_dataset]["splitting"] = _rate_splitting(
            scorecard["census"][census_dataset]["county_splitting"],
            scorecard["census"][census_dataset]["district_splitting"],
            n_counties,
            n_districts,
        )

    # Combine the by-district metrics
    new_aggs: Aggregates = aggs.copy()
    if mode in ["all", "compactness"]:
        new_aggs["shapes"][shapes_dataset].update(compactness_by_district)
    if mode in ["all", "splitting"]:
        new_aggs["census"][census_dataset].update(splitting_by_district)
        new_aggs["census"][census_dataset].pop("CxD")

    # Trim the floating point numbers
    precision: int = 4
    int_metrics: List[str] = [
        "pr_seats",
        "fptp_seats",
        "proportionality",
        "competitive_district_count",
        "competitiveness",
        "proportional_opportunities",
        "proportional_coalitions",
        "mmd_black",
        "mmd_hispanic",
        "mmd_coalition",
        "minority",
        "cut_score",
        "spanning_tree_score",
        "compactness",
        "counties_split",
        "county_splits",
        "splitting",
    ]
    for type_, datasets_ in scorecard.items():
        for dataset_, metrics in datasets_.items():
            for metric_, value_ in metrics.items():
                if value_ is None:  # Was: or metric == "by_district":
                    continue
                if metric_ not in int_metrics:
                    scorecard[type_][dataset_][metric_] = round(value_, precision)

    return scorecard, new_aggs


### RATING HELPERS ###


def _rate_proportionality(disproportionality: float, Vf: float, Sf: float) -> int:
    rating: int = rate_proportionality(disproportionality, Vf, Sf)

    return rating


def _rate_competitiveness(cdf: float) -> int:
    rating: int = rate_competitiveness(cdf)

    return rating


def _rate_minority_opportunity(od: float, pod: float, cd: float, pcd: float) -> int:
    rating: int = rate_minority_opportunity(od, pod, cd, pcd)

    return rating


def _rate_compactness(avg_reock: int, avg_polsby: int) -> int:
    reock_rating: int = rate_reock(avg_reock)
    polsby_rating: int = rate_polsby(avg_polsby)
    rating: int = rate_compactness(reock_rating, polsby_rating)

    return rating


def _rate_splitting(
    county_splitting: float,
    district_splitting: float,
    n_counties: int,
    n_districts: int,
) -> int:
    county_rating: int = rate_county_splitting(
        county_splitting, n_counties, n_districts
    )
    district_rating: int = rate_district_splitting(
        district_splitting, n_counties, n_districts
    )
    rating: int = rate_splitting(county_rating, district_rating)

    return rating


### END ###
