#!/usr/bin/env python3

from math import erf, sqrt, isclose
from scipy.interpolate import interp1d

# import numpy as np

from typing import Optional

from .utils import *


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


###


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


"""
"""


###

# Estimate the S/V seats measure of bias (@ V = 50%)


def est_seats_bias(sv_curve_pts, total_seats):
    d_seats = d_seats_at_half_share(sv_curve_pts)
    r_seats = total_seats - d_seats

    return (r_seats - d_seats) / 2.0


def d_seats_at_half_share(sv_curve_pts):
    close_pts = [pt for pt in sv_curve_pts if isclose(pt[0], 0.5)]
    _, d_seats = next(iter(close_pts))

    return d_seats


# Instead expressed as a percentage of the # of districts


def est_seats_bias_pct(seats_bias, total_seats):
    return seats_bias / float(total_seats)


# Interpolate the S/V votes measure of bias (for half the seats)


def est_votes_bias(sv_curve_pts, total_seats):
    half_seats = float(total_seats) / 2.0

    x = [x for x, y in sv_curve_pts]
    y = [y for x, y in sv_curve_pts]
    fn = interp1d(y, x, kind="cubic")

    return fn(half_seats) - 0.50


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


# Estimate geometric seats bias (@ V = statewide vote share)


def est_geometric_seats_bias(statewide_vote_share, b_gs_pts):
    x = [x for x, y in b_gs_pts]
    y = [y for x, y in b_gs_pts]
    fn = interp1d(x, y, kind="cubic")

    return fn(statewide_vote_share)


# Instead expressed as a percentage of the # of districts


def est_geometric_seats_bias_pct(b_gs, total_seats):
    return b_gs / float(total_seats)


# Estimate geometric votes bias (for the statewide seat share)


def est_geometric_votes_bias(d_sv_pts, r_sv_pts, statewide_seats):
    x = [x for x, y in r_sv_pts]
    y = [y for x, y in r_sv_pts]
    fn = interp1d(y, x, kind="cubic")

    v_r = fn(statewide_seats)

    x = [x for x, y in d_sv_pts]
    y = [y for x, y in d_sv_pts]
    fn = interp1d(y, x, kind="cubic")

    v_d = fn(statewide_seats)

    # NOTE - By convention: '+' = R bias; '-' = D bias
    return 0.5 * (v_d - v_r)


# Calculate the efficiency gap
# NOTE - This version is consistent with the rest of our metrics.
#   It's not the same as the version I've seen elsewhere, namely:
#   EG = (Seat Share – 50%)  – (2 × (Vote Share – 50%))


def efficiency_gap(vote_share, seat_share):
    return (-1 * (seat_share - 0.5)) + (2 * (vote_share - 0.5))


# Calculate new gamma measure
# g = 50 + r<V>(<V>-50) – S(<V>)
def calc_gamma(plan):
    return (
        0.5
        + plan.responsiveness * (plan.statewide_vote_share - 0.5)
        - (plan.predicted_D_seats / plan.districts)
    ) * 100


# __all__ = ["TODO"]

### END ###
