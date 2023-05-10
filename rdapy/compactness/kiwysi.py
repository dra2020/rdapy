#!/usr/bin/env python3

"""
AARON KAUFMAN & GARY KING'S "KIWYSI" COMPACTNESS MODEL
"""

import numpy as np
from shapely.geometry import Polygon, MultiPolygon

from .features import *


def score_shape(
    shp: Polygon | MultiPolygon, *, geodesic: bool = True, revised: bool = True
) -> float:
    """Feature-ize a shape and then score it [1-100], smaller is better."""

    features: list[float] = featureize_shape(shp, geodesic)
    score = score_features(features, revised=revised)

    return score


def rank_shape(raw_rank: float) -> float:
    """Constrain values to the range [1–100].

    Smaller is better.
    """

    return min(max(raw_rank, 1.0), 100.0)


def rate_shape(rank: int) -> int:
    """Inverted a [1–100] rank to [0–100] rating where bigger is better."""

    return 100 - rank + 1


def featureize_shape(shp: Polygon | MultiPolygon, geodesic: bool = True) -> list[float]:
    features: list[float] = []

    features.append(calc_sym_x(shp, geodesic))
    features.append(calc_sym_y(shp, geodesic))
    features.append(calc_reock(shp, geodesic))
    features.append(calc_bbox(shp, geodesic))
    features.append(calc_polsby(shp, geodesic))
    features.append(calc_hull(shp, geodesic))
    features.append(calc_schwartzberg(shp, geodesic))

    return features


### PCA MODEL ###


def score_features(features: list[float], *, revised: bool = True) -> float:
    """SmartFeatures PCA model (including Schwartzberg)"""

    if revised:
        return _apply_PCA_model_REVISED(features)
    else:
        return _apply_PCA_model_ORIGINAL(features)


def _apply_PCA_model_REVISED(features: list[float]) -> float:
    """The revised (CORRECT) SmartFeatures PCA model (including Schwartzberg)"""

    model: list[float] = [
        3.0428861122,  # sym_x
        4.5060390447,  # sym_y
        -22.7768820155,  # reock
        -24.1176096770,  # bbox
        -107.9434473497,  # polsby
        -67.1088897240,  # hull
        -1.2981693414,  # schwartzberg
    ]  # Revised 01/25/21

    intercept: float = 145.6420811716

    score: float = np.dot(features, model) + intercept
    normalized_score: float = score

    return normalized_score


def _apply_PCA_model_ORIGINAL(features: list[float]) -> float:
    """The original (INCORRECT) SmartFeatures PCA model (including Schwartzberg)

    For *testing* purposes only.
    """

    model: list[float] = [
        0.317566717356693,  # sym_x
        0.32545234315137,  # sym_y
        0.32799567316863,  # reock
        0.411560782484889,  # bbox
        0.412187169816954,  # polsby
        0.420085928286392,  # hull
        0.412187169816954,  # schwartzberg
    ]

    score: float = np.dot(features, model)
    normalized_score: float = (score * 11) + 50

    return normalized_score


__all__ = [
    "score_shape",
    "featureize_shape",
    "score_features",
    "rank_shape",
    "rate_shape",
]

### END ###
