#!/usr/bin/env python3

"""
REPROJECT A SHAPE OR SHAPES' CRS ON THE FLY

Examples:

crs_in = CRS('epsg:4269')     # NAD 83
crs_out = CRS('esri:102003')  # Albers equal-area conic
"""

from functools import partial
import pyproj
from shapely.ops import transform


def reproject_shape(shp, source_crs, dest_crs):
    project = partial(pyproj.transform, source_crs, dest_crs)
    return transform(project, shp)


def reproject_shapes(source_shapes, crs_in, crs_out):
    new_shapes = []
    for item in source_shapes:
        new_shapes.append((item[0], reproject_shape(item[1], crs_in, crs_out)))

    return new_shapes


__all__ = ["reproject_shape", "reproject_shapes"]

### END ###
