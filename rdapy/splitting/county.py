#!/usr/bin/env python3

"""
COUNTY-DISTRICT SPLITTING -- building on Moon Duchin's work
"""

import math
import copy


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


# TODO - HERE ...
def calc_county_fractions(
    CxD: list[list[float]], county_totals: list[float]
) -> list[list[float]]:
    """Calculate county fractions from the county-district splits and the county population totals"""

    nD: int = len(CxD)
    nC: int = len(CxD[0])

    f: list[list[float]] = [[0.0] * nC for i in range(nD)]

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

    g: list[list[float]] = [[0.0] * nC for i in range(nD)]

    for j in range(nC):
        for i in range(nD):
            if district_totals[i] > 0:
                g[i][j] = CxD[i][j] / district_totals[i]
            else:
                g[i][j] = 0.0

    return g


__all__ = [
    "split_score",
    "county_totals",
    "district_totals",
    "reduce_county_splits",
    "reduce_district_splits",
    "calc_county_weights",
    "calc_district_weights",
    "calc_county_fractions",
    "calc_district_fractions",
]

### END ###
