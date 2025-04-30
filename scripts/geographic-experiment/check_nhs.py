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

from rdapy.score.geographic import get_bit, deserialize_bits

#

graph_path: str = "testdata/examples/NC_graph.json"
neighborhoods_path: str = "~/local/geographic/NC_precinct_neighborhoods.jsonl"

verbose: bool = True
debug: bool = False

#

adjacency_graph: Dict[str, List[str]] = load_graph(graph_path)

#

geoid_to_index = {geoid: idx for idx, geoid in enumerate(adjacency_graph.keys())}
index_to_geoid = {idx: geoid for geoid, idx in geoid_to_index.items()}

with smart_read(neighborhoods_path) as input_stream:
    for i, line in enumerate(input_stream):
        parsed_line = json.loads(line)

        geoid: str = parsed_line["geoid"]

        bits = deserialize_bits(parsed_line["neighborhood"])
        neighborhood: List[str] = [
            index_to_geoid[idx] for idx in range(len(bits)) if get_bit(bits, idx)
        ]

        neighbors: List[int] = [geoid_to_index[id] for id in neighborhood]
        nneighbors: int = len(neighbors)
        checksum: int = sum(neighbors)

        assert geoid in neighborhood, f"Missing {geoid} in neighborhood"
        assert (
            nneighbors == parsed_line["nneighbors"]
        ), f"Mismatch in number of neighbors for {geoid}"
        assert checksum == parsed_line["checksum"], f"Checksum mismatch for {geoid}"

        pass  # for debugging

pass  # for debugging

### END ###
