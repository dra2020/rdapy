#!/usr/bin/env python3

"""
Metrics:

* R = Big 'R'
* MIR = Minimal inverse responsiveness

TODO
"""

from typing import Optional

from .method import est_seat_probability
from .utils import *
from .constants import *


# Estimate responsiveness (R) at the statewide vote share


def est_responsiveness(statewide_vote_share, sv_curve_pts, total_seats):
    VOTE_SHARE = 0

    V1, S1 = lower_bracket(sv_curve_pts, statewide_vote_share, VOTE_SHARE)
    V2, S2 = upper_bracket(sv_curve_pts, statewide_vote_share, VOTE_SHARE)

    # NOTE - To get a proper slope, normalize the seat delta into a fraction!
    R = ((S2 - S1) / total_seats) / (V2 - V1)

    return R


# Estimate the number of responsive districts [R(d)], given a set of VPI's


def est_responsive_districts(vpi_by_district):
    return sum([est_district_responsiveness(vpi) for vpi in vpi_by_district])


# Estimate the responsiveness of a district, given a VPI


def est_district_responsiveness(vpi):
    return 1 - 4 * (est_seat_probability(vpi) - 0.5) ** 2


# BIG 'R': Defined in Footnote 22 on P. 10


def calc_big_R(Vf: float, Sf: float) -> Optional[float]:
    """BIG 'R'"""

    if roughly_equal(Vf, 0.5, EPSILON):
        return None  # Undefined
    else:
        return (Sf - 0.5) / (Vf - 0.5)


# MINIMAL INVERSE RESPONSIVENESS


def _is_balanced(Vf: float) -> bool:
    """Is the statewide vote share balanced?"""

    lower: float = 0.45
    upper: float = 0.55
    b_balanced: bool = False if (Vf > upper) or (Vf < lower) else True

    return b_balanced


def calc_minimal_inverse_responsiveness(Vf: float, r: float) -> Optional[float]:
    """MIR - Minimal inverse responsiveness

    zeta = (1 / r) - (1 / r_sub_max)     : Eq. 5.2.1

    where r_sub_max = 10 or 20 for balanced and unbalanced states, respectively.
    """

    if roughly_equal(r, 0, EPSILON):
        return None  # Undefined
    else:
        b_balanced: bool = _is_balanced(Vf)
        ideal: float = 0.1 if b_balanced else 0.2

        MIR = (1 / r) - ideal

        MIR = max(MIR, 0.0)

        return MIR


### END ###
