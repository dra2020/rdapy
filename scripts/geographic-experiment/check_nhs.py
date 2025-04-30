#!/usr/bin/env python3

"""
EXPERIMENT: VERIFY THAT THE "NEIGHBORHOOD" FOR EACH PRECINCT ROUNDTRIPS

For example:

$ scripts/geographic-experiment/check_nhs.py

"""

from typing import Any, List, Dict

import json

from rdapy import (
    load_graph,
    smart_read,
)

from rdapy.score.geographic import (
    index_geoids,
    reverse_index,
    get_bit,
    deserialize_bits,
    get_neighborhood,
)

#

graph_path: str = "testdata/examples/NC_graph.json"
neighborhoods_path: str = "-"
# neighborhoods_path: str = "~/local/geographic/NC_precinct_neighborhoods.jsonl"

verbose: bool = True
debug: bool = True

#

adjacency_graph: Dict[str, List[str]] = load_graph(graph_path)

#

geoid_to_index: Dict[str, int] = index_geoids(list(adjacency_graph.keys()))
index_to_geoid: Dict[int, str] = reverse_index(geoid_to_index)

with smart_read(neighborhoods_path) as input_stream:
    for i, line in enumerate(input_stream):
        parsed_line = json.loads(line)

        geoid: str = parsed_line["geoid"]

        get_neighborhood(geoid, parsed_line, index_to_geoid, debug=debug)

        pass  # for debugging

pass  # for debugging

### END ###
