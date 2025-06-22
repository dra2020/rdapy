#!/usr/bin/env python3

"""
Metrics:

* ^S#   = the Democratic seats closest to proportional
* ^S%   = the corresponding Democratic seat share
* B%    = the bias calculated as S% – ^S%

* PR    = Disproportionality
* EG    = Efficiency gap as a fraction
* gamma = Gamma

These 4 depend on the points of an inferred seats-votes curve:
* BS_50 = Seat bias as a fraction of N
* BV_50 = Votes bias as a fraction
* BS_V  = Seats bias @ <V> (geometric)
* GS    = Global symmetry

* decl  = Declination
* MM    = Mean – median difference using statewide Vf
* MM'   = Mean – median difference using average district v
* TO    = Turnout bias
* LO    = Lopsided outcomes

By convention, '+' = R bias; '-' = D bias
"""

from typing import Optional

import math
from scipy.interpolate import interp1d
import statistics

from ..base import EPSILON
from .method import est_seat_probability, est_seats, infer_geometric_seats_bias_points
from .utils import *


### BASIC BIAS ###


def calc_best_seats(N: int, Vf: float) -> int:
    """^S# - The # of Democratic seats closest to proportional @ statewide Vf

    The "expected number of seats" from http://bit.ly/2Fcuf4q
    """
    return round((N * Vf) - EPSILON)


def calc_disproportionality_from_best(est_Sf: float, best_Sf: float) -> float:
    """B% - The deviation from proportionality calculated as ^S% — S%"""

    return best_Sf - est_Sf


### ADVANCED BIAS ###

# PR - Eq.C.1.1 on P. 42


def calc_disproportionality(Vf: float, Sf: float) -> float:
    """PR - raw disproportionality"""

    return Vf - Sf


# EFFICIENCY GAP


def calc_efficiency_gap(Vf: float, Sf: float) -> float:
    """EG - Calculate the efficiency gap

    NOTE - This alternate formulation is consistent with the rest of our metrics,
    where '+' = R bias; '-' = D bias. It's *not* the same as the other common version:

    EG = (Seat Share – 50%)  – (2 × (Vote Share – 50%))
    """

    EG: float = (2 * (Vf - 0.5)) - (Sf - 0.5)

    return EG


# GAMMA


def calc_gamma(Vf: float, Sf: float, r: float) -> float:
    """GAMMA

    g = 50 + r<V>(<V>-50) – S(<V>)
    """

    return 0.5 + (r * (Vf - 0.5)) - Sf


# SEATS BIAS -- John Nagle's simple seat bias @ 50% (alpha), a fractional # of seats.


def est_seats_bias(sv_curve_pts: list[tuple[float, float]], N: int) -> float:
    """BS_50 - Seats bias as a fraction of N"""

    d_seats: float = _d_seats_at_half_share(sv_curve_pts)
    r_seats: float = N - d_seats

    return (r_seats - d_seats) / 2.0


def _d_seats_at_half_share(sv_curve_pts: list[tuple[float, float]]) -> float:
    close_pts = [pt for pt in sv_curve_pts if math.isclose(pt[0], 0.5)]
    _, d_seats = next(iter(close_pts))

    return d_seats


# VOTES BIAS -- John Nagle's simple vote bias @ 50% (alpha2), a percentage.


def est_votes_bias(sv_curve_pts: list[tuple[float, float]], N: int) -> float:
    """BV_50 - Votes bias as a fraction"""

    half_seats: float = float(N) / 2.0

    x: list[float] = [x for x, y in sv_curve_pts]
    y: list[float] = [y for x, y in sv_curve_pts]
    fn = interp1d(y, x, kind="cubic")

    return fn(half_seats) - 0.50


# GEOMETRIC SEATS BIAS (@ V = statewide vote share)


def est_geometric_seats_bias(
    Vf: float,
    d_sv_pts: list[tuple[float, float]],
    r_sv_pts: list[tuple[float, float]],
) -> float:
    """BS_V - Estimate geometric seats bias (@ V = statewide vote share)"""

    b_gs_pts: list[tuple[float, float]] = infer_geometric_seats_bias_points(
        d_sv_pts, r_sv_pts
    )

    x: list[float] = [x for x, y in b_gs_pts]
    y: list[float] = [y for x, y in b_gs_pts]
    fn = interp1d(x, y, kind="cubic")

    return fn(Vf)  # NOTE - Fractional # of seats, not seat share!


# GLOBAL SYMMETRY - Fig. 17 in Section 5.1


def calc_global_symmetry(
    d_sv_pts: list[tuple[float, float]],
    r_sv_pts: list[tuple[float, float]],
    S50V: float,
    N: int,
) -> float:
    """GS - Global symmetry

    * gSym is the area of asymmetry between the two curves.
    * The choice of what base to normalize it by is somewhat arbitrary.
    * We actually only infer the S–V curve over the range [0.25–0.75] <<< 101 points (not 100!)
    * But dividing by 100 normalizes the area of asymmetry to the area of the SxV unit square.
    """

    g_Sym: float = 0.0

    for i in range(len(d_sv_pts)):
        # 11/01/23 - Convert fractional seats to seat shares
        d_sf: float = d_sv_pts[i][1] / N
        r_sf: float = r_sv_pts[i][1] / N
        g_Sym += abs(d_sf - r_sf) / 2
        # g_Sym += abs(d_sv_pts[i][0] - r_sv_pts[i][0]) / 2

    sign: int = -1 if S50V < 0 else 1
    g_Sym *= sign

    return g_Sym / 100


# DECLINATION and helpers


def key_RV_points(Vf_array: list[float]) -> dict[str, float]:
    """Calculate the key declination r(v) points, defined in Fig. 16.

    NOTE - District vote shares are D shares, so party A = Rep & B = Dem.
    """

    n_districts: int = len(Vf_array)
    est_S: float = est_seats(Vf_array)

    Sb: float = est_S / n_districts  # Sb = Sf
    Ra: float = (1 + Sb) / 2
    Rb: float = Sb / 2

    Va: float = sum([est_seat_probability(1 - v) * (1 - v) for v in Vf_array]) / (
        n_districts - est_S
    )
    Vb: float = (
        1.0 - sum([est_seat_probability(v) * v for v in Vf_array]) / est_S
    )  # Vb = Vf

    # Make sure the results are in range (no floating point errors)
    Vb = min(Vb, 0.50)
    Va = max(Va, 0.50)

    key_points: dict[str, float] = {
        "Sb": Sb,
        "Ra": Ra,
        "Rb": Rb,
        "Va": Va,
        "Vb": Vb,
    }

    return key_points


def is_sweep(Sf: float, n_districts: int) -> bool:
    """Did one party win all the seats?"""

    one_district: float = 1 / n_districts
    b_sweep: bool = True if Sf > (1 - one_district) or Sf < one_district else False

    return b_sweep


def radians_to_degrees(radians: float) -> float:
    """Convert radians to degrees"""

    degrees: float = radians * (180 / math.pi)

    return degrees


def calc_declination(Vf_array: list[float]) -> Optional[float]:
    """Declination is calculated using the key r(v) points, defined in Fig. 16.

    NOTE - District vote shares are D shares, so party A = Rep & B = Dem.
    """

    key_points: dict[str, float] = key_RV_points(Vf_array)
    Sb: float = key_points["Sb"]
    Ra: float = key_points["Ra"]
    Rb: float = key_points["Rb"]
    Va: float = key_points["Va"]
    Vb: float = key_points["Vb"]

    b_sweep: bool = is_sweep(Sb, len(Vf_array))
    b_too_few_districts: bool = True if len(Vf_array) < 5 else False
    b_Va_at_50: bool = True if roughly_equal(Va - 0.5, 0.0, EPSILON) else False
    b_Vb_at_50: bool = True if roughly_equal(0.5 - Vb, 0.0, EPSILON) else False

    decl: Optional[float] = None

    if b_sweep or b_too_few_districts or b_Va_at_50 or b_Vb_at_50:
        decl = None  # Undefined
    else:
        l_tan: float = (Sb - Rb) / (0.5 - Vb)
        r_tan: float = (Ra - Sb) / (Va - 0.5)

        l_angle: float = radians_to_degrees(math.atan(l_tan))
        r_angle: float = radians_to_degrees(math.atan(r_tan))
        decl = r_angle - l_angle

    return decl


# MEAN–MEDIAN DIFFERENCE


def calc_mean_median_difference(
    Vf_array: list[float], Vf: Optional[float] = None
) -> float:
    """Both:
    * MM  - Mean – median difference using statewide Vf -and-
    * MM' - Mean – median difference using average district Vf
    """

    benchmark: float = Vf if Vf else statistics.mean(Vf_array)
    median_Vf: float = statistics.median(Vf_array)

    difference: float = benchmark - median_Vf

    return difference


# TURNOUT BIAS


def calc_turnout_bias(Vf: float, Vf_array: list[float]) -> float:
    """TO - Turnout bias

    The difference between the statewide turnout and the average district turnout
    """

    district_avg = statistics.mean(Vf_array)
    turnout_bias = Vf - district_avg

    return turnout_bias


# LOPSIDED OUTCOMES


def calc_lopsided_outcomes(Vf_array: list[float]) -> Optional[float]:
    """LO - Lopsided outcomes

    This is a measure of packing bias is:

    LO = (1⁄2 - vB) - (vA – 1⁄2)     Eq. 5.4.1 on P. 26

    "The ideal for this measure is that the excess vote share for districts
    won by party A averaged over those districts equals the excess vote share
    for districts won by party B averaged over those districts.
    A positive value of LO indicates greater packing of party B voters and,
    therefore, indicates a bias in favor of party A."
    """

    key_points: dict[str, float] = key_RV_points(Vf_array)
    Sb: float = key_points["Sb"]
    Va: float = key_points["Va"]
    Vb: float = key_points["Vb"]

    b_sweep: bool = is_sweep(Sb, len(Vf_array))

    if b_sweep:  # Undefined
        return None
    else:
        return (0.5 - Vb) - (Va - 0.5)


### END ###
