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
from collections import defaultdict

# NOTE -- This is a relative reference w/in the project, not a use of a `pip install`ed package.
import rdapy as rda

from .utils import Precinct, District
from .aggregate import (
    get_dataset,
    get_fields,
    DatasetKey,
    Aggregates,
    NamedAggregates,
)
from .partisan import calc_efficiency_gap_wasted_votes, calc_average_margin
from .majority_minority import calculate_mmd_simple
from .discrete_compactness import (
    calc_cut_score,
    calc_spanning_tree_score,
    split_graph_by_districts,
)
from .energy import calc_energy


def score_plans(
    input_stream: TextIO,
    output_stream: TextIO,
    input_data: List[Dict[str, Any]],
    data_map: Dict[str, Any],
    adjacency_graph: Dict[str, List[str]],
    metadata: Dict[str, Any],
    mode: str,
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
    mmd_scoring: bool = True,  # If False, don't do MMD scoring for backwards compatibility w/ tests.
    add_spanning_tree_score: bool = False,  # Too expensive for scoring plans in bulk.
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

    # TODO - Enable specific & multiple datasets per type
    datasets: Dict[str, str] = default_datasets(data_map)

    n_districts: int = metadata["D"]
    n_counties: int = metadata["C"]

    scorecard: Dict[str, Any] = dict()

    if mode in ["all", "general"]:
        deviation: float = calc_population_deviation(
            aggs["census"][datasets["census"]],
            n_districts,
        )
        scorecard["population_deviation"] = deviation

    if mode in ["all", "partisan"]:
        partisan_metrics: Dict[str, Optional[float]] = calc_partisan_metrics(
            aggs["election"][datasets["election"]],
            n_districts,
        )
        estimated_seat_pct = partisan_metrics.pop("estimated_seat_pct")
        assert estimated_seat_pct is not None
        scorecard.update(partisan_metrics)

        scorecard["proportionality"] = rate_proportionality(
            scorecard["pr_deviation"],
            scorecard["estimated_vote_pct"],
            estimated_seat_pct,
        )
        scorecard["competitiveness"] = rate_competitiveness(
            scorecard["competitive_districts"] / n_districts
        )

    if mode in ["all", "minority"]:
        vap_dataset: DatasetKey = get_dataset(data_map, "vap")
        vap_keys: List[str] = list(get_fields(data_map, "vap", vap_dataset).keys())

        if mmd_scoring:
            mmd_counts: Dict[str, int] = calculate_mmd_simple(
                aggs["cvap"][datasets["cvap"]]
            )
            scorecard.update(mmd_counts)

        # Revised minority ratings that don't click Black VAP % below 37%

        alt_minority_metrics: Dict[str, float] = (
            calc_minority_metrics(  # Was: calc_alt_minority_metrics(
                aggs["vap"][datasets["vap"]], n_districts, vap_keys
            )
        )
        scorecard.update(alt_minority_metrics)

        scorecard["minority"] = rate_minority_opportunity(
            alt_minority_metrics["opportunity_districts"],
            alt_minority_metrics["proportional_opportunities"],
            alt_minority_metrics["coalition_districts"],
            alt_minority_metrics["proportional_coalitions"],
        )

    if mode in ["all", "compactness"]:
        compactness_by_district: Dict[str, List[float]] = calc_compactness_metrics(
            aggs["shapes"][datasets["shapes"]], n_districts
        )
        compactness_metrics: Dict[str, float] = {
            "reock": compactness_by_district["reock"][0],
            "polsby_popper": compactness_by_district["polsby_popper"][0],
        }

        # Additional discrete compactness metrics
        cut_score: int = calc_cut_score(assignments, graph)
        compactness_metrics["cut_score"] = cut_score

        if add_spanning_tree_score:
            district_graphs = split_graph_by_districts(graph, assignments)
            spanning_tree_by_district: List[Dict[str, float]] = [
                {"spanning_tree_score": calc_spanning_tree_score(g)}
                for g in district_graphs.values()
            ]
            spanning_tree_score: float = sum(
                d["spanning_tree_score"] for d in spanning_tree_by_district
            )
            compactness_metrics["spanning_tree_score"] = spanning_tree_score

        # Population compactness
        census_dataset: DatasetKey = get_dataset(data_map, "census")
        pop_field: str = get_fields(data_map, "census", census_dataset)["total_pop"]
        energy: float = calc_energy(assignments, data, pop_field)  # type: ignore
        compactness_metrics["population_compactness"] = energy

        scorecard.update(compactness_metrics)

        scorecard["compactness"] = rate_compactness(
            scorecard["reock"], scorecard["polsby_popper"]
        )

    if mode in ["all", "splitting"]:
        splitting_metrics: Dict[str, float]
        splitting_by_district: Dict[str, List[float]]
        splitting_metrics, splitting_by_district = calc_splitting_metrics(
            aggs["census"][datasets["census"]], n_districts
        )
        scorecard.update(splitting_metrics)
        scorecard["splitting"] = rate_splitting(
            scorecard["county_splitting"],
            scorecard["district_splitting"],
            n_counties,
            n_districts,
        )

    # Combine the by-district metrics
    new_aggs: Aggregates = aggs.copy()
    if mode in ["all", "compactness"]:
        new_aggs["shapes"][datasets["shapes"]].update(compactness_by_district)
    if mode in ["all", "splitting"]:
        new_aggs["census"][datasets["census"]].update(splitting_by_district)
        new_aggs["census"][datasets["census"]].pop("CxD")

    # Trim the floating point numbers
    precision: int = 4
    int_metrics: List[str] = [
        "pr_seats",
        "fptp_seats",
        "proportional_opportunities",
        "proportional_coalitions",
        "cut_score",
        "spanning_tree_score",
        "counties_split",
        "county_splits",
        "proportionality",
        "competitiveness",
        "minority",
        "minority_alt",
        "compactness",
        "splitting",
        "mod_districts",
    ]
    for metric in scorecard:
        if scorecard[metric] is None or metric == "by_district":
            continue
        if metric not in int_metrics:
            scorecard[metric] = round(scorecard[metric], precision)

    return scorecard, new_aggs


def default_datasets(input_metadata: Dict[str, Any]) -> Dict[str, str]:
    """Get the default/first datasets"""

    datasets: Dict[str, str] = {
        "census": get_dataset(input_metadata, "census"),
        "vap": get_dataset(input_metadata, "vap"),
        "cvap": get_dataset(input_metadata, "cvap"),
        "election": get_dataset(input_metadata, "election"),
        "shapes": get_dataset(input_metadata, "shapes"),
    }

    return datasets


### CALCULATE ANALYTICS BY AREA ###


def calc_population_deviation(data: NamedAggregates, n_districts: int) -> float:
    """Calculate population deviation."""

    pop_by_district: List[int] = data["pop_by_district"][1:]
    total_pop: int = data["pop_by_district"][0]

    max_pop: int = max(pop_by_district)
    min_pop: int = min(pop_by_district)
    target_pop: int = int(total_pop / n_districts)

    deviation: float = rda.calc_population_deviation(max_pop, min_pop, target_pop)

    return deviation


def calc_partisan_metrics(
    data: NamedAggregates, n_districts: int
) -> Dict[str, Optional[float]]:
    """Calulate partisan metrics."""

    total_d_votes: int = data["dem_by_district"][0]
    total_votes: int = data["tot_by_district"][0]
    d_by_district: List[int] = data["dem_by_district"][1:]
    tot_by_district: List[int] = data["tot_by_district"][1:]
    r_by_district: List[int] = [t - r for t, r in zip(tot_by_district, d_by_district)]

    partisan_metrics: Dict[str, Optional[float]] = dict()

    Vf: float = total_d_votes / total_votes
    Vf_array: List[float] = [d / tot for d, tot in zip(d_by_district, tot_by_district)]
    partisan_metrics["estimated_vote_pct"] = Vf

    all_results: dict = rda.calc_partisan_metrics(Vf, Vf_array)

    partisan_metrics["pr_deviation"] = all_results["bias"]["deviation"]
    partisan_metrics["estimated_seats"] = all_results["bias"]["estS"]
    partisan_metrics["estimated_seat_pct"] = all_results["bias"]["estSf"]
    partisan_metrics["fptp_seats"] = all_results["bias"]["fptpS"]

    partisan_metrics["disproportionality"] = all_results["bias"]["prop"]

    partisan_metrics["efficiency_gap_wasted_votes"] = calc_efficiency_gap_wasted_votes(
        d_by_district, r_by_district
    )
    Sf: float = partisan_metrics["fptp_seats"] / n_districts
    partisan_metrics["efficiency_gap_statewide"] = rda.calc_efficiency_gap(Vf, Sf)
    partisan_metrics["efficiency_gap"] = all_results["bias"]["eG"]

    partisan_metrics["seats_bias"] = all_results["bias"]["bS50"]
    partisan_metrics["votes_bias"] = all_results["bias"]["bV50"]
    partisan_metrics["geometric_seats_bias"] = all_results["bias"]["bSV"]

    partisan_metrics["declination"] = all_results["bias"]["decl"]
    partisan_metrics["mean_median_statewide"] = all_results["bias"]["mMs"]
    partisan_metrics["mean_median_average_district"] = all_results["bias"]["mMd"]
    partisan_metrics["turnout_bias"] = all_results["bias"]["tOf"]
    partisan_metrics["lopsided_outcomes"] = all_results["bias"]["lO"]

    partisan_metrics["competitive_district_count"] = all_results["responsiveness"][
        "cSimple"
    ]
    partisan_metrics["competitive_districts"] = all_results["responsiveness"]["cD"]
    partisan_metrics["average_margin"] = calc_average_margin(Vf_array)

    partisan_metrics["responsiveness"] = all_results["responsiveness"]["littleR"]
    partisan_metrics["responsive_districts"] = all_results["responsiveness"]["rD"]
    partisan_metrics["overall_responsiveness"] = all_results["responsiveness"]["bigR"]

    return partisan_metrics


def calc_minority_metrics(
    data: NamedAggregates,
    n_districts: int,
    vap_keys: List[str],
) -> Dict[str, float]:
    """Calculate minority metrics."""

    # Thunk aggregates into the format that rda.calc_minority_opportunity expects
    statewide_demos: Dict[str, float] = dict()
    for demo in vap_keys[1:]:  # Skip total VAP
        simple_demo: str = demo.split("_")[
            0
        ].lower()  # NOTE - To match what 'rdapy' expects
        statewide_demos[simple_demo] = data[demo][0] / data[vap_keys[0]][0]

    by_district: List[Dict[str, float]] = list()
    for i in range(n_districts):
        district_demos: Dict[str, float] = dict()
        for demo in vap_keys[1:]:  # Skip total VAP
            simple_demo: str = demo.split("_")[0].lower()
            district_demos[simple_demo] = data[demo][i + 1] / data[vap_keys[0]][i + 1]

        by_district.append(district_demos)

    minority_metrics: Dict[str, float] = rda.calc_minority_opportunity(
        statewide_demos, by_district, clip=False
    )

    return minority_metrics


def calc_compactness_metrics(
    data: NamedAggregates,  # All aggregates by district
    n_districts: int,
) -> Dict[str, List[float]]:
    """Calculate compactness metrics using implied district props."""

    tot_reock: float = 0
    tot_polsby: float = 0
    by_district: Dict[str, List[float]] = {"reock": [0.0], "polsby_popper": [0.0]}

    for d in range(1, n_districts + 1):
        reock: float = rda.reock_formula(data["area"][d], data["diameter"][d] / 2)
        polsby: float = rda.polsby_formula(data["area"][d], data["perimeter"][d])
        by_district["reock"].append(reock)
        by_district["polsby_popper"].append(polsby)

        tot_reock += reock
        tot_polsby += polsby

    avg_reock: float = tot_reock / n_districts
    avg_polsby: float = tot_polsby / n_districts

    by_district["reock"][0] = avg_reock
    by_district["polsby_popper"][0] = avg_polsby

    return by_district


def calc_splitting_metrics(
    data: NamedAggregates, n_districts: int
) -> Tuple[Dict[str, float], Dict[str, List[float]]]:
    """Calculate county-district splitting metrics."""

    CxD: List[List[float]] = data["CxD"]

    all_results: Dict[str, float] = rda.calc_county_district_splitting(CxD)

    splitting_metrics: Dict[str, float] = dict()
    splitting_metrics["county_splitting"] = all_results["county"]
    splitting_metrics["district_splitting"] = all_results["district"]

    # Calculate the # of counties split and the # of splits
    # In the CxD matrix, rows are districts, columns are counties.
    counties_split: int = 0
    county_splits: int = 0
    for j in range(len(CxD[0])):  # for each county
        # Find the number districts that have this county
        parts: int = 0
        for i in range(len(CxD)):  # for each district
            if CxD[i][j] > 0:
                parts += 1
        # If it's more than 1, increment the # of counties split and the # of splits
        if parts > 1:
            counties_split += 1
            county_splits += parts - 1

    splitting_metrics["counties_split"] = counties_split
    splitting_metrics["county_splits"] = county_splits

    # Calculate split scores by district
    # This is redundantly calculating intermediate values that rda.calc_county_district_splitting(CxD) above
    # does, but it's easier to recompute the constituents here than it is to tunnel them from rdapy.
    dT: list[float] = rda.district_totals(CxD)
    cT: list[float] = rda.county_totals(CxD)
    rD: list[list[float]] = rda.reduce_district_splits(CxD, cT)
    g: list[list[float]] = rda.calc_district_fractions(rD, dT)
    splitting_by_district: List[float] = district_split_scores(g)

    by_district: Dict[str, List[float]] = {
        "district_splitting": [splitting_metrics["district_splitting"]]
        + splitting_by_district
    }

    return splitting_metrics, by_district


def district_split_scores(g: List[List[float]]) -> List[float]:
    """Calculate split scores by district."""

    numD: int = len(g)
    by_district: List[float] = list()

    for i in range(numD):
        split_score: float = rda.district_split_score(i, g)
        by_district.append(split_score)

    return by_district


### RATING DIMENSIONS ###


def rate_proportionality(disproportionality: float, Vf: float, Sf: float) -> int:
    rating: int = rda.rate_proportionality(disproportionality, Vf, Sf)

    return rating


def rate_competitiveness(cdf: float) -> int:
    rating: int = rda.rate_competitiveness(cdf)

    return rating


def rate_minority_opportunity(od: float, pod: float, cd: float, pcd: float) -> int:
    rating: int = rda.rate_minority_opportunity(od, pod, cd, pcd)

    return rating


def rate_compactness(avg_reock: int, avg_polsby: int) -> int:
    reock_rating: int = rda.rate_reock(avg_reock)
    polsby_rating: int = rda.rate_polsby(avg_polsby)
    rating: int = rda.rate_compactness(reock_rating, polsby_rating)

    return rating


def rate_splitting(
    county_splitting: float,
    district_splitting: float,
    n_counties: int,
    n_districts: int,
) -> int:
    county_rating: int = rda.rate_county_splitting(
        county_splitting, n_counties, n_districts
    )
    district_rating: int = rda.rate_district_splitting(
        district_splitting, n_counties, n_districts
    )
    rating: int = rda.rate_splitting(county_rating, district_rating)

    return rating


### END ###
