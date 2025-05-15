"""
INPUT DATA
"""

from typing import Any, Dict, Generator, List, Tuple, TextIO, Set

import json

from .constants import COUNTIES_BY_STATE, DISTRICTS_BY_STATE, OUT_OF_STATE
from .types import ParseGeoID
from .ensemble_io import smart_read, read_record


def load_data(data_path) -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Load precinct data from a file with JSON lines.

    Args:
        data_path: Path to the data file with JSON lines

    Returns:
        list: List of precinct data dictionaries
    """
    with open(data_path, "r") as f:
        records = [json.loads(line) for line in f]

    data_map: Dict[str, Any] = dict()
    input_data: List[Dict[str, Any]] = list()
    for record in records:
        if "_tag_" not in record:
            continue
        if record["_tag_"] == "metadata":
            data_map = record["properties"]
        elif record["_tag_"] == "precinct":
            input_data.append(record["data"])

    return data_map, input_data


def load_graph(graph_path) -> Dict[str, List[str]]:
    """
    Load and parse a graph from a JSON file.

    Args:
        graph_path: Path to the graph JSON file

    Returns:
        dict: Dictionary mapping node IDs to lists of connected node IDs
    """
    with open(graph_path, "r") as f:
        graph_data = json.load(f)
    return {key: list(value) for key, value in graph_data.items()}


def extract_counties(geoids: List[str]) -> List[str]:
    """Extract the counties from a list of precinct GEOIDs."""

    counties: Set[str] = set()
    for geoid in geoids:
        county: str = ParseGeoID(geoid).county[2:]
        counties.add(county)

    return list(counties)


def collect_metadata(xx: str, plan_type: str, geoids: List[str]) -> Dict[str, Any]:
    """Load scoring-specific metadata for a state."""

    ### INFER COUNTY FIPS CODES ###

    counties: List[str] = extract_counties(geoids)

    ### GATHER METADATA ###

    C: int = COUNTIES_BY_STATE[xx]
    D: int = DISTRICTS_BY_STATE[xx][plan_type]

    county_to_index: Dict[str, int] = {county: i for i, county in enumerate(counties)}

    district_to_index: Dict[int, int] = {
        district: i for i, district in enumerate(range(1, D + 1))
    }

    metadata: Dict[str, Any] = dict()
    metadata["C"] = C
    metadata["D"] = D
    metadata["county_to_index"] = county_to_index
    metadata["district_to_index"] = district_to_index

    return metadata


def sorted_geoids(
    precinct_data: List[Dict[str, Any]], *, geoid: str = "geoid"
) -> List[str]:
    """Return a list of sorted GEOIDs from input data."""

    geoids: List[str] = [precinct[geoid] for precinct in precinct_data]
    if OUT_OF_STATE in geoids:
        geoids.remove(OUT_OF_STATE)
    geoids.sort()

    return geoids


### END ###
