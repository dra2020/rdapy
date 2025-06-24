#!/usr/bin/env python3

from .method import *
from .bias import *
from .more import *
from .responsiveness import *


def calc_partisan_metrics(Vf: float, Vf_array: List[float]) -> dict:
    """Calculate partisan metrics for a set of districts and statewide vote share.

    NOTE - The variable names here match those in the dra2020/dra-analytics TypeScript code.
    """

    proportional: bool = True  # shift

    N: int = len(Vf_array)

    bestS: int = calc_best_seats(N, Vf)
    bestSf: float = bestS / N

    fptpS: int = est_fptp_seats(Vf_array)

    estS: float = est_seats(Vf_array)
    estSf: float = estS / N

    deviation: float = calc_disproportionality_from_best(
        estSf, bestSf
    )  # This is the dis-proportionality

    dSVpoints: list[tuple[float, float]] = infer_sv_points(Vf, Vf_array, proportional)
    rSVpoints: list[tuple[float, float]] = infer_inverse_sv_points(dSVpoints, N)

    TOf: float = calc_turnout_bias(Vf, Vf_array)

    Bs50: float = est_seats_bias(dSVpoints, N)
    Bs50f: float = Bs50 / N
    Bv50f: float = est_votes_bias(dSVpoints, N)
    rvPoints: dict[str, float] = key_RV_points(Vf_array)
    decl: Optional[float] = calc_declination(Vf_array)
    gSym: Optional[float] = calc_global_symmetry(dSVpoints, rSVpoints, Bs50f, N)

    # Efficiency Gap (EG) variations
    # - Statewide using fractional seats
    # - Statewide using FPTP seats
    # - Wasted votes formula -- needs votes by district, so have to calculate separately
    EG: float = calc_efficiency_gap(Vf, estSf)
    EG_FPTP: float = calc_efficiency_gap(Vf, fptpS / N)
    # EG_wasted_votes: float = calc_efficiency_gap_wasted_votes(
    #     d_by_district, r_by_district
    # )

    BsGf: float = (
        est_geometric_seats_bias(Vf, dSVpoints, rSVpoints) / N
    )  # Convert to a fraction [0, 1]

    prop: float = calc_disproportionality(Vf, estSf)
    mMs: float = calc_mean_median_difference(Vf_array, Vf)
    mMd: float = calc_mean_median_difference(Vf_array)
    LO: Optional[float] = calc_lopsided_outcomes(Vf_array)

    # Calculate alternate responsiveness metrics for reference
    bigR: Optional[float] = calc_big_R(Vf, estSf)
    littleR: float = est_responsiveness(Vf, dSVpoints, N)
    MIR: Optional[float] = calc_minimal_inverse_responsiveness(Vf, littleR)
    rD: float = est_responsive_districts(Vf_array)
    rDf: float = rD / N

    gamma: Optional[float] = calc_gamma(Vf, estSf, littleR)

    Cn: int = count_competitive_districts(Vf_array)
    cD: float = est_competitive_districts(Vf_array)
    cDf: float = cD / N

    _DWins: list[float] = list(filter(lambda x: x > 0.5, Vf_array))
    _RWins: list[float] = list(
        filter(lambda x: x <= 0.5, Vf_array)
    )  # Ties credited to R's
    averageDVf: Optional[float] = sum(_DWins) / len(_DWins) if len(_DWins) > 0 else None
    averageRVf: Optional[float] = sum(_RWins) / len(_RWins) if len(_RWins) > 0 else None

    average_margin = calc_average_margin(Vf_array)

    # Build the JSON to match what is produced by the TypeScript code

    bias_measurements: dict = {
        "bestS": bestS,
        "bestSf": bestSf,
        "estS": estS,
        "estSf": estSf,
        "deviation": deviation,
        "tOf": TOf,
        "fptpS": fptpS,
        "bS50": Bs50f,
        "bV50": Bv50f,
        "decl": decl,
        "rvPoints": rvPoints,
        "gSym": gSym,
        "gamma": gamma,
        "eG": EG,
        "eGFPTP": EG_FPTP,
        "bSV": BsGf,
        "prop": prop,
        "mMs": mMs,
        "mMd": mMd,
        "lO": LO,
    }

    responsiveness_measurements: dict = {
        "cSimple": Cn,
        "cD": cD,
        "cDf": cDf,
        "bigR": bigR,
        "littleR": littleR,
        "mIR": MIR,
        "rD": rD,
        "rDf": rDf,
        "averageMargin": average_margin,
    }

    results: dict = {
        "bias": bias_measurements,
        "responsiveness": responsiveness_measurements,
        "dSVpoints": dSVpoints,
        "rSVpoints": rSVpoints,
        "averageDVf": averageDVf,
        "averageRVf": averageRVf,
    }

    return results


### END ###
