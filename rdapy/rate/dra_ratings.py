#!/usr/bin/env python3

"""
DRA-SPECIFIC RATINGS ("SCORES")
"""

from .normalize import Normalizer, NORMALIZED_RANGE


### RATE PROPORTIONALITY ###


def rate_proportionality(raw_disproportionality: float, Vf: float, Sf: float) -> int:
    if is_antimajoritarian(Vf, Sf):
        return 0
    else:
        # Adjust bias to incorporate an acceptable winner's bonus based on Vf
        extra: float = extra_bonus(Vf)
        adjusted: float = adjust_deviation(Vf, raw_disproportionality, extra)

        # Then normalize
        _normalizer: Normalizer = Normalizer(adjusted)

        best: float = 0.0
        worst: float = 0.20

        _normalizer.positive()
        _normalizer.clip(worst, best)
        _normalizer.unitize(worst, best)
        _normalizer.invert()
        _normalizer.rescale()

        rating: int = _normalizer.normalized_num

        return rating


### RATE COMPETITIVENESS ###


def rate_competitiveness(raw_cdf: float) -> int:
    """
    Normalize overall competitiveness - Raw values are in the range [0.0–1.0].
    But the practical max is more like 3/4's, so unitize that range to [0.0–1.0].
    Then scale the values to [0–100].
    """

    _normalizer: Normalizer = Normalizer(raw_cdf)

    worst: float = 0.0
    best: float = 0.75

    _normalizer.clip(worst, best)
    _normalizer.unitize(worst, best)
    _normalizer.rescale()

    rating: int = _normalizer.normalized_num

    return rating


### RATE MINORITY REPRESENTATION ###


def rate_minority_opportunity(od: float, pod: float, cd: float, pcd: float) -> int:
    """
    NOTE - The probable # of opportunity & coalition districts can be *larger* than
      what would be a proportional # based on the statewide percentage, because of
      how minority opportunities are estimated (so that 37% minority shares score
      like 52% share).
    """

    # Score minority opportunity [0–100]
    cd_weight: float = 0.5

    # Cap opportunity & coalition districts
    od_capped: float = min(od, pod)
    cd_capped = min(cd, pcd)

    opportunity_score = round((od_capped / pod) * 100) if (pod > 0) else 0
    coalition_score = round((cd_capped / pcd) * 100) if (pcd > 0) else 0

    rating: int = round(
        min(
            opportunity_score
            + (cd_weight * max(coalition_score - opportunity_score, 0)),
            100,
        )
    )

    return rating


### RATE COMPACTNESS ###


def rate_reock(raw_value: float) -> int:
    _normalizer: Normalizer = Normalizer(raw_value)

    worst: float = REOCK_MIN
    best: float = REOCK_MAX

    _normalizer.clip(worst, best)
    _normalizer.unitize(worst, best)
    _normalizer.rescale()

    return _normalizer.normalized_num


def rate_polsby(raw_value: float) -> int:
    _normalizer: Normalizer = Normalizer(raw_value)

    worst: float = POLSBY_MIN
    best: float = POLSBY_MAX

    _normalizer.clip(worst, best)
    _normalizer.unitize(worst, best)
    _normalizer.rescale()

    return _normalizer.normalized_num


def rate_compactness(reock_rating: int, polsby_rating: int) -> int:
    reock_weight: int = 50
    polsby_weight: int = NORMALIZED_RANGE - reock_weight

    rating: int = round(
        ((reock_rating * reock_weight) + (polsby_rating * polsby_weight))
        / NORMALIZED_RANGE
    )

    return rating


### RATE SPLITTING ###

# Rating county- & district-splitting are inverses of each other.
# Sometimes counties >> districts sometimes counties << districts.

MAX_SPLITTING: float = 1.20  # 90–10 => 95–5 splits
MIN_SPLITTING: float = 1.00  # No splits still vs. 97–03 splits
WORST_MULTIPLIER: float = 1.33  # 1/3 bigger


def best_target(n: float, m: float) -> float:
    """=LAMBDA(n, m, most, least, (((MIN(n, m) - 1) / MAX(n, m)) * most) + ((1 - ((MIN(n, m) - 1) / MAX(n, m))) * least))"""

    more: float = max(n, m)
    less: float = min(n, m)

    w1: float = (less - 1) / more
    w2: float = 1 - w1

    target: float = (w1 * MAX_SPLITTING) + (w2 * MIN_SPLITTING)

    return target


def rate_county_splitting(
    raw_county_splitting: float, n_counties: int, n_districts: int
) -> int:
    _normalizer: Normalizer = Normalizer(raw_county_splitting)

    # The practical ideal raw measurement depends on the # of counties & districts
    best: float = (
        best_target(n_counties, n_districts)
        if (n_counties > n_districts)
        else MAX_SPLITTING
    )
    worst: float = best * WORST_MULTIPLIER

    _normalizer.clip(best, worst)
    _normalizer.unitize(best, worst)
    _normalizer.invert()
    _normalizer.rescale()

    # 09-07-21 - Preserve max value (100) for only when no counties are split
    rating: int = _normalizer.normalized_num
    if (rating == 100) and (raw_county_splitting > 1.0):
        rating = 100 - 1

    return rating


def rate_district_splitting(
    raw_district_splitting: float, n_counties: int, n_districts: int
) -> int:
    _normalizer: Normalizer = Normalizer(raw_district_splitting)

    # The practical ideal raw measurement depends on the # of counties & districts
    best: float = (
        MAX_SPLITTING
        if (n_counties > n_districts)
        else best_target(n_counties, n_districts)
    )
    worst: float = best * WORST_MULTIPLIER

    _normalizer.clip(best, worst)
    _normalizer.unitize(best, worst)
    _normalizer.invert()
    _normalizer.rescale()

    # 09-07-21 - Preserve max value (100) for only when no districts are split
    rating = _normalizer.normalized_num
    if (rating == 100) and (raw_district_splitting > 1.0):
        rating = 100 - 1

    return rating


def rate_splitting(county_rating: int, district_rating: int) -> int:
    county_weight: int = 50
    district_weight: int = NORMALIZED_RANGE - county_weight

    rating = round(
        ((county_rating * county_weight) + (district_rating * district_weight))
        / NORMALIZED_RANGE
    )

    # Preserve max value (100) for only when no districts are split.
    # The max county- or district-splitting rating is 99 when there are splits.
    if (rating == 100) and ((county_rating < 100) or (district_rating < 100)):
        rating = 100 - 1

    return rating


### CONSTANTS ###

AVG_SV_ERROR: float = 0.02
WINNER_BONUS: float = 2.0

REOCK_MIN: float = 0.25
REOCK_MAX: float = 0.50
POLSBY_MIN: float = 0.10
POLSBY_MAX: float = 0.50

### HELPERS ###


def is_antimajoritarian(Vf: float, Sf: float) -> bool:
    bDem = True if ((Vf < (0.5 - AVG_SV_ERROR)) and (Sf > 0.5)) else False
    bRep = True if (((1 - Vf) < (0.5 - AVG_SV_ERROR)) and ((1 - Sf) > 0.5)) else False

    return bDem or bRep


def extra_bonus(Vf: float) -> float:
    over_50_pct: float = (Vf - 0.5) if (Vf > 0.5) else (0.5 - Vf)
    ok_extra: float = over_50_pct * (WINNER_BONUS - 1.0)

    return ok_extra


def adjust_deviation(Vf: float, disproportionality: float, extra: float) -> float:
    """
    Adjust deviation from proportionality to account for a winner's bonus
    * If the bias is in the *same* direction as the statewide vote %, then
      discount the bias by the winner's bonus (extra).
    * But if the bias and statewide vote % go in opposite directions, leave the
      bias unadjusted.
    """
    adjusted: float = disproportionality

    if (Vf > 0.5) and (disproportionality < 0):
        adjusted = min(disproportionality + extra, 0)
    elif (Vf < 0.5) and (disproportionality > 0):
        adjusted = max(disproportionality - extra, 0)

    return adjusted


### END ###
