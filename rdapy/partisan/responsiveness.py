#!/usr/bin/env python3

"""
Competitiveness & responsiveness metrics:

* Cn  = Count the # of competitive districts, defined as [45–55%]
* cD  = The estimated # of competitive districts
* cDf = The estimated % of competitive districts (cD / N)
* r   = Responsiveness (little 'r') at the statewide vote share (Vf);
        depends on the points of an inferred seats-votes curve
* R   = Big 'R'
* MIR = Minimal inverse responsiveness
* rD  = The estimated fractional # of responsive districts
* rDf = The estimated fractional % of responsive districts (rD / N)
"""

from typing import Optional

from .method import est_district_responsiveness
from .utils import *
from .constants import *


# COMPETITIVENESS


def count_competitive_districts(Vf_array: list[float]) -> int:
    """Cn - Count the # of competitive districts, defined as [45–55%]."""

    count: int = 0
    for v in Vf_array:
        if (v >= 0.45) and (v <= 0.55):
            count += 1

    return count


def est_competitive_districts(Vf_array: list[float]) -> float:
    """cD - The estimated # of competitive districts"""

    return sum([est_district_competitiveness(v) for v in Vf_array])


def est_district_competitiveness(Vf: float) -> float:
    """Estimate the district competitiveness, a synonym for responsiveness."""

    return est_district_responsiveness(Vf)


# RESPONSIVENESS

# LITTLE 'r'


def est_responsiveness(
    Vf: float, sv_curve_pts: list[tuple[float, float]], N: int
) -> float:
    """Estimate responsiveness (little 'r') at the statewide vote share (Vf)"""

    VOTE_SHARE: int = 0  # Index of vote share in a (V, S) point tuple

    V1, S1 = lower_bracket(sv_curve_pts, Vf, VOTE_SHARE)
    V2, S2 = upper_bracket(sv_curve_pts, Vf, VOTE_SHARE)

    # NOTE - To get a proper slope, normalize the seat delta into a fraction!
    r: float = ((S2 - S1) / N) / (V2 - V1)

    return r


# BIG 'R': Defined in Footnote 22 on P. 10


def calc_big_R(Vf: float, Sf: float) -> Optional[float]:
    """BIG 'R'"""

    if roughly_equal(Vf, 0.5, EPSILON):
        return None  # Undefined
    else:
        return (Sf - 0.5) / (Vf - 0.5)


# MINIMAL INVERSE RESPONSIVENESS


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


def _is_balanced(Vf: float) -> bool:
    """Is the statewide vote share balanced?"""

    lower: float = 0.45
    upper: float = 0.55
    b_balanced: bool = False if (Vf > upper) or (Vf < lower) else True

    return b_balanced


# RESPONSIVE DISTRICTS


def est_responsive_districts(vpi_by_district) -> float:
    """Estimate the # of responsive districts [R(d)], given a set of VPI's"""

    return sum([est_district_responsiveness(vpi) for vpi in vpi_by_district])


### END ###
