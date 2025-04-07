#!/usr/bin/env python3

"""
MINORITY OPPORTUNITY
"""

from collections import defaultdict
from typing import Optional

from ..partisan import est_seat_probability


def calc_proportional_districts(proportion: float, n_districts: int) -> int:
    """Calculate the whole number of districts that would be proportional."""

    round_up: float = 0.0
    fractional: float = proportion * n_districts
    integral: int = round(fractional + round_up)

    return integral


DEMOGRAPHICS: list[str] = [
    "white",
    "minority",
    "black",
    "hispanic",
    "pacific",
    "asian",
    "native",
]


def est_minority_opportunity(
    mf: float, demo: Optional[str] = None, clip: bool = True
) -> float:
    """Estimate the opportunity for a minority representation.

    NOTE - Shift minority proportions up, so 37% minority scores like 52% share,
      but use the uncompressed seat probability distribution. This makes a 37%
      district have a ~70% chance of winning, and a 50% district have a >99% chance.
      Below 37 % has no chance.
    NOTE - Sam Wang suggest 90% probability for a 37% district. That seems a little
      too abrupt and all or nothing, so I backed off to the ~70%.
    """

    assert mf >= 0.0

    range: list[float] = [0.37, 0.50]

    shift: float = 0.15  # For Black VAP % (and Minority)
    dilution: float = 0.50  # For other demos, dilute the Black shift by half
    if demo and (demo not in ["black", "minority"]):
        shift *= dilution

    wip_num: float = mf + shift

    if clip:
        # Original behavior with clipping at range[0]
        oppty: float = (
            0.0 if (mf < range[0]) else min(est_seat_probability(wip_num), 1.0)
        )
    else:
        # Alternative behavior without the low-end cutoff
        oppty: float = max(min(est_seat_probability(wip_num), 1.0), 0.0)

    return oppty


# TODO - DELETE
# def est_minority_opportunity(mf: float, demo: Optional[str] = None) -> float:
#     """Estimate the opportunity for a minority representation.

#     NOTE - Shift minority proportions up, so 37% minority scores like 52% share,
#       but use the uncompressed seat probability distribution. This makes a 37%
#       district have a ~70% chance of winning, and a 50% district have a >99% chance.
#       Below 37 % has no chance.
#     NOTE - Sam Wang suggest 90% probability for a 37% district. That seems a little
#       too abrupt and all or nothing, so I backed off to the ~70%.
#     """

#     assert mf >= 0.0

#     range: list[float] = [0.37, 0.50]

#     shift: float = 0.15  # For Black VAP % (and Minority)
#     dilution: float = 0.50  # For other demos, dilute the Black shift by half
#     if demo and (demo not in ["black", "minority"]):
#         shift *= dilution

#     wip_num: float = mf + shift
#     oppty: float = 0.0 if (mf < range[0]) else min(est_seat_probability(wip_num), 1.0)

#     return oppty


def calc_minority_opportunity(
    statewide_demos: dict[str, float],
    demos_by_district: list[dict[str, float]],
    clip: bool = True,
) -> dict[str, float]:
    """Estimate minority opportunity (everything except the table which is used in DRA)."""

    n_districts: int = len(demos_by_district)

    # Determine statewide proportional minority districts by single demographics (ignoring'White')
    districts_by_demo: dict[str, int] = {
        x: calc_proportional_districts(statewide_demos[x], n_districts)
        for x in DEMOGRAPHICS[1:]
    }

    # Sum the statewide proportional districts for each single demographic
    total_proportional: int = sum(
        [v for k, v in districts_by_demo.items() if k not in ["white", "minority"]]
    )

    # Sum the opportunities for minority represention in each district
    oppty_by_demo: dict[str, float] = defaultdict(float)
    for district in demos_by_district:
        for d in DEMOGRAPHICS[1:]:  # Ignore 'white'
            oppty_by_demo[d] += est_minority_opportunity(district[d], d, clip=clip)

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


### END ###
