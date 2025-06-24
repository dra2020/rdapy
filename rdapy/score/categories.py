"""
CALCULATE CATEGORIES OF SCORES (METRICS)

TODO - Consolidate these
"""

from typing import Any, List, Dict, Tuple, Optional

import sys, json

# TODO -- This is a relative reference w/in the project to avoid a long list of imports,
# not a use of a `pip install`ed package
import rdapy as rda

from ..base import NamedAggregates
from ..equal import calc_population_deviation
from ..partisan import *  # calc_efficiency_gap_wasted_votes, calc_average_margin

# TODO -- Incorporate these
# from ..compactness import (
#     calc_cut_score,
#     calc_spanning_tree_score,
#     _split_graph_by_districts,
#     calc_energy,
# )
# from ..minority import calculate_mmd_simple


def calc_general_category(data: NamedAggregates, n_districts: int) -> Dict[str, Any]:
    """Calculate general metrics like population deviation."""

    general_metrics: Dict[str, Any] = dict()

    pop_by_district: List[int] = data["pop_by_district"][1:]
    total_pop: int = data["pop_by_district"][0]

    max_pop: int = max(pop_by_district)
    min_pop: int = min(pop_by_district)
    target_pop: int = int(total_pop / n_districts)

    deviation: float = rda.calc_population_deviation(max_pop, min_pop, target_pop)

    general_metrics["population_deviation"] = deviation

    return general_metrics


def calc_partisan_category(
    data: NamedAggregates, n_districts: int, geographic_baselines: Dict[str, Any]
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

    all_results: dict = calc_partisan_metrics(Vf, Vf_array)

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

    if geographic_baselines and "whole_seats" in geographic_baselines:
        partisan_metrics["geographic_advantage"] = (
            partisan_metrics["estimated_seats"] - geographic_baselines["whole_seats"]
        )

    partisan_metrics["competitive_district_count"] = all_results["responsiveness"][
        "cSimple"
    ]
    partisan_metrics["competitive_districts"] = all_results["responsiveness"]["cD"]
    partisan_metrics["average_margin"] = calc_average_margin(Vf_array)

    partisan_metrics["responsiveness"] = all_results["responsiveness"]["littleR"]
    partisan_metrics["responsive_districts"] = all_results["responsiveness"]["rD"]
    partisan_metrics["overall_responsiveness"] = all_results["responsiveness"]["bigR"]

    return partisan_metrics


def calc_partisan_metrics(Vf: float, Vf_array: list[float]) -> dict:
    """Calculate partisan metrics for a set of districts and statewide vote share.

    NOTE - The variable names here match those in the dra2020/dra-analytics TypeScript code.
    """

    proportional: bool = True  # shift

    N: int = len(Vf_array)

    bestS: int = calc_best_seats(N, Vf)
    bestSf: float = bestS / N

    fptpS: int = est_fptp_seats(Vf_array)

    estS: float = est_seats(Vf_array)
    estSf: float = estS / N

    deviation: float = calc_disproportionality_from_best(
        estSf, bestSf
    )  # This is the dis-proportionality

    dSVpoints: list[tuple[float, float]] = infer_sv_points(Vf, Vf_array, proportional)
    rSVpoints: list[tuple[float, float]] = infer_inverse_sv_points(dSVpoints, N)

    TOf: float = calc_turnout_bias(Vf, Vf_array)

    Bs50: float = est_seats_bias(dSVpoints, N)
    Bs50f: float = Bs50 / N
    Bv50f: float = est_votes_bias(dSVpoints, N)
    rvPoints: dict[str, float] = key_RV_points(Vf_array)
    decl: Optional[float] = calc_declination(Vf_array)
    gSym: Optional[float] = calc_global_symmetry(dSVpoints, rSVpoints, Bs50f, N)

    EG: float = calc_efficiency_gap(Vf, estSf)
    BsGf: float = (
        est_geometric_seats_bias(Vf, dSVpoints, rSVpoints) / N
    )  # Convert to a fraction [0, 1]

    prop: float = calc_disproportionality(Vf, estSf)
    mMs: float = calc_mean_median_difference(Vf_array, Vf)
    mMd: float = calc_mean_median_difference(Vf_array)
    LO: Optional[float] = calc_lopsided_outcomes(Vf_array)

    # Calculate alternate responsiveness metrics for reference
    bigR: Optional[float] = calc_big_R(Vf, estSf)
    littleR: float = est_responsiveness(Vf, dSVpoints, N)
    MIR: Optional[float] = calc_minimal_inverse_responsiveness(Vf, littleR)
    rD: float = est_responsive_districts(Vf_array)
    rDf: float = rD / N

    gamma: Optional[float] = calc_gamma(Vf, estSf, littleR)

    Cn: int = count_competitive_districts(Vf_array)
    cD: float = est_competitive_districts(Vf_array)
    cDf: float = cD / N

    _DWins: list[float] = list(filter(lambda x: x > 0.5, Vf_array))
    _RWins: list[float] = list(
        filter(lambda x: x <= 0.5, Vf_array)
    )  # Ties credited to R's
    averageDVf: Optional[float] = sum(_DWins) / len(_DWins) if len(_DWins) > 0 else None
    averageRVf: Optional[float] = sum(_RWins) / len(_RWins) if len(_RWins) > 0 else None

    # Build the JSON to match what is produced by the TypeScript code

    bias_measurements: dict = {
        "bestS": bestS,
        "bestSf": bestSf,
        "estS": estS,
        "estSf": estSf,
        "deviation": deviation,
        "tOf": TOf,
        "fptpS": fptpS,
        "bS50": Bs50f,
        "bV50": Bv50f,
        "decl": decl,
        "rvPoints": rvPoints,
        "gSym": gSym,
        "gamma": gamma,
        "eG": EG,
        "bSV": BsGf,
        "prop": prop,
        "mMs": mMs,
        "mMd": mMd,
        "lO": LO,
    }

    responsiveness_measurements: dict = {
        "cSimple": Cn,
        "cD": cD,
        "cDf": cDf,
        "bigR": bigR,
        "littleR": littleR,
        "mIR": MIR,
        "rD": rD,
        "rDf": rDf,
    }

    results: dict = {
        "bias": bias_measurements,
        "responsiveness": responsiveness_measurements,
        "dSVpoints": dSVpoints,
        "rSVpoints": rSVpoints,
        "averageDVf": averageDVf,
        "averageRVf": averageRVf,
    }

    return results


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
    splitting_by_district: List[float] = _district_split_scores(g)

    by_district: Dict[str, List[float]] = {
        "district_splitting": [splitting_metrics["district_splitting"]]
        + splitting_by_district
    }

    return splitting_metrics, by_district


### HELPERS ###


def _district_split_scores(g: List[List[float]]) -> List[float]:
    """Calculate split scores by district."""

    numD: int = len(g)
    by_district: List[float] = list()

    for i in range(numD):
        split_score: float = rda.district_split_score(i, g)
        by_district.append(split_score)

    return by_district


### END ###
