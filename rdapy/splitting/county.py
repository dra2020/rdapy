#!/usr/bin/env python3

"""
COUNTY-DISTRICT SPLITTING -- building on Moon Duchin's work
"""

from typing import List

import math
import copy


def calc_splitting_metrics(CxD: List[List[float]]) -> dict:
    """Calculate the county & district splitting scores for a plan."""

    dT: List[float] = _district_totals(CxD)
    cT: List[float] = _county_totals(CxD)
    county: float = _calc_county_splitting_reduced(CxD, dT, cT)
    district: float = _calc_district_splitting_reduced(CxD, dT, cT)

    out: dict = {"county": county, "district": district}

    return out


def split_score(split: List[float]) -> float:
    """Moon Duchin's raw split score"""

    if len(split) > 0:
        return sum(map(math.sqrt, split))
    else:
        return 1.0


### HELPERS ###

# NOTE - The county-district splits and the county & district totals may all,
# in general, be fractional/decimal numbers as opposed to integers, due to
# dissaggregation & re-aggregation. Hence, comparisons need to approximate
# equality.

# NOTE - Not sure why populations are floats instead of ints, but there must have
# been some instance in which the data were fractional.


def _county_totals(CxD: List[List[float]]) -> List[float]:
    """Total population of each county (column) in the CxD matrix"""

    nC: int = len(CxD[0])
    nD: int = len(CxD)
    totals: List[float] = [0.0] * nC

    for j in range(nC):
        for i in range(nD):
            totals[j] += CxD[i][j]

    return totals


def _district_totals(CxD: List[List[float]]) -> List[float]:
    """Total population of each district (row) in the CxD matrix"""

    nC: int = len(CxD[0])
    nD: int = len(CxD)
    totals: List[float] = [0.0] * nD

    for j in range(nC):
        for i in range(nD):
            totals[i] += CxD[i][j]

    return totals


def _reduce_county_splits(
    CxD: List[List[float]], dTotals: List[float]
) -> List[List[float]]:
    """Consolidate *whole districts* (w/in one county) UP into dummy district 0, county by county."""

    # Create the reduced template
    CxDreducedC: List[List[float]] = copy.deepcopy(CxD)
    nC: int = len(CxDreducedC[0])
    vRow: List[float] = [0.0] * nC
    CxDreducedC.insert(0, vRow)
    nD: int = len(CxDreducedC)

    for j in range(nC):
        # Skip the virtual district 0
        for i in range(1, nD):
            split_total: float = CxDreducedC[i][j]

            if split_total > 0:
                if math.isclose(split_total, dTotals[i - 1], abs_tol=1e-6):
                    CxDreducedC[0][j] += split_total
                    CxDreducedC[i][j] = 0

    return CxDreducedC


def _reduce_district_splits(
    CxD: List[List[float]], cTotals: List[float]
) -> List[List[float]]:
    """Consolidate *whole counties* (w/in one district) LEFT into the dummy county 0, district by district."""

    # Create the reduced template
    CxDreducedD: List[List[float]] = copy.deepcopy(CxD)
    for row in CxDreducedD:
        row.insert(0, 0.0)
    nC: int = len(CxDreducedD[0])
    nD: int = len(CxDreducedD)

    for i in range(nD):
        # Skip the virtual county 0
        for j in range(1, nC):
            split_total: float = CxDreducedD[i][j]

            if split_total > 0:
                if math.isclose(split_total, cTotals[j - 1], abs_tol=1e-6):
                    CxDreducedD[i][0] += split_total
                    CxDreducedD[i][j] = 0

    return CxDreducedD


def _calc_county_weights(
    county_totals: List[float], reverse_weight: bool = False
) -> List[float]:
    """Calculate county weights from the county population totals"""

    nC: int = len(county_totals)
    cTotal: float = sum(county_totals)

    w: List[float] = [0.0] * nC
    weight_fn = _reverse_weight if reverse_weight else _population_weight

    for j in range(nC):
        w[j] = weight_fn(county_totals[j], nC, cTotal)

    return w


def _population_weight(
    county_pop: float,
    ncounties: int,
    state_pop: float,
) -> float:
    """
    Weight counties by population.
    """

    w: float = county_pop / state_pop

    return w


def _reverse_weight(
    county_pop: float,
    ncounties: int,
    state_pop: float,
) -> float:
    """
    Calculate Don Leake's reverse weights for county splitting.

    "Reverse weighting formula: (S - c)/[(n-1)S], where S is the total population of the state,
    c is the population of the county, and n is the number of counties."
    """

    rw: float = (state_pop - county_pop) / ((ncounties - 1) * state_pop)

    return rw


def _calc_district_weights(district_totals: List[float]) -> List[float]:
    """Calculate district weights from the district population totals"""

    nD: int = len(district_totals)
    dTotal: float = sum(district_totals)

    x: List[float] = [0.0] * nD

    for i in range(nD):
        x[i] = district_totals[i] / dTotal

    return x


def _calc_county_fractions(
    CxD: List[List[float]], county_totals: List[float]
) -> List[List[float]]:
    """Calculate county fractions from the county-district splits and the county population totals"""

    nD: int = len(CxD)
    nC: int = len(CxD[0])

    f: List[List[float]] = [[0.0] * nC for d in range(nD)]

    for j in range(nC):
        for i in range(nD):
            if county_totals[j] > 0:
                f[i][j] = CxD[i][j] / county_totals[j]
            else:
                f[i][j] = 0.0

    return f


def _calc_district_fractions(
    CxD: List[List[float]], district_totals: List[float]
) -> List[List[float]]:
    """Calculate district fractions from the county-district splits and the district population totals"""

    nD: int = len(CxD)
    nC: int = len(CxD[0])

    g: List[List[float]] = [[0.0] * nC for d in range(nD)]

    for j in range(nC):
        for i in range(nD):
            if district_totals[i] > 0:
                g[i][j] = CxD[i][j] / district_totals[i]
            else:
                g[i][j] = 0.0

    return g


def _county_split_score(j: int, f: List[List[float]]) -> float:
    """For all districts in a county, sum the split score."""

    numD: int = len(f)
    splits: List[float] = []

    for i in range(numD):
        splits.append(f[i][j])

    score: float = split_score(splits)

    return score


def _district_split_score(i: int, g: List[List[float]]) -> float:
    """For all counties in a district, sum the split score."""

    numC: int = len(g[0])
    splits: List[float] = []

    for j in range(numC):
        splits.append(g[i][j])

    score: float = split_score(splits)

    return score


def _county_splitting(f: List[List[float]], w: List[float]) -> float:
    """For all counties, sum the weighted county splits."""

    numC: int = len(f[0])

    e: float = 0.0

    for j in range(numC):
        split_score: float = _county_split_score(j, f)
        e += w[j] * split_score

    return e


def _district_splitting(g: List[List[float]], x: List[float]) -> float:
    """For all districts, sum the weighted district splits."""

    numD: int = len(g)

    e: float = 0.0

    for i in range(numD):
        split_score: float = _district_split_score(i, g)
        e += x[i] * split_score

    return e


def _calc_county_splitting_reduced(
    CxD: List[List[float]],
    district_totals: List[float],
    county_totals: List[float],
    reverse_weight: bool = False,
) -> float:
    """Calculate the reduced county splitting score for a plan."""

    rC: List[List[float]] = _reduce_county_splits(CxD, district_totals)
    f: List[List[float]] = _calc_county_fractions(rC, county_totals)
    w: List[float] = _calc_county_weights(county_totals, reverse_weight=reverse_weight)

    rawSqEnt_DC: float = _county_splitting(f, w)

    return rawSqEnt_DC


def _calc_county_splitting(
    CxD: List[List[float]], district_totals: List[float], county_totals: List[float]
) -> float:
    """Calculate the county splitting score for a plan.

    *FOR TESTING*
    """

    f: List[List[float]] = _calc_county_fractions(CxD, county_totals)
    w: List[float] = _calc_county_weights(county_totals)

    SqEnt_DC: float = _county_splitting(f, w)

    return SqEnt_DC


def _calc_district_splitting_reduced(
    CxD: List[List[float]], district_totals: List[float], county_totals: List[float]
) -> float:
    """Calculate the reduced district splitting score for a plan."""

    rD: List[List[float]] = _reduce_district_splits(CxD, county_totals)
    g: List[List[float]] = _calc_district_fractions(rD, district_totals)
    x: List[float] = _calc_district_weights(district_totals)

    rawSqEnt_CD: float = _district_splitting(g, x)

    return rawSqEnt_CD


def _calc_district_splitting(
    CxD: List[List[float]], district_totals: List[float], county_totals: List[float]
) -> float:
    """Calculate the district splitting score for a plan.

    *FOR TESTING*
    """

    g: List[List[float]] = _calc_district_fractions(CxD, district_totals)
    x: List[float] = _calc_district_weights(district_totals)

    SqEnt_CD: float = _district_splitting(g, x)

    return SqEnt_CD


### END ###
