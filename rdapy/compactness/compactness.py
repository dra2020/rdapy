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

        reock_flat: float = calc_reock(shp, geodesic=False)
        polsby_flat: float = calc_polsby(shp, geodesic=False)

        kiwysi_rank: int = rank_shape(score_features(features))

        tot_reock += reock_flat
        tot_polsby += polsby_flat
        tot_kiwysi += kiwysi_rank

        measures: dict = {
            "rawReock": reock_flat,
            "rawPolsby": polsby_flat,
            "kiwysiRank": kiwysi_rank,
        }
        by_district.append(measures)

    avg_reock: float = tot_reock / len(shapes)
    avg_polsby: float = tot_polsby / len(shapes)
    avg_kiwysi: float = round(tot_kiwysi / len(shapes))

    scorecard: dict = {
        "avgReock": avg_reock,
        "avgPolsby": avg_polsby,
        "avgKIWYSI": avg_kiwysi,
        "byDistrict": by_district,
    }

    return scorecard


### END ###
