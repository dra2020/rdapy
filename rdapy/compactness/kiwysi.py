#!/usr/bin/env python3

"""
AARON KAUFMAN & GARY KING'S "KIWYSI" COMPACTNESS MODEL

Their six "smart features" plus Schwartzberg:

1 - sym_x (X-SYMMETRY)
2 - sym_y (Y-SYMMETRY)
3 - reock (REOCK)
4 - bbox (BOUNDING-BOX)
5 - polsby (POPOLSBYPOPPERLSBY)
6 - hull (Hull(D))
7 - schwartzberg (SCHWARTZBERG)

TODO

- Refactor report.py
- Invert the 1–100 rank so bigger is better

    // Constrain values to the range [1–100]
    kiwysiRank = Math.min(Math.max(kiwysiRank, 1), 100);
    // Raw KIWYSI scores ("ranks") are 1–100 where smaller is better
    // Round & invert into scores where bigger is better [0–100]
    const kiwysiScore: number = 100 - Math.round(kiwysiRank) + 1

"""

import math
import numpy as np
from shapely.geometry import Polygon
from shapely.ops import transform
from shapely.ops import unary_union  # Supersedes cascaded_union

from .pypoly import *


def score_shape(shp, *, geodesic=True, revised=True):
    features = featureize_shape(shp, geodesic)
    score = score_features(features, revised=revised)

    return score


def score_features(features, *, revised=True):
    """SmartFeatures PCA model (including Schwartzberg)"""

    if revised:
        return _apply_PCA_model_REVISED(features)
    else:
        return _apply_PCA_model_ORIGINAL(features)


def _apply_PCA_model_REVISED(features):
    """The REVISED SmartFeatures PCA model (including Schwartzberg)"""

    model = [
        3.0428861122,  # sym_x
        4.5060390447,  # sym_y
        -22.7768820155,  # reock
        -24.1176096770,  # bbox
        -107.9434473497,  # polsby
        -67.1088897240,  # hull
        -1.2981693414,  # schwartzberg
    ]  # Revised 01/25/21

    intercept = 145.6420811716

    score = np.dot(features, model) + intercept
    normalized_score = score

    return normalized_score


def _apply_PCA_model_ORIGINAL(features):
    """original, INCORRECT SmartFeatures PCA model (including Schwartzberg)"""

    model = [
        0.317566717356693,  # sym_x
        0.32545234315137,  # sym_y
        0.32799567316863,  # reock
        0.411560782484889,  # bbox
        0.412187169816954,  # polsby
        0.420085928286392,  # hull
        0.412187169816954,  # schwartzberg
    ]

    score = np.dot(features, model)
    normalized_score = (score * 11) + 50

    return normalized_score


def featureize_shape(shp, geodesic=True):
    features = []

    features.append(calc_sym_x(shp, geodesic))
    features.append(calc_sym_y(shp, geodesic))
    features.append(calc_reock(shp, geodesic))
    features.append(calc_bbox(shp, geodesic))
    features.append(calc_polsby(shp, geodesic))
    features.append(calc_hull(shp, geodesic))
    features.append(calc_schwartzberg(shp, geodesic))

    return features


def calc_sym_x(shp, geodesic=True):
    """FEATURE 1: X-SYMMETRY

    The same as Y-SYMMETRY except reflect the district D around a horizontal line going through the centroid.
    See below.
    """

    cx, _ = mean_centroid(shp)
    reflected_x_shp = transform(_reflect_x(cx), shp)

    comp_x_shp = shp.union(reflected_x_shp)
    # comp_x_shp = unary_union([shp.buffer(0), reflected_x_shp.buffer(0)])

    # print("X: Unary =", (comp_x_shp2.geom_type == 'Polygon'),
    #       len(comp_x_shp2.interiors))
    # print("X: Union =", (comp_x_shp.geom_type == 'Polygon'),
    #       len(comp_x_shp.interiors))

    shp_area, _, _ = get_polygon_attributes(shp, geodesic)
    comp_area, _, _ = get_polygon_attributes(comp_x_shp, geodesic)

    # orig_area, _, _ = get_polygon_attributes(comp_x_shp2, geodesic)
    # print("orig_area =", orig_area, "x_area =", comp_area)

    # print("dist_area =", shp_area, "x_area =", comp_area, "cx =", cx)

    return comp_area / shp_area


def calc_sym_y(shp, geodesic=True):
    """FEATURE 2: Y-SYMMETRY

    The area of a district overlapping with its reflection around a vertical line going through the centroid,
    divided by the area of the district. Values range [1–2].

    1. Find the centroid
    2. Take the area of the district
    3. Flip the shape about its x or y axis, running through the centroid
    4. Calculate the union of the original shape and its mirror
    5. Take the ratio of the area of that union* and the area of the original shape
    """

    _, cy = mean_centroid(shp)
    reflected_y_shp = transform(_reflect_y(cy), shp)

    comp_y_shp = shp.union(reflected_y_shp)
    # comp_y_shp = unary_union([shp.buffer(0), reflected_y_shp.buffer(0)])

    # print("Y: Unary =", (comp_y_shp2.geom_type == 'Polygon'),
    #       len(comp_y_shp2.interiors))
    # print("Y: Union =", (comp_y_shp.geom_type == 'Polygon'),
    #       len(comp_y_shp.interiors))

    shp_area, _, _ = get_polygon_attributes(shp, geodesic)
    comp_area, _, _ = get_polygon_attributes(comp_y_shp, geodesic)

    # orig_area, _, _ = get_polygon_attributes(comp_y_shp2, geodesic)
    # print("orig_area =", orig_area, "y_area =", comp_area)

    # print("dist_area =", shp_area, "y_area =", comp_area, "cy =", cy)

    return comp_area / shp_area


def _reflect_x(x0):
    return lambda x, y: (2 * x0 - x, y)


def _reflect_y(y0):
    return lambda x, y: (x, 2 * y0 - y)


def mean_centroid(shp):
    """An alternate definition of centroid, following Aaron's R code:

    centroid_x = mean(df$x, na.rm=T)
    centroid_y = mean(df$y, na.rm=T)
    """

    n = 0
    x_tot = 0
    y_tot = 0

    # NOTE - These two methods yield the same result
    if True:
        # NOTE - Shapely points are in (lon, lat) order ...
        pts = [p for l in get_polygons_coordinates(shp) for p in l]

        for p in pts:
            n += 1
            x_tot += p[0]
            y_tot += p[1]
    else:
        if shp.geom_type == "Polygon":
            for p in shp.exterior.coords:
                n += 1
                x_tot += p[0]
                y_tot += p[1]

        else:  # == 'MultiPolygon
            for single_poly in shp.geoms:
                for p in single_poly.exterior.coords:
                    n += 1
                    x_tot += p[0]
                    y_tot += p[1]

    return (x_tot / n, y_tot / n)


def calc_reock(shp, geodesic=True):
    """FEATURE 3: REOCK

    Reock is the primary measure of the dispersion of district shapes, calculated as
    “the area of the district to the area of the minimum spanning circle that can enclose the district.”

    R = A / A(Minimum Bounding Circle)
    R = A / (π * (d / 2)^2)

    R = 4A / πd^2

    This simplifies to:

    R = A / πr^2

    where r is the radius of the minimum bounding circle.
    """

    area, _, diameter = get_polygon_attributes(shp, geodesic)
    radius = diameter / 2

    return area / (math.pi * (radius**2))


def calc_bbox(shp, geodesic=True):
    """FEATURE 4: "BOUNDING-BOX"

    This is shorthand for the ratio of the area of the district to the area of the minimum bounding box of the district.
    """

    # Get the shape's exterior points in a single flat list
    shp_pts = [[p[0], p[1]] for l in get_polygons_coordinates(shp) for p in l]

    # Find the minimum area bounding rectangle (not a simple bounding box)
    bbox_pts = minimum_bounding_rectangle(np.array(shp_pts))
    bbox_shp = Polygon([[p[0], p[1]] for p in bbox_pts])

    # Get the area of the two shapes
    district_area, _, _ = get_polygon_attributes(shp, geodesic)
    bbox_area, _, _ = get_polygon_attributes(bbox_shp, geodesic)

    return district_area / bbox_area


def calc_polsby(shp, geodesic=True):
    """FEATURE 5: POLSBYPOPPER

    Polsby-Popper is the primary measure of the indentation of district shapes,
    calculated as the “the ratio of the area of the district to the area of a circle whose circumference
    is equal to the perimeter of the district.”

    PP = A / A(C)

    where C is that circle. In other words:

    P = 2πRc and A(C) = π(P / 2π)^2

    where P is the perimeter of the district and Rc is the radius of the circle.

    Hence, the measure simplifies to:

    PP = 4π * (A / P^2)
    """

    area, perimeter, _ = get_polygon_attributes(shp, geodesic)

    return (4 * math.pi) * (area / perimeter**2)


def calc_hull(shp, geodesic=True):
    """FEATURE 6: Hull(D)

    Convex Hull is a secondary measure of the dispersion of district shapes,
    calculated as “the ratio of the district area to the area of the minimum convex bounding polygon
    (also known as a convex hull) enclosing the district.”

    CH = A / A(Convex Hull)

    where a convex hull is the minimum perimeter that encloses all points in a shape,
    basically the shortest unstretched rubber band that fits around the shape.
    """

    ch_shp = shp.convex_hull

    shp_area, _, _ = get_polygon_attributes(shp, geodesic)
    hull_area, _, _ = get_polygon_attributes(ch_shp, geodesic)

    return shp_area / hull_area


def calc_schwartzberg(shp, geodesic=True):
    """FEATURE 7: SCHWARTZBERG

    Schwartzberg is a secondary measure of the
    degree of indentation of district shapes, calculated as “the ratio of the
    perimeter of the district to the circumference of a circle whose area is equal
    to the area of the district.”

    https://www.azavea.com/blog/2016/07/11/measuring-district-compactness-postgis/
    defines Schwartzberg as:

    S = 1 / (P / C)

    where P is the perimeter of the district and C is the circumference of the
    circle. The radius of the circle is:

    Rc = SQRT(A / π)

    So, the circumference of the circle is:

    C = 2πRc or C = 2π * SQRT(A / π)

    Hence:

    S = 1 / (P / 2π * SQRT(A / π))

    S = (2π * SQRT(A / π)) / P

    NOTE - Aaron's feature matches the verbal description of P/C (feature_helpers.R).
    """

    area, perimeter, _ = get_polygon_attributes(shp, geodesic)

    # NOTE - Use P/C here, not C/P as Azavea describes.
    return perimeter / ((2 * math.pi) * math.sqrt(area / math.pi))


### FOR TESTING ###


# LIMIT WHAT GETS EXPORTED.

__all__ = [
    "score_shape",
    "score_features",
    "featureize_shape",
    "calc_sym_x",
    "calc_sym_y",
    "calc_reock",
    "calc_bbox",
    "calc_polsby",
    "calc_hull",
    "calc_schwartzberg",
]