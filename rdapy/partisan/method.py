#!/usr/bin/env python3

"""
The core elements of John Nagle's method.

Formulas:

* Estimate seat probability
* Estimate district responsiveness

Metrics:

* S# = the estimated Democratic seats, using seat probabilities
* S! = the estimated number of Democratic seats using first past the post

Seats-votes curves:

* Infer SV points
* Infer inverse SV points
* Infer geometric seats bias points
"""

from math import erf, sqrt, isclose

from typing import Optional

from .utils import *


# FORMULAS - John Nagle's two formulas for estimating seats & responsiveness


def est_seat_probability(vpi: float) -> float:
    """Estimate the fractional probability of a seat win for district, given a VPI"""

    return 0.5 * (1 + erf((vpi - 0.50) / (0.02 * sqrt(8))))


def est_district_responsiveness(vpi: float) -> float:
    """Estimate the responsiveness of a district, given a VPI"""

    return 1 - 4 * (est_seat_probability(vpi) - 0.5) ** 2


# ESTIMATE THE STATEWIDE SEATS, GIVEN VPI'S BY DISTRICT


def est_seats(Vf_array: list[float]) -> float:
    """S# - The estimated # of Democratic seats, using seat probabilities"""

    return sum([est_seat_probability(vpi) for vpi in Vf_array])


def est_seats_fptp(Vf_array: list[float]) -> float:
    """S! - The estimated # of Democratic seats, using first past the post"""

    return sum([1.0 for vpi in Vf_array if (vpi > 0.5)])


# INFER AN S/V CURVE


def infer_sv_points(Vf: float, Vf_array: list[float], proportional=True) -> list[tuple]:
    """Infer the points of an S/V curve from a set of VPI's by district,
    using either proportional or uniform shifts in statewide vote share."""

    sv_curve_pts = []

    for shifted_Vf in shift_range(Vf):
        shifted_Vf_array = _shift_districts(Vf, Vf_array, shifted_Vf, proportional)
        shifted_Sf = est_seats(shifted_Vf_array)
        sv_curve_pts.append((shifted_Vf, shifted_Sf))

    return sv_curve_pts


def _shift_districts(
    Vf: float, Vf_array: list[float], shifted_Vf: float, proportional: bool = True
) -> list[float]:
    """Shift the VPI's by district, using either proportional or uniform shifts in statewide vote share."""

    if proportional:
        return _shift_districts_proportionally(Vf, Vf_array, shifted_Vf)
    else:
        return _shift_districts_uniformly(Vf, Vf_array, shifted_Vf)


def _shift_districts_uniformly(
    Vf: float, Vf_array: list[float], shifted_Vf: float
) -> list[float]:
    """Shift the VPI's by district, using uniform shifts in statewide vote share."""

    shift: float = shifted_Vf - Vf
    shifted_vpis: list[float] = [(v + shift) for v in Vf_array]

    return shifted_vpis


def _shift_districts_proportionally(
    Vf: float, Vf_array: list[float], shifted_Vf: float
) -> list[float]:
    """Shift the VPI's by district, using proportional shifts in statewide vote share."""

    proportion: float
    shifted_Vf_array: list[float]

    if shifted_Vf < Vf:
        # Shift down: D's to R's
        proportion = shifted_Vf / Vf
        shifted_Vf_array = [(v * proportion) for v in Vf_array]
    elif shifted_Vf > Vf:
        # Shift up: R's to D's
        proportion = (1 - shifted_Vf) / (1 - Vf)
        shifted_Vf_array = [(1 - (1 - v) * proportion) for v in Vf_array]
    else:
        # No shift: shift = actual
        shifted_Vf_array = Vf_array

    return shifted_Vf_array


def infer_inverse_sv_points(
    N: int, Vf: float, sv_pts: list[tuple]
) -> list[tuple[float, float]]:
    """Infer the points of an inverse S/V curve from a set of S/V curve points."""

    inverse_sv_curve_pts: list[tuple[float, float]] = []

    for v_d, s_d in sv_pts:
        v_r: float = 1 - v_d
        s_r: float = N - s_d  # of seats, not seat share!
        inverse_sv_curve_pts.append((v_r, s_r))

    inverse_sv_curve_pts = sorted(inverse_sv_curve_pts, key=lambda pt: [pt[0]])

    return inverse_sv_curve_pts


def infer_geometric_seats_bias_points(
    d_sv_pts: list[tuple[float, float]], r_sv_pts: list[tuple[float, float]]
) -> list[tuple[float, float]]:
    """Infer a Bias of Geometric Seats (B_GS) curve"""

    b_gs_pts: list[tuple[float, float]] = []

    for i in range(0, len(d_sv_pts)):
        v_r: float
        s_r: float
        v_d: float
        s_d: float

        v_r, s_r = r_sv_pts[i]
        v_d, s_d = d_sv_pts[i]

        b_gs: float = 0.5 * (s_r - s_d)

        b_gs_pts.append((v_d, b_gs))

    return b_gs_pts


### END ###
