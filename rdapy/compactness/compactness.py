#!/usr/bin/env python3

"""
COMPACTNESS
"""

from shapely.geometry import Polygon, MultiPolygon

from .features import *
from .kiwysi import *


def make_compactness_scorecard(shapes: list[Polygon | MultiPolygon]) -> dict:
    """Compute Reock, Polsby-Popper, and KIWYSI compactness for a set of districts and by district."""

    tot_reock: float = 0
    tot_polsby: float = 0
    tot_kiwysi: float = 0

    by_district: list[dict] = list()

    for i, shp in enumerate(shapes):
        print(f"Processing shape {i + 1} of {len(shapes)}...")
        features: list[float] = featureize_shape(shp)

    return dict()


"""
export function makeCompactnessScorecard(shapes: GeoJSON.FeatureCollection, bLog: boolean = false): T.CompactnessScorecard
{
  const pca: T.PCAModel = T.PCAModel.Revised;
  const options: Poly.PolyOptions | undefined = undefined;

  // For calculating averages of by-district values
  let totReock: number = 0;
  let totPolsby: number = 0;
  let totKIWYSI: number = 0;

  // For returning compactness by district to DRA
  // Note, these use the Cartesian (flat earth) measurements
  let byDistrict: T.Compactness[] = [];

  for (let i = 0; i < shapes.features.length; i++)
  {
    const features: T.CompactnessFeatures = featureizePoly(shapes.features[i], options);

    const reockFlat: number = features.reockFlat;
    const polsbyFlat: number = features.polsbyFlat;

    // Note: In order to compute the by-district compactness that DRA needs,
    // you have to normalize Reock & Polsby–Popper here (vs. in DRA proper)
    // like the overall compactness rating.
    const normalizedReock: number = rateReock(reockFlat);
    const normalizedPolsby: number = ratePolsby(polsbyFlat);

    let kiwysiRank: number = scoreFeatureSet(features, pca);
    // Constrain values to the range [1–100]
    kiwysiRank = Math.min(Math.max(kiwysiRank, 1), 100);
    // Raw KIWYSI scores ("ranks") are 1–100 where smaller is better
    // Round & invert into scores where bigger is better [0–100]
    const kiwysiScore: number = 100 - Math.round(kiwysiRank) + 1

    totReock += reockFlat;
    totPolsby += polsbyFlat;
    totKIWYSI += kiwysiScore;

    const measures: T.Compactness = {
      rawReock: reockFlat,
      normalizedReock: normalizedReock,
      rawPolsby: polsbyFlat,
      normalizedPolsby: normalizedPolsby,
      kiwysiScore: kiwysiScore
    };

    byDistrict.push(measures);
  }

  const avgReock: number = totReock / shapes.features.length;
  const avgPolsby: number = totPolsby / shapes.features.length;
  const avgKWIWYSI: number = Math.round(totKIWYSI / shapes.features.length);

  const s: T.CompactnessScorecard = {
    avgReock: avgReock,
    avgPolsby: avgPolsby,
    avgKWIWYSI: avgKWIWYSI,
    byDistrict: byDistrict,  // Legacy format
    details: {},             // None
    // score?: 
  }

  return s;
}
"""


### END ###
