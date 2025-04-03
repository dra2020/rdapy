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


# TODO - Rationalize these


def input_data_precincts(
    data_stream: TextIO,
) -> Generator[Tuple[str, Dict[str, Any]], None, None]:
    """Return precinct data one record at a time (including a metadata record) from an input data JSONL file."""

    for i, line in enumerate(data_stream):
        try:
            in_record: Dict[str, Any] = read_record(line)
            if "_tag_" not in in_record:
                continue

            assert in_record["_tag_"] == "metadata" or in_record["_tag_"] == "precinct"

            tag: str = in_record["_tag_"]
            data: Dict[str, Any] = dict()
            if tag == "metadata":
                data = in_record["properties"]
            else:
                data = in_record["data"]

            yield (tag, data)

        except Exception as e:
            raise Exception(f"Reading input data {i}: {e}")


def unpack_input_data(
    input_data_path: str,
) -> Tuple[Dict[str, Any], List[Dict[str, Any]], Dict[str, List[str]]]:
    """Read an input data file and return the metadata, the precinct data, and the adjacency graph."""

    input_metadata: Dict[str, Any] = dict()
    input_data: List[Dict[str, Any]] = list()
    adjacency_graph: Dict[str, List[str]] = dict()

    with smart_read(input_data_path) as data_stream:
        for tag, data in input_data_precincts(data_stream):
            if tag == "metadata":
                input_metadata = data
            else:
                if data["geoid"] != OUT_OF_STATE:
                    input_data.append(data)
                adjacency_graph[data["geoid"]] = data["neighbors"]

    return input_metadata, input_data, adjacency_graph


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


def geoids_from_precinct_data(
    precinct_data: List[Dict[str, Any]], *, geoid: str = "geoid"
) -> List[str]:
    """Return a list of GEOIDs from data indexed (keyed) by geoid."""

    geoids: List[str] = [precinct[geoid] for precinct in precinct_data]

    return geoids


### END ###
