#!/usr/bin/env python3
#
# EXTRACT THE EXTERIOR COORDINATES OF A POLYGON OR MULTIPOLYGON

from shapely.geometry import Polygon, MultiPolygon


def get_polygon_coordinates(geometry):
    """
    Extract exterior & interior coordinates from a single polygon.

    Parameters
    ----------
    geometry : shapely Polygon
        the geometry to extract coordinates from

    Returns
    -------
    polygons_coords : list
    """

    if isinstance(geometry, MultiPolygon):
        raise ValueError("Geometry must be a shapely Polygon (not MultiPolygon)")

    polygons_coords = []

    x, y = geometry.exterior.xy
    polygons_coords.append(list(zip(x, y)))

    if len(geometry.interiors) > 0:
        for hole in geometry.interiors:
            x, y = hole.xy
            polygons_coords.append(list(zip(x, y)))

    return polygons_coords


# NOTE - This is a slightly edited version of the online code that follows.


def get_polygons_coordinates(geometry):
    """
    Extract exterior coordinates from polygon(s).

    Parameters
    ----------
    geometry : shapely Polygon or MultiPolygon
        the geometry to extract exterior coordinates from

    Returns
    -------
    polygons_coords : list
    """

    # extract the exterior coordinates of the geometry
    polygons_coords = []
    if isinstance(geometry, Polygon):
        x, y = geometry.exterior.xy
        polygons_coords.append(list(zip(x, y)))
    elif isinstance(geometry, MultiPolygon):
        # for polygon in geometry:
        for polygon in list(geometry.geoms):
            x, y = polygon.exterior.xy
            polygons_coords.append(list(zip(x, y)))
    else:
        raise ValueError("Geometry must be a shapely Polygon or MultiPolygon")

    return polygons_coords


# NOTE - From https://www.programcreek.com/python/example/58596/shapely.geometry.MultiPolygon
#
# def get_polygons_coordinates(geometry):
#     """
#     Extract exterior coordinates from polygon(s) to pass to OSM in a query by
#     polygon.

#     Parameters
#     ----------
#     geometry : shapely Polygon or MultiPolygon
#         the geometry to extract exterior coordinates from

#     Returns
#     -------
#     polygon_coord_strs : list
#     """

#     # extract the exterior coordinates of the geometry to pass to the API later
#     polygons_coords = []
#     if isinstance(geometry, Polygon):
#         x, y = geometry.exterior.xy
#         polygons_coords.append(list(zip(x, y)))
#     elif isinstance(geometry, MultiPolygon):
#         for polygon in geometry:
#             x, y = polygon.exterior.xy
#             polygons_coords.append(list(zip(x, y)))
#     else:
#         raise ValueError('Geometry must be a shapely Polygon or MultiPolygon')

#     # convert the exterior coordinates of the polygon(s) to the string format
#     # the API expects
#     polygon_coord_strs = []
#     for coords in polygons_coords:
#         s = ''
#         separator = ' '
#         for coord in list(coords):
#             # round floating point lats and longs to 14 places, so we can hash
#             # and cache strings consistently
#             s = '{}{}{:.14f}{}{:.14f}'.format(s, separator, coord[1], separator, coord[0])
#         polygon_coord_strs.append(s.strip(separator))

#     return polygon_coord_strs

# END


# LIMIT WHAT GETS EXPORTED.

__all__ = ["get_polygon_coordinates", "get_polygons_coordinates"]
