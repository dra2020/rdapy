#!/usr/bin/env python3

"""
MINORITY OPPORTUNITY
"""

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


def est_minority_opportunity(mf: float, demo: Optional[str] = None) -> float:
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
    oppty: float = 0.0 if (mf < range[0]) else min(est_seat_probability(wip_num), 1.0)

    return oppty


# makeMinorityScorecard

### END ###
