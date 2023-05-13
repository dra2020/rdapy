#!/usr/bin/env python3

"""
UTILITIES for John Nagle's method
"""

import numpy as np
from typing import Optional


def roughly_equal(x: float, y: float, tolerance: float) -> bool:
    """Compare two numbers for approximate equality"""

    delta: float = abs(x - y)
    result: bool = True if delta < tolerance else False

    return result


def shift_range():
    """Define vote shifts over the middle of the S/V curve, including V = 50%"""

    shift_lower: float = 25 / 100
    shift_upper: float = 75 / 100
    shift_step: float = (1 / 100) / 2  # In 1/2% increments
    epsilon: float = 1.0e-12

    return np.arange(shift_lower, shift_upper + epsilon, shift_step)


def lower_bracket(
    sv_curve_pts: list[tuple[float, float]], value: float, v_or_s: int
) -> tuple[float, float]:
    """Find the point that brackets a value on the lower end"""

    LAST: int = -1

    smaller_pts: list[tuple[float, float]] = []
    for pt in sv_curve_pts:
        if pt[v_or_s] <= value:
            smaller_pts.append(pt)
    lower_pt: tuple[float, float] = smaller_pts[LAST]

    return lower_pt


def upper_bracket(
    sv_curve_pts: list[tuple[float, float]], value: float, v_or_s: int
) -> Optional[tuple[float, float]]:
    """Find the point that brackets a value on the upper end"""

    upper_pt: Optional[tuple[float, float]] = None
    for pt in sv_curve_pts:
        if pt[v_or_s] >= value:
            upper_pt = pt
            break
    return upper_pt


### END ###
