#!/usr/bin/env python3

"""
POLYGON ATTRIBUTES: AREA, PERIMETER, DIAMETER

- Either do flat / projected calculations, using whatever projection is
  associated with the shape -- it should be in meters, e.g., Albers equal-area
  conic 
- Or do geodesic calculations that take into account the curvative of
  the earth. Handle both MultiPolygons and Polygons.
"""

from geographiclib.geodesic import Geodesic

from .smallestenclosingcircle import make_circle
from .polygoncoordinates import get_polygon_coordinates, get_polygons_coordinates


def get_polygon_attributes(shp, geodesic=True):
    if geodesic:
        area, perimeter, diameter = _get_geodesic_attributes(shp)

        return area, perimeter, diameter
    else:
        area, perimeter, diameter = _get_projected_attributes(shp)

        return area, perimeter, diameter


def _get_projected_attributes(shp):
    """Units are whatever the units of the project are!"""

    # 10/25/23 - Added this guard
    if shp.geom_type not in ["Polygon", "MultiPolygon"]:
        return 0, 0, 0

    area = shp.area
    perimeter = shp.length

    ch = shp.convex_hull
    # 10/25/23 - Added this guard
    if ch.geom_type not in ["Polygon", "MultiPolygon"]:
        return 0, 0, 0
    pts = ch.exterior.coords
    _, _, r = make_circle(pts)
    diameter = 2 * r

    return area, perimeter, diameter


def _get_geodesic_attributes(shp):
    if shp.geom_type == "Polygon":
        area, perimeter, diameter = _get_geodesic_attributes_poly(shp)

        return abs(area), abs(perimeter), abs(diameter)

    else:  # == 'MultiPolygon
        area, perimeter, diameter = _get_geodesic_attributes_multipoly(shp)

        return abs(area), abs(perimeter), abs(diameter)


def _get_geodesic_attributes_poly(shp):
    """
    If a Polygon has no interiors (holes), just compute the area of it.
    If it has interiors though, subtract the area of each hole.
    """

    # 10/25/23 - Added this guard
    if shp.geom_type not in ["Polygon", "MultiPolygon"]:
        return 0, 0, 0

    # NOTE - Shapely points are in (lon, lat) order ...
    list_pts = get_polygon_coordinates(shp)

    # Calculate the geodesic area and perimeter of the polygon exterior

    pts = list_pts[0]  # The exterior coordinates
    p = _create_geopoly_from_pts(pts)

    _, perimeter, area = p.Compute()

    # Subtract the area of any interior holes
    if len(list_pts) > 1:
        holes = list_pts[1:]
        for pts in holes:
            p = _create_geopoly_from_pts(pts)
            _, _, area_of_hole = p.Compute()
            area += area_of_hole

    area /= 1000000  # Convert to km^2
    perimeter /= 1000  # Convert to km

    # Calculate the geodesic diameter
    ch = shp.convex_hull
    # 10/25/23 - Added this guard
    if ch.geom_type not in ["Polygon", "MultiPolygon"]:
        return 0, 0, 0
    pts = ch.exterior.coords
    lon, lat, r = make_circle(pts)

    lon1 = lon - r
    lat1 = lat
    lon2 = lon + r
    lat2 = lat

    geo_dict1 = Geodesic.WGS84.Inverse(lat1, lon1, lat2, lon2)  # type: ignore
    lon_s12 = geo_dict1["s12"]

    lon3 = lon
    lat3 = lat - r
    lon4 = lon
    lat4 = lat + r

    geo_dict2 = Geodesic.WGS84.Inverse(lat3, lon3, lat4, lon4)  # type: ignore
    lat_s12 = geo_dict2["s12"]

    diameter = max(lon_s12, lat_s12)
    diameter /= 1000  # Convert to km

    return abs(area), abs(perimeter), abs(diameter)


def _create_geopoly_from_pts(pts):
    p = Geodesic.WGS84.Polygon()  # type: ignore

    for pt in pts:
        # NOTE - ... but Geodesic needs them in (lat, lon) order!
        p.AddPoint(pt[1], pt[0])

    return p


def _get_geodesic_attributes_multipoly(shp):
    area_mp, perimeter_mp, diameter_mp = 0, 0, 0

    for p in shp.geoms:
        area, perimeter, diameter = _get_geodesic_attributes_poly(p)

        area_mp += area
        perimeter_mp += perimeter

    ch = shp.convex_hull
    _, _, diameter_mp = _get_geodesic_attributes_poly(ch)

    return abs(area_mp), abs(perimeter_mp), abs(diameter_mp)


__all__ = ["get_polygon_attributes"]

### END ###
