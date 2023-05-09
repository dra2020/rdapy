#!/usr/bin/env python3

"""
COUNTY-DISTRICT SPLITTING -- building on Moon Duchin's work
"""

import math


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


# LIMIT WHAT GETS EXPORTED.

__all__ = ["split_score", "county_totals", "district_totals"]

### END ###
