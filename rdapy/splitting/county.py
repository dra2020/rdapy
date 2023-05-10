#!/usr/bin/env python3

"""
COUNTY-DISTRICT SPLITTING -- building on Moon Duchin's work
"""

import math
import copy


def calc_splitting(CxD: list[list[float]]) -> dict:
    """Calculate the county & district splitting scores for a plan."""

    dT: list[float] = district_totals(CxD)
    cT: list[float] = county_totals(CxD)
    county: float = calc_county_splitting_reduced(CxD, dT, cT)
    district: float = calc_district_splitting_reduced(CxD, dT, cT)

    out: dict = {"county": county, "district": district}

    return out


def split_score(split: list[float]) -> float:
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


def county_totals(CxD: list[list[float]]) -> list[float]:
    """Total population of each county (column) in the CxD matrix"""

    nC: int = len(CxD[0])
    nD: int = len(CxD)
    totals: list[float] = [0.0] * nC

    for j in range(nC):
        for i in range(nD):
            totals[j] += CxD[i][j]

    return totals


def district_totals(CxD: list[list[float]]) -> list[float]:
    """Total population of each district (row) in the CxD matrix"""

    nC: int = len(CxD[0])
    nD: int = len(CxD)
    totals: list[float] = [0.0] * nD

    for j in range(nC):
        for i in range(nD):
            totals[i] += CxD[i][j]

    return totals


def reduce_county_splits(
    CxD: list[list[float]], dTotals: list[float]
) -> list[list[float]]:
    """Consolidate *whole districts* (w/in one county) UP into dummy district 0, county by county."""

    # Create the reduced template
    CxDreducedC: list[list[float]] = copy.deepcopy(CxD)
    nC: int = len(CxDreducedC[0])
    vRow: list[float] = [0.0] * nC
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


def reduce_district_splits(
    CxD: list[list[float]], cTotals: list[float]
) -> list[list[float]]:
    """Consolidate *whole counties* (w/in one district) LEFT into the dummy county 0, district by district."""

    # Create the reduced template
    CxDreducedD: list[list[float]] = copy.deepcopy(CxD)
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


def calc_county_weights(county_totals: list[float]) -> list[float]:
    """Calculate county weights from the county population totals"""

    nC: int = len(county_totals)
    cTotal: float = sum(county_totals)

    w: list[float] = [0.0] * nC

    for j in range(nC):
        w[j] = county_totals[j] / cTotal

    return w


def calc_district_weights(district_totals: list[float]) -> list[float]:
    """Calculate district weights from the district population totals"""

    nD: int = len(district_totals)
    dTotal: float = sum(district_totals)

    x: list[float] = [0.0] * nD

    for i in range(nD):
        x[i] = district_totals[i] / dTotal

    return x


def calc_county_fractions(
    CxD: list[list[float]], county_totals: list[float]
) -> list[list[float]]:
    """Calculate county fractions from the county-district splits and the county population totals"""

    nD: int = len(CxD)
    nC: int = len(CxD[0])

    f: list[list[float]] = [[0.0] * nC for d in range(nD)]

    for j in range(nC):
        for i in range(nD):
            if county_totals[j] > 0:
                f[i][j] = CxD[i][j] / county_totals[j]
            else:
                f[i][j] = 0.0

    return f


def calc_district_fractions(
    CxD: list[list[float]], district_totals: list[float]
) -> list[list[float]]:
    """Calculate district fractions from the county-district splits and the district population totals"""

    nD: int = len(CxD)
    nC: int = len(CxD[0])

    g: list[list[float]] = [[0.0] * nC for d in range(nD)]

    for j in range(nC):
        for i in range(nD):
            if district_totals[i] > 0:
                g[i][j] = CxD[i][j] / district_totals[i]
            else:
                g[i][j] = 0.0

    return g


def county_split_score(j: int, f: list[list[float]]) -> float:
    """For all districts in a county, sum the split score."""

    numD: int = len(f)
    splits: list[float] = []

    for i in range(numD):
        splits.append(f[i][j])

    score: float = split_score(splits)

    return score


def district_split_score(i: int, g: list[list[float]]) -> float:
    """For all counties in a district, sum the split score."""

    numC: int = len(g[0])
    splits: list[float] = []

    for j in range(numC):
        splits.append(g[i][j])

    score: float = split_score(splits)

    return score


def county_splitting(f: list[list[float]], w: list[float]) -> float:
    """For all counties, sum the weighted county splits."""

    numC: int = len(f[0])

    e: float = 0.0

    for j in range(numC):
        split_score: float = county_split_score(j, f)
        e += w[j] * split_score

    return e


def district_splitting(g: list[list[float]], x: list[float]) -> float:
    """For all districts, sum the weighted district splits."""

    numD: int = len(g)

    e: float = 0.0

    for i in range(numD):
        split_score: float = district_split_score(i, g)
        e += x[i] * split_score

    return e


def calc_county_splitting_reduced(
    CxD: list[list[float]], district_totals: list[float], county_totals: list[float]
) -> float:
    """Calculate the reduced county splitting score for a plan."""

    rC: list[list[float]] = reduce_county_splits(CxD, district_totals)
    f: list[list[float]] = calc_county_fractions(rC, county_totals)
    w: list[float] = calc_county_weights(county_totals)

    rawSqEnt_DC: float = county_splitting(f, w)

    return rawSqEnt_DC


def calc_county_splitting(
    CxD: list[list[float]], district_totals: list[float], county_totals: list[float]
) -> float:
    """Calculate the county splitting score for a plan.

    *FOR TESTING*
    """

    f: list[list[float]] = calc_county_fractions(CxD, county_totals)
    w: list[float] = calc_county_weights(county_totals)

    SqEnt_DC: float = county_splitting(f, w)

    return SqEnt_DC


def calc_district_splitting_reduced(
    CxD: list[list[float]], district_totals: list[float], county_totals: list[float]
) -> float:
    """Calculate the reduced district splitting score for a plan."""

    rD: list[list[float]] = reduce_district_splits(CxD, county_totals)
    g: list[list[float]] = calc_district_fractions(rD, district_totals)
    x: list[float] = calc_district_weights(district_totals)

    rawSqEnt_CD: float = district_splitting(g, x)

    return rawSqEnt_CD


def calc_district_splitting(
    CxD: list[list[float]], district_totals: list[float], county_totals: list[float]
) -> float:
    """Calculate the district splitting score for a plan.

    *FOR TESTING*
    """

    g: list[list[float]] = calc_district_fractions(CxD, district_totals)
    x: list[float] = calc_district_weights(district_totals)

    SqEnt_CD: float = district_splitting(g, x)

    return SqEnt_CD


__all__ = [
    "calc_splitting",
    "split_score",
    "county_totals",
    "district_totals",
    "reduce_county_splits",
    "reduce_district_splits",
    "calc_county_weights",
    "calc_district_weights",
    "calc_county_fractions",
    "calc_district_fractions",
    "county_split_score",
    "district_split_score",
    "county_splitting",
    "district_splitting",
    "calc_county_splitting_reduced",
    "calc_district_splitting_reduced",
    "calc_county_splitting",
    "calc_district_splitting",
]

### END ###
