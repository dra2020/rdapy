#!/usr/bin/env python3

"""
COMPACTNESS
"""

from shapely.geometry import Polygon, MultiPolygon

from .features import *
from .kiwysi import *


def calc_compactness(shapes: list[Polygon | MultiPolygon], kiwysi: bool = True) -> dict:
    """Compute Reock, Polsby-Popper, and KIWYSI compactness for a set of districts and by district.

    NOTE - Most of the runtime cost of these compactness calculations is for the KIWYSI calculation,
           which is why you can disable it.

    """

    tot_reock: float = 0
    tot_polsby: float = 0
    tot_kiwysi: float = 0

    by_district: list[dict] = list()

    for i, shp in enumerate(shapes):
        reock_flat: float = calc_reock(shp, geodesic=False)
        polsby_flat: float = calc_polsby(shp, geodesic=False)

        tot_reock += reock_flat
        tot_polsby += polsby_flat

        measures: dict = {
            "reock": reock_flat,
            "polsby": polsby_flat,
        }

        if kiwysi:
            features: list[float] = featureize_shape(shp)
            kiwysi_rank: float = trim_kiwysi_rank(score_features(features))
            tot_kiwysi += kiwysi_rank
            measures["kiwysiRank"] = kiwysi_rank

        by_district.append(measures)

    avg_reock: float = tot_reock / len(shapes)
    avg_polsby: float = tot_polsby / len(shapes)

    results: dict = {
        "avgReock": avg_reock,
        "avgPolsby": avg_polsby,
        "byDistrict": by_district,
    }

    if kiwysi:
        avg_kiwysi: float = round(tot_kiwysi / len(shapes))
        results["avgKIWYSI"] = avg_kiwysi

    return results


### END ###
