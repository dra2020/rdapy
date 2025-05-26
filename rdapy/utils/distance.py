"""
DISTANCE UTILITIES
"""

from typing import Tuple, Dict

import math


def distance_proxy(a: Tuple[float, float], b: Tuple[float, float]) -> float:
    """
    Calculate a proxy for the distance between two points expressed as (lon, lat) tuples.

    No need for sqrt() since we are only *comparing* distances.
    """

    lat_squared: float = (a[1] - b[1]) * (a[1] - b[1])
    lon_squared: float = (a[0] - b[0]) * (a[0] - b[0])

    return lat_squared + lon_squared


def distance(a: Tuple[float, float], b: Tuple[float, float]) -> float:
    """Calculate the distance between two points expressed as (lon, lat) tuples."""

    return math.sqrt((a[1] - b[1]) * (a[1] - b[1]) + (a[0] - b[0]) * (a[0] - b[0]))


def make_precinct_pair(precinct1: str, precinct2: str) -> Tuple[str, str]:
    """Return a pair of precincts in canonical sorted order."""

    return (precinct1, precinct2) if precinct1 < precinct2 else (precinct2, precinct1)


class DistanceLedger:
    """Compute and cache distances between pairs of precincts as needed."""

    def __init__(self):
        self.distances: Dict[Tuple[str, str], float] = dict()

    def distance_between(
        self,
        geoid1: str,
        center1: Tuple[float, float],
        geoid2: str,
        center2: Tuple[float, float],
    ) -> float:
        pair: Tuple[str, str] = make_precinct_pair(geoid1, geoid2)
        if pair in self.distances:
            return self.distances[pair]
        else:
            d: float = distance_proxy(center1, center2)
            self.distances[pair] = d
            return d


### END ###
