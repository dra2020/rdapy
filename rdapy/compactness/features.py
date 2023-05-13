#!/usr/bin/env python3

"""
The 6 "smart" features from Kaufman & King's "know it when you see it" (KIWYSI)
compactness model plus Schwartzberg:

1 - sym_x (X-SYMMETRY)
2 - sym_y (Y-SYMMETRY)
3 - reock (REOCK)
4 - bbox (BOUNDING-BOX)
5 - polsby (POLSBYPOPPER)
6 - hull (Hull(D))
7 - schwartzberg (SCHWARTZBERG)
"""

import math
import numpy as np
from shapely.geometry import Polygon, MultiPolygon
from shapely.ops import transform
from shapely.ops import unary_union  # Supersedes cascaded_union

from typing import Any, Callable
from nptyping import NDArray

from .pypoly import *


def calc_sym_x(shp: Polygon | MultiPolygon, geodesic: bool = True) -> float:
    """FEATURE 1: X-SYMMETRY

    The same as Y-SYMMETRY except reflect the district D around a horizontal line going through the centroid.
    See below.
    """

    _: Any
    cx: float

    cx, _ = _mean_centroid(shp)
    reflected_x_shp: Polygon | MultiPolygon = transform(_reflect_x(cx), shp)

    comp_x_shp: Polygon | MultiPolygon = shp.union(reflected_x_shp)

    shp_area: float
    comp_area: float

    shp_area, _, _ = get_polygon_attributes(shp, geodesic)
    comp_area, _, _ = get_polygon_attributes(comp_x_shp, geodesic)

    return comp_area / shp_area


def calc_sym_y(shp: Polygon | MultiPolygon, geodesic: bool = True) -> float:
    """FEATURE 2: Y-SYMMETRY

    The area of a district overlapping with its reflection around a vertical line going through the centroid,
    divided by the area of the district. Values range [1–2].

    1. Find the centroid
    2. Take the area of the district
    3. Flip the shape about its x or y axis, running through the centroid
    4. Calculate the union of the original shape and its mirror
    5. Take the ratio of the area of that union* and the area of the original shape
    """

    _: Any
    cy: float

    _, cy = _mean_centroid(shp)
    reflected_y_shp: Polygon | MultiPolygon = transform(_reflect_y(cy), shp)

    comp_y_shp: Polygon | MultiPolygon = shp.union(reflected_y_shp)

    shp_area: float
    comp_area: float

    shp_area, _, _ = get_polygon_attributes(shp, geodesic)
    comp_area, _, _ = get_polygon_attributes(comp_y_shp, geodesic)

    return comp_area / shp_area


def _reflect_x(x0: float) -> Callable[..., tuple[float, float]]:
    return lambda x, y: (2 * x0 - x, y)


def _reflect_y(y0: float) -> Callable[..., tuple[float, float]]:
    return lambda x, y: (x, 2 * y0 - y)


def _mean_centroid(shp: Polygon | MultiPolygon) -> tuple[float, float]:
    """An alternate definition of centroid, following Aaron's R code:

    centroid_x = mean(df$x, na.rm=T)
    centroid_y = mean(df$y, na.rm=T)
    """

    n: int = 0
    x_tot: float = 0
    y_tot: float = 0

    # These two methods yield the same result
    # 1 - NOTE: Shapely points are in (lon, lat) order ...
    pts: list = [p for l in get_polygons_coordinates(shp) for p in l]

    for p in pts:
        n += 1
        x_tot += p[0]
        y_tot += p[1]

    # 2
    # if shp.geom_type == "Polygon":
    #     for p in shp.exterior.coords:
    #         n += 1
    #         x_tot += p[0]
    #         y_tot += p[1]

    # else:  # == 'MultiPolygon
    #     for single_poly in shp.geoms:
    #         for p in single_poly.exterior.coords:
    #             n += 1
    #             x_tot += p[0]
    #             y_tot += p[1]

    return (x_tot / n, y_tot / n)


def calc_reock(shp: Polygon | MultiPolygon, geodesic: bool = True) -> float:
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

    area: float
    diameter: float
    radius: float

    area, _, diameter = get_polygon_attributes(shp, geodesic)
    radius = diameter / 2

    return area / (math.pi * (radius**2))


def calc_bbox(shp: Polygon | MultiPolygon, geodesic: bool = True) -> float:
    """FEATURE 4: "BOUNDING-BOX"

    This is shorthand for the ratio of the area of the district to the area of the minimum bounding box of the district.
    """

    # Get the shape's exterior points in a single flat list
    shp_pts: list = [[p[0], p[1]] for l in get_polygons_coordinates(shp) for p in l]

    # Find the minimum area bounding rectangle (not a simple bounding box)
    bbox_pts: np.ndarray[Any, np.dtype[np.float64]] = minimum_bounding_rectangle(
        np.array(shp_pts)
    )
    bbox_shp: Polygon = Polygon([[p[0], p[1]] for p in bbox_pts])

    # Get the area of the two shapes

    district_area: float
    bbox_area: float

    district_area, _, _ = get_polygon_attributes(shp, geodesic)
    bbox_area, _, _ = get_polygon_attributes(bbox_shp, geodesic)

    return district_area / bbox_area


def calc_polsby(shp: Polygon | MultiPolygon, geodesic: bool = True) -> float:
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

    _: Any
    area: float
    perimeter: float

    area, perimeter, _ = get_polygon_attributes(shp, geodesic)

    return (4 * math.pi) * (area / perimeter**2)


def calc_hull(shp: Polygon | MultiPolygon, geodesic: bool = True) -> float:
    """FEATURE 6: Hull(D)

    Convex Hull is a secondary measure of the dispersion of district shapes,
    calculated as “the ratio of the district area to the area of the minimum convex bounding polygon
    (also known as a convex hull) enclosing the district.”

    CH = A / A(Convex Hull)

    where a convex hull is the minimum perimeter that encloses all points in a shape,
    basically the shortest unstretched rubber band that fits around the shape.
    """

    ch_shp: Polygon | MultiPolygon = shp.convex_hull

    _: Any
    shp_area: float
    hull_area: float

    shp_area, _, _ = get_polygon_attributes(shp, geodesic)
    hull_area, _, _ = get_polygon_attributes(ch_shp, geodesic)

    return shp_area / hull_area


def calc_schwartzberg(shp: Polygon | MultiPolygon, geodesic: bool = True) -> float:
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

    _: Any
    area: float
    perimeter: float

    area, perimeter, _ = get_polygon_attributes(shp, geodesic)

    # NOTE - Use P/C here, not C/P as Azavea describes.
    return perimeter / ((2 * math.pi) * math.sqrt(area / math.pi))


### END ###
