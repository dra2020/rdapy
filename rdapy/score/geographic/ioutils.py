"""
I/O UTILITIES
"""

from typing import List, Dict, Any

import json

from ..utils import smart_read


def load_neighborhoods(nh_path: str) -> Dict[str, Dict[str, Any]]:
    """Load neighborhoods from a JSONL file."""

    neighborhoods: Dict[str, Dict[str, Any]] = dict()
    with smart_read(nh_path) as nh_stream:
        for i, line in enumerate(nh_stream):
            parsed_line = json.loads(line)

            geoid: str = parsed_line["geoid"]
            neighborhoods[geoid] = parsed_line.copy()

    return neighborhoods


def index_data(input_data: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    """Index precinct data by geoid."""

    data: Dict[str, Dict[str, Any]] = {
        precinct["geoid"]: precinct for precinct in input_data
    }

    return data


### END ###
