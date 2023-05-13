#!/usr/bin/env python3

"""
COMMUNITY OF INTEREST SPLITTING -- using Sam Wang's metrics
"""

import math


def calc_coi_splitting(communities: list[dict[str, list[float]]]) -> dict:
    """Calculate the COI metrics for a set of communities of interest."""

    by_coi: list[dict] = list()

    for coi in communities:
        es: float = effective_splits(coi["splits"])
        u: float = uncertainty_of_membership(coi["splits"])

        entry: dict = {"name": coi["name"], "effectiveSplits": es, "uncertainty": u}

        by_coi.append(entry)

    analysis: dict = {"byCOI": by_coi}

    return analysis


def uncertainty_of_membership(splits: list[float]) -> float:
    """Calculate the uncertainty of membership for a set of splits."""

    intermediate: list[float] = list(filter(lambda x: x > 0, splits))
    intermediate = list(map(lambda x: x * math.log2(x), intermediate))

    result: float = -1 * sum(intermediate)

    if result == -0.0:
        result = 0.0

    return result


def effective_splits(splits: list[float]) -> float:
    """Calculate the effective splits for a set of splits."""

    intermediate: list[float] = list(filter(lambda x: x > 0, splits))
    intermediate = list(map(lambda x: x**2, intermediate))

    result: float = (1 / sum(intermediate)) - 1

    if result == -0.0:
        result = 0.0

    return result


### END ###
