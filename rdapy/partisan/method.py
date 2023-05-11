#!/usr/bin/env python3

"""
Metrics:

* S! = the estimated number of Democratic seats using first past the post
* S# = the estimated Democratic seats, using seat probabilities
* S% = the estimated Democratic seat share fraction, calculated as S# / N

TODO
"""

from math import erf, sqrt, isclose

from typing import Optional

from .utils import *


def est_seat_share(seats: float, N: int) -> float:
    """S% - The estimated Democratic seat share fraction"""

    return seats / N


# INFER AN S/V CURVE


def infer_sv_points(
    statewide_vote_share, vpi_by_district, proportional=True, fptp=False
):
    sv_curve_pts = []
    vpis_at_half_share = []

    for shifted_vote_share in shift_range(statewide_vote_share):
        shifted_vpis = shift_districts(
            statewide_vote_share, vpi_by_district, shifted_vote_share, proportional
        )
        shifted_seats = est_statewide_seats(shifted_vpis, fptp)
        sv_curve_pts.append((shifted_vote_share, shifted_seats))

        # Squirrel away the inferred VPIs by district at V = 0.5
        if isclose(shifted_vote_share, 0.5):
            vpis_at_half_share = shifted_vpis

    return sv_curve_pts, vpis_at_half_share


# SHIFT DISTRICTS EITHER PROPORTIONALLY OR UNIFORMLY


def shift_districts(
    statewide_vote_share, vpi_by_district, shifted_vote_share, proportional=True
):
    if proportional:
        return shift_districts_proportionally(
            statewide_vote_share, vpi_by_district, shifted_vote_share
        )
    else:
        return shift_districts_uniformly(
            statewide_vote_share, vpi_by_district, shifted_vote_share
        )


def shift_districts_uniformly(
    statewide_vote_share, vpi_by_district, shifted_vote_share
):
    shift = shifted_vote_share - statewide_vote_share
    shifted_vpis = [(v + shift) for v in vpi_by_district]

    return shifted_vpis


def shift_districts_proportionally(
    statewide_vote_share, vpi_by_district, shifted_vote_share
):
    if shifted_vote_share < statewide_vote_share:
        # Shift down: D's to R's
        proportion = shifted_vote_share / statewide_vote_share
        shifted_vpis = [(v * proportion) for v in vpi_by_district]
    elif shifted_vote_share > statewide_vote_share:
        # Shift up: R's to D's
        proportion = (1 - shifted_vote_share) / (1 - statewide_vote_share)
        shifted_vpis = [(1 - (1 - v) * proportion) for v in vpi_by_district]
    else:
        # No shift: shift = actual
        shifted_vpis = vpi_by_district

    return shifted_vpis


# ESTIMATE THE STATEWIDE SEATS, GIVEN VPI'S BY DISTRICT,
# EITHER PROBABILISTICALLY OR BY FIRST PAST THE POST


def est_statewide_seats(vpi_by_district, fptp=False):
    if fptp:
        return est_statewide_seats_fptp(vpi_by_district)
    else:
        return est_statewide_seats_prob(vpi_by_district)


def est_statewide_seats_fptp(vpi_by_district):
    return sum([1.0 for vpi in vpi_by_district if (vpi > 0.5)])


def est_statewide_seats_prob(vpi_by_district):
    return sum([est_seat_probability(vpi) for vpi in vpi_by_district])


def est_seat_probability(vpi: float, range: Optional[list[float]] = None) -> float:
    """TODO"""

    if range is None:
        range = [0.25, 0.75]
    else:
        raise NotImplementedError  # TODO

    if vpi < range[0]:
        return 0.0
    elif vpi > range[1]:
        return 1.0
    else:
        return seat_probability_fn(vpi)


def seat_probability_fn(vpi: float):
    """Estimate the probability of a seat win for district, given a VPI"""

    return 0.5 * (1 + erf((vpi - 0.50) / (0.02 * sqrt(8))))


def est_seats(Vf_array: list[float], range: Optional[list[float]] = None) -> float:
    """The estimated # of Democratic seats, using seat probabilities"""

    return sum([est_seat_probability(vpi, range) for vpi in Vf_array])


# Infer inverse S/V curve


def infer_inverse_sv_points(ndistricts, statewide_vote_share, sv_pts):
    inverse_sv_curve_pts = []

    for v_d, s_d in sv_pts:
        v_r = 1 - v_d
        s_r = ndistricts - s_d  # # of seats, not seat share!
        inverse_sv_curve_pts.append((v_r, s_r))

    inverse_sv_curve_pts = sorted(inverse_sv_curve_pts, key=lambda pt: [pt[0]])

    return inverse_sv_curve_pts


# Infer a Bias of Geometric Seats (B_GS) curve


def infer_geometric_seats_bias_points(n_pts, d_sv_pts, r_sv_pts):
    b_gs_pts = []

    for i in range(0, n_pts):
        v_r, s_r = r_sv_pts[i]
        v_d, s_d = d_sv_pts[i]

        # NOTE - By convention: '+' = R bias; '-' = D bias
        b_gs = 0.5 * (s_r - s_d)

        b_gs_pts.append((v_d, b_gs))

    return b_gs_pts


### END ###
