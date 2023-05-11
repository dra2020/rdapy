#!/usr/bin/env python3

"""
UTILITIES for John Nagle's method
"""

import numpy as np


def roughly_equal(x, y, tolerance):
    """Compare two numbers for approximate equality"""

    delta = abs(x - y)
    result = True if delta < tolerance else False

    return result


def shift_range(statewide_vote_share):
    """Define vote shifts over the middle of the S/V curve, including V = 50%"""

    shift_lower = 25 / 100
    shift_upper = 75 / 100
    shift_step = (1 / 100) / 2  # In 1/2% increments
    epsilon = 1.0e-12

    return np.arange(shift_lower, shift_upper + epsilon, shift_step)


def lower_bracket(sv_curve_pts, value, v_or_s):
    """Find the point that brackets a value on the lower end"""

    LAST = -1

    smaller_pts = []
    for pt in sv_curve_pts:
        if pt[v_or_s] <= value:
            smaller_pts.append(pt)
    lower_pt = smaller_pts[LAST]

    return lower_pt


def upper_bracket(sv_curve_pts, value, v_or_s):
    """Find the point that brackets a value on the upper end"""

    upper_pt = None
    for pt in sv_curve_pts:
        if pt[v_or_s] >= value:
            upper_pt = pt
            break
    return upper_pt


# __all__ = ["TODO"]

### END ###
