#!/usr/bin/env python3

"""
EXPERIMENT: EVAL THE "NEIGHBORHOOD" FOR EACH PRECINCT
for Jon Eguia & Jeff Barton's geographic (central) advantage metric

For example:

$ scripts/geographic-experiment/eval_neighborhoods.py

"""

from typing import Any, List, Dict, Deque

import json
import array

from rdapy import (
    load_data,
    load_graph,
    smart_read,
)

from rdapy.score import (
    get_dataset,
    DatasetKey,
    get_fields,
)

from rdapy.score.geographic import get_bit, deserialize_bits, nh_partisan_lean

#

# xx: str = "NC"
# plan_type: str = "congress"
# ndistricts: int = 14
# ncounties: int = 100
data_path: str = "testdata/examples/NC_input_data.v4.jsonl"
graph_path: str = "testdata/examples/NC_graph.json"

neighborhoods_path: str = "~/local/geographic/NC_precinct_neighborhoods.jsonl"

verbose: bool = True
debug: bool = False

# granularity: int = ndistricts

#

data_map: Dict[str, Any]
input_data: List[Dict[str, Any]]
data_map, input_data = load_data(data_path)
adjacency_graph: Dict[str, List[str]] = load_graph(graph_path)

census_dataset: DatasetKey = get_dataset(data_map, "census")
total_pop_field: str = get_fields(data_map, "census", census_dataset)["total_pop"]

election_dataset: DatasetKey = get_dataset(data_map, "election")
dem_votes_field: str = get_fields(data_map, "election", election_dataset)["dem_votes"]
rep_votes_field: str = get_fields(data_map, "election", election_dataset)["rep_votes"]

# More fields ...

data: Dict[str, Dict[str, Any]] = dict()

for precinct in input_data:
    geoid: str = precinct["geoid"]
    data[geoid] = precinct.copy()

#

geoid_to_index = {geoid: idx for idx, geoid in enumerate(adjacency_graph.keys())}
index_to_geoid = {idx: geoid for geoid, idx in geoid_to_index.items()}
nprecincts: int = len(geoid_to_index)

with smart_read(neighborhoods_path) as input_stream:
    for i, line in enumerate(input_stream):
        parsed_line = json.loads(line)

        geoid: str = parsed_line["geoid"]

        bits = deserialize_bits(parsed_line["neighborhood"])
        neighborhood: List[str] = [
            index_to_geoid[idx] for idx in range(len(bits)) if get_bit(bits, idx)
        ]

        pop: int = data[geoid][total_pop_field]

        Vf: float
        fractional_seats: float
        whole_seats: float
        neighborhood: List[str]
        Vf, fractional_seats, whole_seats = nh_partisan_lean(
            neighborhood, data, dem_votes_field, rep_votes_field
        )

        if i > 10:
            break

        pass  # for debugging

pass  # for debugging

### END ###
