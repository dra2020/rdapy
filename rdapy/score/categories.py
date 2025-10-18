"""
CALCULATE CATEGORIES OF SCORES (METRICS)
"""

from typing import Any, List, Dict, Tuple, Optional

from ..base import NamedAggregates
from ..equal import calc_population_deviation
from ..partisan import calc_partisan_metrics, calc_efficiency_gap_wasted_votes
from ..minority import calc_minority_metrics
from ..compactness import reock_formula, polsby_formula
from ..splitting.county import (
    calc_splitting_metrics,
    _calc_district_fractions,
    _county_totals,
    _district_split_score,
    _district_totals,
    _reduce_district_splits,
)


def calc_general_category(data: NamedAggregates, n_districts: int) -> Dict[str, Any]:
    """Calculate general metrics like population deviation."""

    general_metrics: Dict[str, Any] = dict()

    pop_by_district: List[int] = data["pop_by_district"][1:]
    total_pop: int = data["pop_by_district"][0]

    max_pop: int = max(pop_by_district)
    min_pop: int = min(pop_by_district)
    target_pop: int = int(total_pop / n_districts)

    deviation: float = calc_population_deviation(max_pop, min_pop, target_pop)

    general_metrics["population_deviation"] = deviation

    return general_metrics


##### PARTISAN CATEGORY #####


def calc_partisan_category(
    data: NamedAggregates, n_districts: int, geographic_baselines: Dict[str, Any]
) -> Dict[str, Optional[float]]:
    """Calulate partisan metrics."""

    # Get data for metrics

    total_d_votes: int = data["dem_by_district"][0]
    total_votes: int = data["tot_by_district"][0]
    d_by_district: List[int] = data["dem_by_district"][1:]
    tot_by_district: List[int] = data["tot_by_district"][1:]
    r_by_district: List[int] = [t - r for t, r in zip(tot_by_district, d_by_district)]

    Vf: float = total_d_votes / total_votes
    Vf_array: List[float] = [d / tot for d, tot in zip(d_by_district, tot_by_district)]

    all_results: dict = calc_partisan_metrics(Vf, Vf_array)

    # Flatten the partisan scorecard & rename metrics

    METRIC_MAPPING = {
        # Bias metrics
        "pr_deviation": ("bias", "deviation"),
        "estimated_seats": ("bias", "estS"),
        "fptp_seats": ("bias", "fptpS"),
        "disproportionality": ("bias", "prop"),
        "efficiency_gap": ("bias", "eG"),
        "efficiency_gap_FPTP": ("bias", "eGFPTP"),
        "seats_bias": ("bias", "bS50"),
        "votes_bias": ("bias", "bV50"),
        "geometric_seats_bias": ("bias", "bSV"),
        "declination": ("bias", "decl"),
        "mean_median_statewide": ("bias", "mMs"),
        "mean_median_average_district": ("bias", "mMd"),
        "turnout_bias": ("bias", "tOf"),
        "lopsided_outcomes": ("bias", "lO"),
        # Responsiveness metrics
        "competitive_district_count": ("responsiveness", "cSimple"),
        "competitive_districts": ("responsiveness", "cD"),
        "average_margin": ("responsiveness", "averageMargin"),
        "responsiveness": ("responsiveness", "littleR"),
        "responsive_districts": ("responsiveness", "rD"),
        "overall_responsiveness": ("responsiveness", "bigR"),
    }

    partisan_metrics: Dict[str, Optional[float]] = {
        key: all_results[category][metric_key]
        for key, (category, metric_key) in METRIC_MAPPING.items()
    }

    # Add a few more metrics

    partisan_metrics["estimated_vote_pct"] = Vf

    # NOTE - This formulate needs actual votes by district, not just the vote shares,
    # so we calculate it here separately.
    partisan_metrics["efficiency_gap_wasted_votes"] = calc_efficiency_gap_wasted_votes(
        d_by_district, r_by_district
    )

    if geographic_baselines and "whole_seats" in geographic_baselines:
        partisan_metrics["geographic_advantage"] = (
            partisan_metrics["estimated_seats"] - geographic_baselines["whole_seats"]
        )

    return partisan_metrics


##### MINORITY CATEGORY #####


def calc_minority_category(
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

    minority_metrics: Dict[str, float] = calc_minority_metrics(
        statewide_demos, by_district, clip=False
    )

    return minority_metrics


##### COMPACTNESS CATEGORY #####


def calc_compactness_category(
    data: NamedAggregates,  # All aggregates by district
    n_districts: int,
) -> Dict[str, List[float]]:
    """Calculate compactness metrics using implied district props."""

    tot_reock: float = 0
    tot_polsby: float = 0
    by_district: Dict[str, List[float]] = {"reock": [0.0], "polsby_popper": [0.0]}

    for d in range(1, n_districts + 1):
        reock: float = reock_formula(data["area"][d], data["diameter"][d] / 2)
        polsby: float = polsby_formula(data["area"][d], data["perimeter"][d])
        by_district["reock"].append(reock)
        by_district["polsby_popper"].append(polsby)

        tot_reock += reock
        tot_polsby += polsby

    avg_reock: float = tot_reock / n_districts
    avg_polsby: float = tot_polsby / n_districts

    by_district["reock"][0] = avg_reock
    by_district["polsby_popper"][0] = avg_polsby

    return by_district


##### SPLITTING CATEGORY #####


def calc_splitting_category(
    data: NamedAggregates, n_districts: int, reverse_weight: bool = False
) -> Tuple[Dict[str, float], Dict[str, List[float]]]:
    """Calculate county-district splitting metrics."""

    CxD: List[List[float]] = data["CxD"]

    all_results: Dict[str, float] = calc_splitting_metrics(
        CxD, reverse_weight=reverse_weight
    )

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
    dT: list[float] = _district_totals(CxD)
    cT: list[float] = _county_totals(CxD)
    rD: list[list[float]] = _reduce_district_splits(CxD, cT)
    g: list[list[float]] = _calc_district_fractions(rD, dT)
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
        split_score: float = _district_split_score(i, g)
        by_district.append(split_score)

    return by_district


### END ###
