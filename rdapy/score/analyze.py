"""
ANALYZE ("SCORE") A PLAN
- There are 4 types of datasets -- census, VAP, election, and shapes.
- Input "data" can include multiple datasets of the same type -- e.g., multiple elections.
- Because a plan can be scored against more than one dataset of a given type,
  scores are always in the context of the dataset used in the scoring.

- For plan-level metrics, multiple sets of scores are disambiguated with prefixes
  that identify the dataset.
- For district-level metrics, each set of scores is wrapped in a dictionary with the dataset key.
"""

from collections import defaultdict
from typing import Any, List, Dict, Tuple, Optional

import rdapy as rda

from .utils import Precinct, District
from .aggregate import (
    get_dataset,
    get_fields,
    aggregate_districts,
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


def analyze_plan(
    plan: Dict[Precinct, District],
    data: List[Dict[str, Any]],
    graph: Dict[str, List[str]],
    metadata: Dict[str, Any],
    alt_minority: bool = True,  # If False, don't add alternative minority opportunity metrics
    mmd_scoring: bool = True,  # If True, add MMD scoring
    *,
    which: str = "all",  # Or one of "general", "partisan", "minority", "compactness", "splitting"
    data_metadata: Dict[str, Any],
    add_spanning_tree_score: bool = False,
) -> Dict[str, Any]:
    """Analyze a plan."""

    # Pulled 'extended' scoring moved out separately
    assert which in [
        "all",
        "general",
        "partisan",
        "minority",
        "compactness",
        "splitting",
    ]

    # TODO - Enable specific & multiple datasets per type
    datasets: Dict[str, str] = default_datasets(data_metadata)

    aggs: Aggregates = aggregate_districts(
        plan,
        data,
        graph,
        metadata,
        which=which,
        data_metadata=data_metadata,
    )

    n_districts: int = metadata["D"]
    n_counties: int = metadata["C"]

    scorecard: Dict[str, Any] = dict()

    if which in ["all", "general"]:
        deviation: float = calc_population_deviation(
            aggs["census"][datasets["census"]],
            n_districts,
        )
        scorecard["population_deviation"] = deviation

    if which in ["all", "partisan"]:
        partisan_metrics: Dict[str, Optional[float]] = calc_partisan_metrics(
            aggs["election"][datasets["election"]],
            n_districts,
        )
        # 2025-03-21: Added
        estimated_seat_pct = partisan_metrics.pop("estimated_seat_pct")
        assert estimated_seat_pct is not None
        scorecard.update(partisan_metrics)
        scorecard["proportionality"] = rate_proportionality(
            scorecard["pr_deviation"],
            scorecard["estimated_vote_pct"],
            estimated_seat_pct,  # 2025-03-21: Removed scorecard["estimated_seat_pct"],
        )
        scorecard["competitiveness"] = rate_competitiveness(
            scorecard["competitive_districts"]
            / n_districts  # 2025-03-21: scorecard["competitive_district_pct"]
        )

    if which in ["all", "minority"]:
        vap_dataset: DatasetKey = get_dataset(data_metadata, "vap")
        vap_keys: List[str] = list(get_fields(data_metadata, "vap", vap_dataset).keys())
        # 2025-03-21: Removed
        # minority_metrics = calc_minority_metrics(
        #     aggs["vap"][datasets["vap"]],
        #     n_districts,
        #     vap_keys,
        # )
        # scorecard.update(minority_metrics)
        # scorecard["minority"] = rate_minority_opportunity(
        #     scorecard["opportunity_districts"],
        #     scorecard["proportional_opportunities"],
        #     scorecard["coalition_districts"],
        #     scorecard["proportional_coalitions"],
        # )

        # 2025-03-21: Added
        if mmd_scoring:
            mmd_counts: Dict[str, int] = calculate_mmd_simple(
                aggs["cvap"][datasets["cvap"]]
            )
            scorecard.update(mmd_counts)

        # Alternate minority ratings
        if alt_minority:
            alt_minority_metrics: Dict[str, float] = calc_alt_minority_metrics(
                aggs["vap"][datasets["vap"]], n_districts, vap_keys
            )
            # 2025-03-21: Removed
            # subset: Dict[str, float] = {
            #     f"alt_{k}": v
            #     for k, v in alt_minority_metrics.items()
            #     if k
            #     in [
            #         "opportunity_districts",
            #         # 2025-03-21: Removed
            #         # "opportunity_districts_pct",
            #         "coalition_districts",
            #     ]
            # }
            scorecard.update(
                alt_minority_metrics
            )  # 2025-03-21: scorecard.update(subset)
            # 2025-03-21: Removed
            # scorecard["minority_alt"] = rate_minority_opportunity(
            scorecard["minority"] = rate_minority_opportunity(
                alt_minority_metrics["opportunity_districts"],
                alt_minority_metrics["proportional_opportunities"],
                alt_minority_metrics["coalition_districts"],
                alt_minority_metrics["proportional_coalitions"],
            )

    if which in ["all", "compactness"]:
        compactness_by_district: Dict[str, List[float]] = calc_compactness_metrics(
            aggs["shapes"][datasets["shapes"]], n_districts
        )
        compactness_metrics: Dict[str, float] = {
            "reock": compactness_by_district["reock"][0],
            "polsby_popper": compactness_by_district["polsby_popper"][0],
        }

        # Additional discrete compactness metrics
        cut_score: int = calc_cut_score(plan, graph)
        compactness_metrics["cut_score"] = cut_score

        if add_spanning_tree_score:
            district_graphs = split_graph_by_districts(graph, plan)
            spanning_tree_by_district: List[Dict[str, float]] = [
                {"spanning_tree_score": calc_spanning_tree_score(g)}
                for g in district_graphs.values()
            ]
            spanning_tree_score: float = sum(
                d["spanning_tree_score"] for d in spanning_tree_by_district
            )
            compactness_metrics["spanning_tree_score"] = spanning_tree_score

        # Population compactness
        census_dataset: DatasetKey = get_dataset(data_metadata, "census")
        pop_field: str = get_fields(data_metadata, "census", census_dataset)[
            "total_pop"
        ]
        energy: float = calc_energy(plan, data, pop_field)
        compactness_metrics["population_compactness"] = energy

        scorecard.update(compactness_metrics)
        scorecard["compactness"] = rate_compactness(
            scorecard["reock"], scorecard["polsby_popper"]
        )

    if which in ["all", "splitting"]:
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
    if which in ["all", "compactness"]:
        aggs["shapes"][datasets["shapes"]].update(compactness_by_district)
    if which in ["all", "splitting"]:
        aggs["census"][datasets["census"]].update(splitting_by_district)
        aggs["census"][datasets["census"]].pop("CxD")
    scorecard["by_district"] = aggs

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

    return scorecard


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
    # 2025-03-21: Removed
    # partisan_metrics["pr_seats"] = all_results["bias"]["bestS"]
    # 2025-03-21: Removed
    # partisan_metrics["pr_pct"] = all_results["bias"]["bestSf"]
    partisan_metrics["estimated_seats"] = all_results["bias"]["estS"]
    partisan_metrics["estimated_seat_pct"] = all_results["bias"]["estSf"]
    partisan_metrics["fptp_seats"] = all_results["bias"]["fptpS"]

    partisan_metrics["disproportionality"] = all_results["bias"]["prop"]

    # 2025-03-21: Added
    partisan_metrics["efficiency_gap_wasted_votes"] = calc_efficiency_gap_wasted_votes(
        d_by_district, r_by_district
    )
    Sf: float = partisan_metrics["fptp_seats"] / n_districts
    partisan_metrics["efficiency_gap_statewide"] = rda.calc_efficiency_gap(Vf, Sf)
    #
    partisan_metrics["efficiency_gap"] = all_results["bias"]["eG"]
    # 2025-03-21: Removed
    # partisan_metrics["gamma"] = all_results["bias"]["gamma"]

    partisan_metrics["seats_bias"] = all_results["bias"]["bS50"]
    partisan_metrics["votes_bias"] = all_results["bias"]["bV50"]
    partisan_metrics["geometric_seats_bias"] = all_results["bias"]["bSV"]
    # 2025-03-21: Removed
    # partisan_metrics["global_symmetry"] = all_results["bias"]["gSym"]

    partisan_metrics["declination"] = all_results["bias"]["decl"]
    partisan_metrics["mean_median_statewide"] = all_results["bias"]["mMs"]
    partisan_metrics["mean_median_average_district"] = all_results["bias"]["mMd"]
    partisan_metrics["turnout_bias"] = all_results["bias"]["tOf"]
    partisan_metrics["lopsided_outcomes"] = all_results["bias"]["lO"]

    partisan_metrics["competitive_district_count"] = all_results["responsiveness"][
        "cSimple"
    ]  # 2025-03-21: Added
    partisan_metrics["competitive_districts"] = all_results["responsiveness"]["cD"]
    # 2025-03-21: Removed
    # partisan_metrics["competitive_district_pct"] = all_results["responsiveness"]["cDf"]
    partisan_metrics["average_margin"] = calc_average_margin(Vf_array)

    partisan_metrics["responsiveness"] = all_results["responsiveness"]["littleR"]
    partisan_metrics["responsive_districts"] = all_results["responsiveness"]["rD"]
    # 2025-03-21: Removed
    # partisan_metrics["responsive_district_pct"] = all_results["responsiveness"]["rDf"]
    partisan_metrics["overall_responsiveness"] = all_results["responsiveness"]["bigR"]

    # 2025-03-21: Removed
    # partisan_metrics["avg_dem_win_pct"] = all_results["averageDVf"]
    # partisan_metrics["avg_rep_win_pct"] = (
    #     1.0 - all_results["averageRVf"]
    #     if all_results["averageRVf"] is not None
    #     else None
    # )

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
        statewide_demos, by_district
    )

    return minority_metrics


def est_alt_minority_opportunity(mf: float, demo: Optional[str] = None) -> float:
    """
    Estimate the ALTERNATE opportunity for a minority representation.

    NOTE - This is a slightly modified clone of est_minority_opportunity in rdapy.
    """

    assert mf >= 0.0

    # range: list[float] = [0.37, 0.50]

    shift: float = 0.15  # For Black VAP % (and Minority)
    dilution: float = 0.50  # For other demos, dilute the Black shift by half
    if demo and (demo not in ["black", "minority"]):
        shift *= dilution

    wip_num: float = mf + shift
    oppty: float = (
        # NOTE - This is the one-line change from est_minority_opportunity in rdapy,
        # i.e., don't clip VAP % below 37%.
        max(min(rda.est_seat_probability(wip_num), 1.0), 0.0)
        # 0.0 if (mf < range[0]) else min(rda.est_seat_probability(wip_num), 1.0)
    )

    return oppty


def calc_alt_minority_opportunity(
    statewide_demos: dict[str, float], demos_by_district: list[dict[str, float]]
) -> dict[str, float]:
    """
    Estimate ALTERNATE minority opportunity (everything except the table which is used in DRA).

    NOTE - This is a clone of calc_minority_opportunity in rdapy that uses
    and slightly modified est_alt_minority_opportunity above instead.
    """

    n_districts: int = len(demos_by_district)

    # Determine statewide proportional minority districts by single demographics (ignoring'White')
    districts_by_demo: dict[str, int] = {
        x: rda.calc_proportional_districts(statewide_demos[x], n_districts)
        for x in rda.DEMOGRAPHICS[1:]
    }

    # Sum the statewide proportional districts for each single demographic
    total_proportional: int = sum(
        [v for k, v in districts_by_demo.items() if k not in ["white", "minority"]]
    )

    # Sum the opportunities for minority represention in each district
    oppty_by_demo: dict[str, float] = defaultdict(float)
    for district in demos_by_district:
        for d in rda.DEMOGRAPHICS[1:]:  # Ignore 'white'
            # NOTE - Use the est_alt_minority_opportunity above, instead of est_minority_opportunity in rdapy.
            oppty_by_demo[d] += est_alt_minority_opportunity(district[d], d)

    # The # of opportunity districts for each separate demographic and all minorities
    od: float = sum(
        [v for k, v in oppty_by_demo.items() if k not in ["white", "minority"]]
    )
    cd: float = oppty_by_demo["minority"]

    # The # of proportional districts for each separate demographic and all minorities
    pod: float = total_proportional
    pcd: float = districts_by_demo["minority"]

    results: dict[str, float] = {
        # "pivot_by_demographic": table, # For this, use dra-analytics instead
        "opportunity_districts": od,
        "proportional_opportunities": pod,
        "coalition_districts": cd,
        "proportional_coalitions": pcd,
        # "details": {} # None
    }

    return results


def calc_alt_minority_metrics(
    data: NamedAggregates,
    n_districts: int,
    vap_keys: List[str],
) -> Dict[str, float]:
    """
    Calculate alternate minority metrics.

    NOTE - This is a clone of calc_minority_metrics that uses calc_alt_minority_opportunity above,
    instead of calc_minority_opportunity in rdapy.
    """

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

    # NOTE - Calc alternative minority metrics
    alt_minority_metrics: Dict[str, float] = calc_alt_minority_opportunity(
        statewide_demos, by_district
    )

    return alt_minority_metrics


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
