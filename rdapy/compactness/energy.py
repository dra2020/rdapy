"""
POPULATION COMPACTNESS (AKA "ENERGY")
"""

from typing import List, Dict, Tuple, Any
from collections import defaultdict


def calc_energy(
    assignments: Dict[str, int], precinct_data: List[Dict[str, Any]], pop_field: str
) -> float:
    """Calculate the 'energy' of a redistricting plan."""

    district_centers: Dict[int, Tuple[float, float]] = _get_centroids(
        assignments, precinct_data, pop_field
    )

    energy: float = 0.0
    for precinct in precinct_data:
        geoid: str = precinct["geoid"]
        if geoid not in assignments:
            continue
        district: int = assignments[geoid]

        pop: int = precinct[pop_field]
        energy += pop * _squared_distance(
            district_centers[district], precinct["center"]
        )

    return energy


### HELPERS ###


def _squared_distance(a: Tuple[float, float], b: Tuple[float, float]) -> float:
    """Calculate the squared distance between two points expressed as (lon, lat) tuples."""

    return (a[1] - b[1]) * (a[1] - b[1]) + (a[0] - b[0]) * (a[0] - b[0])


def _get_centroids(
    assignments: Dict[str, int], precinct_data: List[Dict[str, Any]], pop_field: str
) -> Dict[int, Tuple[float, float]]:
    """Calculate the centroids of the districts in a redistricting plan, expressed as (lon, lat) tuples."""

    wlon_by_district: defaultdict[int, float] = defaultdict(float)
    wlat_by_district: defaultdict[int, float] = defaultdict(float)
    pop_by_district: defaultdict[int, int] = defaultdict(int)

    for precinct in precinct_data:
        geoid: str = precinct["geoid"]
        if geoid not in assignments:
            continue
        district: int = assignments[geoid]

        pop: int = precinct[pop_field]
        pop_by_district[district] += pop
        wlon_by_district[district] += precinct["center"][0] * pop
        wlat_by_district[district] += precinct["center"][1] * pop

    centers: Dict[int, Tuple[float, float]] = dict()
    ndistricts: int = max(s for s in pop_by_district.keys())
    for district in range(1, ndistricts + 1):
        lon: float = wlon_by_district[district] / pop_by_district[district]
        lat: float = wlat_by_district[district] / pop_by_district[district]
        centers[district] = (lon, lat)

    return centers


### END ###
