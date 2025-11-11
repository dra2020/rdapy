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
    get_dataset_keys,
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
    reverse_weight_splitting: bool = False,
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
                    reverse_weight_splitting=reverse_weight_splitting,
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
    reverse_weight_splitting: bool = False,
) -> Tuple[Dict[str, Any], Aggregates]:
    """Score a plan."""

    assert mode in [
        "all",
        "general",
        "partisan",
        "minority",
        "compactness",
        "splitting",
    ]  # Pulled 'extended' scoring out separately

    n_districts: int = metadata["D"]
    n_counties: int = metadata["C"]

    # region - Get the dataset keys
    census_dataset: DatasetKey
    vap_dataset: DatasetKey
    cvap_dataset: DatasetKey
    election_datasets: List[DatasetKey]
    shapes_dataset: DatasetKey
    census_dataset, vap_dataset, cvap_dataset, election_datasets, shapes_dataset = (
        get_dataset_keys(data_map)
    )
    # endregion

    # region - Set up the scorecard & new by-district aggregates
    scorecard: Dict[str, Any] = setup_scorecard(
        census_dataset,
        vap_dataset,
        cvap_dataset,
        election_datasets,
        shapes_dataset,
        mode,
    )
    compactness_by_district: Dict[str, List[float]] = dict()
    splitting_by_district: Dict[str, List[float]] = dict()
    # endregion

    if mode in ["all", "general"]:  # 'general' mode
        score_general_mode(
            aggs,
            census_dataset,
            n_districts,
            scorecard,
        )

    if mode in ["all", "partisan"]:  # 'partisan' mode
        for election_dataset in election_datasets:
            score_partisan_mode(
                aggs,
                election_dataset,
                n_districts,
                precomputed,
                scorecard,
            )

    if mode in ["all", "minority"]:  # 'minority' mode
        score_minority_mode(
            aggs,
            vap_dataset,
            cvap_dataset,
            data_map,
            n_districts,
            scorecard,
            mmd_scoring=mmd_scoring,
        )

    if mode in ["all", "compactness"]:  # 'compactness' mode
        score_compactness_mode(
            aggs,
            shapes_dataset,
            n_districts,
            assignments,
            graph,
            data,
            data_map,
            scorecard,
            compactness_by_district,
        )

    if mode in ["all", "splitting"]:  # 'splitting' mode
        score_splitting_mode(
            aggs,
            census_dataset,
            n_districts,
            n_counties,
            scorecard,
            splitting_by_district,
            reverse_weight_splitting=reverse_weight_splitting,
        )

    # Update the by-district aggregates
    new_aggs: Aggregates = update_aggregates(
        aggs,
        mode,
        shapes_dataset,
        census_dataset,
        compactness_by_district,
        splitting_by_district,
    )

    # Trim the floating point numbers
    trim_scores(scorecard)

    return scorecard, new_aggs


### SCORING HELPERS ###


def setup_scorecard(
    census_dataset: DatasetKey,
    vap_dataset: DatasetKey,
    cvap_dataset: DatasetKey,
    election_datasets: List[DatasetKey],
    shapes_dataset: DatasetKey,
    mode: str,
) -> Dict[str, Any]:
    """Set up the scorecard structure."""

    scorecard: Dict[str, Any] = {
        "census": {census_dataset: {}},
        "vap": {vap_dataset: {}},
        "cvap": {cvap_dataset: {}},
        "election": {e: {} for e in election_datasets},
        "shapes": {shapes_dataset: {}},
    }

    # ... but limit the scorecard to just the needed dataset types.

    if mode not in ["all", "general", "splitting"]:
        scorecard.pop("census", None)

    if mode not in ["all", "minority"]:
        scorecard.pop("vap", None)
        scorecard.pop("cvap", None)

    if mode not in ["all", "partisan"]:
        scorecard.pop("election", None)

    if mode not in ["all", "compactness"]:
        scorecard.pop("shapes", None)

    return scorecard


def score_general_mode(
    aggs: Aggregates,
    census_dataset: DatasetKey,
    n_districts: int,
    scorecard: Dict[str, Any],  # NOTE - updated
) -> None:
    """Score the general mode."""

    general_metrics: Dict[str, Any] = calc_general_category(
        aggs["census"][census_dataset],
        n_districts,
    )
    deviation: float = general_metrics.pop("population_deviation")
    scorecard["census"][census_dataset]["population_deviation"] = deviation


def score_partisan_mode(
    aggs: Aggregates,
    election_dataset: DatasetKey,
    n_districts: int,
    precomputed: Dict[str, Any],
    scorecard: Dict[str, Any],  # NOTE - updated
) -> None:
    """Score the partisan mode."""

    geographic_baselines: Dict[str, Any] = dict()
    if (
        precomputed
        and "geographic_baseline" in precomputed
        and election_dataset in precomputed["geographic_baseline"]
    ):
        geographic_baselines = precomputed["geographic_baseline"][election_dataset]
    partisan_metrics: Dict[str, Optional[float]] = calc_partisan_category(
        aggs["election"][election_dataset], n_districts, geographic_baselines
    )
    # estimated_seat_pct = partisan_metrics.pop("estimated_seat_pct")
    estimated_seats = partisan_metrics["estimated_seats"]
    assert estimated_seats is not None
    estimated_seat_pct: float = estimated_seats / n_districts
    assert estimated_seat_pct is not None
    scorecard["election"][election_dataset].update(partisan_metrics)

    scorecard["election"][election_dataset]["proportionality"] = _rate_proportionality(
        scorecard["election"][election_dataset]["pr_deviation"],
        scorecard["election"][election_dataset]["estimated_vote_pct"],
        estimated_seat_pct,
    )
    scorecard["election"][election_dataset]["competitiveness"] = _rate_competitiveness(
        scorecard["election"][election_dataset]["competitive_districts"] / n_districts
    )


def score_minority_mode(
    aggs: Aggregates,
    vap_dataset: DatasetKey,
    cvap_dataset: DatasetKey,
    data_map: Dict[str, Any],
    n_districts: int,
    scorecard: Dict[str, Any],
    *,
    mmd_scoring: bool = True,  # NOTE - This is majority-minority district (MMD) scoring!
):
    """Score minority mode."""

    vap_keys: List[str] = list(get_fields(data_map, "vap", vap_dataset).keys())

    if mmd_scoring:
        mmd_counts: Dict[str, int] = calculate_mmd_simple(aggs["cvap"][cvap_dataset])
        scorecard["cvap"][cvap_dataset].update(mmd_counts)

    # Revised minority ratings that don't clip Black VAP % below 37%

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


def score_compactness_mode(
    aggs: Aggregates,
    shapes_dataset: DatasetKey,
    n_districts: int,
    assignments: Dict[Precinct, District],
    graph: Dict[str, List[str]],
    data: List[Dict[str, Any]],
    data_map: Dict[str, Any],
    scorecard: Dict[str, Any],  # NOTE - updated
    compactness_by_district: Dict[str, List[float]],  # NOTE - updated
):
    """Score compactness mode."""

    by_district: Dict[str, List[float]] = calc_compactness_category(
        aggs["shapes"][shapes_dataset], n_districts
    )
    compactness_metrics: Dict[str, float] = {
        "reock": by_district["reock"][0],
        "polsby_popper": by_district["polsby_popper"][0],
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
    compactness_by_district.update(by_district)


def score_splitting_mode(
    aggs: Aggregates,
    census_dataset: DatasetKey,
    n_districts: int,
    n_counties: int,
    scorecard: Dict[str, Any],  # NOTE - updated
    splitting_by_district: Dict[str, List[float]],  # NOTE - updated
    *,
    reverse_weight_splitting: bool = False,
):
    """Score splitting mode."""

    splitting_metrics: Dict[str, float]
    by_district: Dict[str, List[float]]
    splitting_metrics, by_district = calc_splitting_category(
        aggs["census"][census_dataset], n_districts
    )
    scorecard["census"][census_dataset].update(splitting_metrics)
    scorecard["census"][census_dataset]["splitting"] = _rate_splitting(
        scorecard["census"][census_dataset]["county_splitting"],
        scorecard["census"][census_dataset]["district_splitting"],
        n_counties,
        n_districts,
    )

    # 10-18-25 -- Added reverse-weighted splitting metrics for experimentation

    if reverse_weight_splitting:
        temp: Dict[str, float]
        temp, _ = calc_splitting_category(
            aggs["census"][census_dataset],
            n_districts,
            reverse_weight=reverse_weight_splitting,
        )
        reverse_weighted_splitting_metrics: Dict[str, float] = {
            "county_splitting_reverse": temp["county_splitting"],
            # "district_splitting_reverse": temp["district_splitting"], # Same as normal
        }
        scorecard["census"][census_dataset].update(reverse_weighted_splitting_metrics)
        scorecard["census"][census_dataset]["splitting_reverse"] = _rate_splitting(
            scorecard["census"][census_dataset]["county_splitting_reverse"],
            scorecard["census"][census_dataset]["district_splitting"],
            n_counties,
            n_districts,
        )

    splitting_by_district.update(by_district)


def update_aggregates(
    aggs: Aggregates,
    mode: str,
    shapes_dataset: DatasetKey,
    census_dataset: DatasetKey,
    compactness_by_district: Dict[str, List[float]],
    splitting_by_district: Dict[str, List[float]],
) -> Aggregates:
    """Update the aggregates with by-district metrics generated during scoring."""

    new_aggs: Aggregates = aggs.copy()
    if mode in ["all", "compactness"]:
        new_aggs["shapes"][shapes_dataset].update(compactness_by_district)
    if mode in ["all", "splitting"]:
        new_aggs["census"][census_dataset].update(splitting_by_district)
        new_aggs["census"][census_dataset].pop("CxD")

    return new_aggs


def trim_scores(
    scorecard: Dict[str, Any],  # NOTE - updated
    *,
    precision: int = 4,
) -> Dict[str, Any]:
    """Trim floating point numbers in the scorecard to the given precision."""

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

    return scorecard


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
