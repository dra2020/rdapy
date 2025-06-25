#!/usr/bin/env python3

"""
PROFILING COMPACTNESS METRICS

Virtually all of the time is spent in the featureize_shape() function,
which is required for KIWYSI compactness.

To run:

$ samples/compactness_profile.py

"""

import time
from functools import wraps
from typing import Any, Callable

from shapely.geometry import (
    Polygon,
    MultiPolygon,
)

from rdapy import *


def time_function(func) -> Callable[..., Any]:
    """A decorator to report execution run time for freestanding functions"""

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        tic: float = time.perf_counter()

        result: Any = func(*args, **kwargs)

        toc: float = time.perf_counter()
        print(f"{func.__name__} = {toc - tic: 0.1f} seconds")

        return result

    return wrapper


@time_function
def timed_compactness(shapes: list, kiwysi: bool = True) -> dict:
    return calc_compactness_metrics(shapes, kiwysi)


@time_function
def time_featureize_shape(
    shp: Polygon | MultiPolygon, geodesic: bool = True
) -> list[float]:
    features: list[float] = []

    return featureize_shape(shp)


@time_function
def time_score_features(features: list[float], *, revised: bool = True) -> float:
    return score_features(features)


@time_function
def time_calc_sym_x(shp: Polygon | MultiPolygon, geodesic: bool = True) -> float:
    return calc_sym_x(shp)


@time_function
def time_calc_sym_y(shp: Polygon | MultiPolygon, geodesic: bool = True) -> float:
    return calc_sym_y(shp)


@time_function
def time_calc_reock(shp: Polygon | MultiPolygon, geodesic: bool = True) -> float:
    return calc_reock(shp, geodesic)


@time_function
def time_calc_bbox(shp: Polygon | MultiPolygon, geodesic: bool = True) -> float:
    return calc_bbox(shp, geodesic)


@time_function
def time_calc_polsby(shp: Polygon | MultiPolygon, geodesic: bool = True) -> float:
    return calc_polsby(shp, geodesic)


@time_function
def time_calc_hull(shp: Polygon | MultiPolygon, geodesic: bool = True) -> float:
    return calc_hull(shp, geodesic)


@time_function
def time_calc_schwartzberg(shp: Polygon | MultiPolygon, geodesic: bool = True) -> float:
    return calc_schwartzberg(shp, geodesic)


# Load data

sample_path: str = f"testdata/compactness/NC-116th-Congressional"
shapes, _ = load_shapes(sample_path, id="id")
shapes = [item[1] for item in shapes]  # discard the id

# Overall compactness time

results: dict = timed_compactness(shapes, kiwysi=False)
# timed_compactness(shapes)

# # Compactness by district time & function time
# for i, shp in enumerate(shapes):
#     print(f"District {i+1}:")

#     features: list[float] = time_featureize_shape(shp)
#     # time_calc_sym_x(shp)
#     # time_calc_sym_y(shp)
#     # time_calc_reock(shp)
#     # time_calc_bbox(shp)
#     # time_calc_polsby(shp)
#     # time_calc_hull(shp)
#     # time_calc_schwartzberg(shp)

#     # reock_flat: float = time_calc_reock(shp, geodesic=False)
#     # polsby_flat: float = time_calc_polsby(shp, geodesic=False)

#     # kiwysi_rank: float = trim_kiwysi_rank(time_score_features(features))

# Print the results

print(f"Partisan compactness analytics:")
print(results)

### END ###
