#!/usr/bin/env python3

"""
DRA-SPECIFIC RATINGS ("SCORES")
"""

from .normalize import Normalizer


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

        best = 0.0
        worst = 0.20

        _normalizer.positive()
        _normalizer.clip(worst, best)
        _normalizer.unitize(worst, best)
        _normalizer.invert()
        _normalizer.rescale()

        rating: int = _normalizer.normalized_num

        return rating


"""

# RATE COMPETITIVENESS

# Normalize overall competitiveness - Raw values are in the range [0.0–1.0]. 
# But the practical max is more like 3/4's, so unitize that range to [0.0–1.0].
# Then scale the values to [0–100].
export function rateCompetitiveness(rawCdf: float): float

  _normalizer = Normalizer(rawCdf)

  let worst = C.overallCompetitivenessRange()[C.BEG]
  let best = C.overallCompetitivenessRange()[C.END]

  _normalizer.clip(worst, best)
  _normalizer.unitize(worst, best)
  _normalizer.rescale()

  rating = _normalizer.normalizedNum as number

  return rating



# RATE MINORITY REPRESENTATION

# NOTE - The probable # of opportunity & coalition districts can be *larger* than
#   what would be a proportional # based on the statewide percentage, because of
#   how minority opportunities are estimated (so that 37% minority shares score
#   like 52% share).
export function rateMinorityRepresentation(rawOd: float, pOd: float, rawCd: float, pCd: float): float

  # Score minority opportunity [0–100]
  cDWeight = C.coalitionDistrictWeight()

  # Cap opportunity & coalition districts
  oDCapped = min(rawOd, pOd)
  cdCapped = min(rawCd, pCd)

  opportunityScore = (pOd > 0) ? round((oDCapped / pOd) * 100) : 0
  coalitionScore = (pCd > 0) ? round((cdCapped / pCd) * 100) : 0

  rating = round(min(opportunityScore + cDWeight * max(coalitionScore - opportunityScore, 0), 100))

  return rating



# RATE COMPACTNESS

export function rateReock(rawValue: float): float

  _normalizer = Normalizer(rawValue)

  worst = C.reockRange()[C.BEG]
  best = C.reockRange()[C.END]

  _normalizer.clip(worst, best)
  _normalizer.unitize(worst, best)
  _normalizer.rescale()

  return _normalizer.normalizedNum as number


export function ratePolsby(rawValue: float): float

  _normalizer = Normalizer(rawValue)

  worst = C.polsbyRange()[C.BEG]
  best = C.polsbyRange()[C.END]

  _normalizer.clip(worst, best)
  _normalizer.unitize(worst, best)
  _normalizer.rescale()

  return _normalizer.normalizedNum as number


export function rateCompactness(rS: float, ppS: float): float

  rW = C.reockWeight()
  ppW = C.polsbyWeight()

  rating = round(((rS * rW) + (ppS * ppW)) / (rW + ppW))

  return rating



# RATE SPLITTING

export maxSplitting: float = 1.20     # 90–10 => 95–5 splits
export minSplitting: float = 1.00     # No splits still vs. 97–03 splits
export worstMultiplier: float = 1.33  # 1/3 bigger

# =LAMBDA(n, m, most, least, (((MIN(n, m) - 1) / MAX(n, m)) * most) + ((1 - ((MIN(n, m) - 1) / MAX(n, m))) * least))
export function bestTarget(n: float, m: float): float 

  more: float = max(n, m)
  less: float = min(n, m)

  w1: float = ((less - 1) / more)
  w2: float = 1 - w1

  target: float = (w1 * maxSplitting) + (w2 * minSplitting)

  return target


# Rating county- & district-splitting are inverses of each other.
# Sometimes counties >> districts sometimes counties << districts.

export function rateCountySplitting(rawCountySplitting: float, nCounties: float, nDistricts: float): float

  _normalizer = Normalizer(rawCountySplitting)

  # The practical ideal raw measurement depends on the # of counties & districts
  best = (nCounties > nDistricts) ? bestTarget(nCounties, nDistricts) : maxSplitting
  worst = best * worstMultiplier

  _normalizer.clip(best, worst)
  _normalizer.unitize(best, worst)
  _normalizer.invert()
  _normalizer.rescale()

  # 09-07-21 - Preserve max value (100) for only when no counties are split
  let rating = _normalizer.normalizedNum as number
  if ((rating == 100) and (rawCountySplitting > 1.0)) rating = 100 - 1

  return rating


export function rateDistrictSplitting(rawDistrictSplitting: float, nCounties: float, nDistricts: float): float

  _normalizer = Normalizer(rawDistrictSplitting)

  # The practical ideal raw measurement depends on the # of counties & districts
  best = (nCounties > nDistricts) ? maxSplitting : bestTarget(nCounties, nDistricts)
  worst = best * worstMultiplier

  _normalizer.clip(best, worst)
  _normalizer.unitize(best, worst)
  _normalizer.invert()
  _normalizer.rescale()

  # 09-07-21 - Preserve max value (100) for only when no districts are split
  let rating = _normalizer.normalizedNum as number
  if ((rating == 100) and (rawDistrictSplitting > 1.0)) rating = 100 - 1

  return rating


export function rateSplitting(csS: float, dsS: float): float

  csW = C.countySplittingWeight()
  dsW = C.districtSplittingWeight()

  let rating = round(((csS * csW) + (dsS * dsW)) / (csW + dsW))

  # Preserve max value (100) for only when no districts are split.
  # The max county- or district-splitting rating is 99 when there are splits.
  if ((rating == 100) and ((csS < 100) || (dsS < 100))) rating = 100 - 1

  return rating


# RATE SPLITTING - Legacy routines for original splitting ratings that didn't handle state legislative maps properly

export function rateCountySplittingLegacy(rawCountySplitting: float, nCounties: float, nDistricts: float, bLD: boolean = false): float

  _normalizer = Normalizer(rawCountySplitting)

  # The practical ideal rating depends on the # of counties & districts
  avgBest = countySplitBest(nCounties, nDistricts, bLD)
  avgWorst = countySplitWorst(avgBest, bLD)

  _normalizer.clip(avgBest, avgWorst)
  _normalizer.unitize(avgBest, avgWorst)
  _normalizer.invert()
  _normalizer.rescale()

  # 09-07-21 - Preserve max value (100) for only when no counties are split
  let rating = _normalizer.normalizedNum as number
  if ((rating == 100) and (rawCountySplitting > 1.0)) rating = 100 - 1

  return rating


export function countySplitBest(nCounties: float, nDistricts: float, bLD: boolean = false): float

  districtType = (bLD) ? T.DistrictType.StateLegislative : T.DistrictType.Congressional

  practicalBest = C.countySplittingRange(districtType)[C.BEG]
  nAllowableSplits = min(nDistricts - 1, nCounties)
  threshold = ((nAllowableSplits * practicalBest) + ((nCounties - nAllowableSplits) * 1.0)) / nCounties

  return threshold

export function countySplitWorst(avgBest: float, bLD: boolean = false): float

  districtType = (bLD) ? T.DistrictType.StateLegislative : T.DistrictType.Congressional

  singleBest = C.countySplittingRange(districtType)[C.BEG]
  singleWorst = C.countySplittingRange(districtType)[C.END]

  # The practical ideal score depends on the # of counties & districts
  avgWorst = avgBest * (singleWorst / singleBest)

  return avgWorst


export function rateDistrictSplittingLegacy(rawDistrictSplitting: float, bLD: boolean = false): float

  districtType = (bLD) ? T.DistrictType.StateLegislative : T.DistrictType.Congressional

  _normalizer = Normalizer(rawDistrictSplitting)

  best = C.districtSplittingRange(districtType)[C.BEG]
  worst = C.districtSplittingRange(districtType)[C.END]

  _normalizer.clip(best, worst)
  _normalizer.unitize(best, worst)
  _normalizer.invert()
  _normalizer.rescale()

  # 09-07-21 - Preserve max value (100) for only when no districts are split
  let rating = _normalizer.normalizedNum as number
  if ((rating == 100) and (rawDistrictSplitting > 1.0)) rating = 100 - 1

  return rating


export function rateSplittingLegacy(csS: float, dsS: float): float

  csW = C.countySplittingWeight()
  dsW = C.districtSplittingWeight()

  rating = round(((csS * csW) + (dsS * dsW)) / (csW + dsW))

  return rating


export function adjustSplittingRating(rating: float, rawCountySplitting: float, rawDistrictSplitting: float): float

  # 09-07-21 - Preserve max value (100) for only when no districts are split
  if ((rating == 100) and ((rawCountySplitting > 1.0) || (rawDistrictSplitting > 1.0))) rating = 100 - 1

  return rating

"""

### CONSTANTS ###

AVG_SV_ERROR: float = 0.02
WINNER_BONUS: float = 2.0

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
