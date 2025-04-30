#!/usr/bin/env python3

"""
EXPERIMENT: FIND DISTRICT CORES
for Jon Eguia & Jeff Barton's geographic (central) advantage metric

For example:

$ scripts/geographic-experiment/find_district_cores.py

"""

from typing import Any, List, Dict, Deque

import json

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
# data_path: str = "testdata/examples/NC_input_data.v4.jsonl"
graph_path: str = "testdata/examples/NC_graph.json"

neighborhoods_path: str = "~/local/geographic/NC_precinct_neighborhoods.jsonl"
precincts_path: str = "~/local/geographic/NC_precinct_partisan.descending.jsonl"

verbose: bool = True
debug: bool = False

#

# data_map: Dict[str, Any]
# input_data: List[Dict[str, Any]]
# data_map, input_data = load_data(data_path)
adjacency_graph: Dict[str, List[str]] = load_graph(graph_path)

# census_dataset: DatasetKey = get_dataset(data_map, "census")
# total_pop_field: str = get_fields(data_map, "census", census_dataset)["total_pop"]

# election_dataset: DatasetKey = get_dataset(data_map, "election")
# dem_votes_field: str = get_fields(data_map, "election", election_dataset)["dem_votes"]
# rep_votes_field: str = get_fields(data_map, "election", election_dataset)["rep_votes"]

# More fields ...

# data: Dict[str, Dict[str, Any]] = dict()

# state_pop: int = 0
# dem_votes: int = 0
# tot_votes: int = 0

# for precinct in input_data:
#     geoid: str = precinct["geoid"]
#     data[geoid] = precinct.copy()

#     state_pop += precinct[total_pop_field]
#     dem_votes += precinct[dem_votes_field]
#     tot_votes += precinct[dem_votes_field] + precinct[rep_votes_field]

# estimated_vote_pct: float = dem_votes / tot_votes if tot_votes > 0 else 0.0

# print(f"Total population: {state_pop}")
# print(f"Estimated two-party Democratic vote share: {estimated_vote_pct:.4f}")

# Total population: 10439388
# Estimated two-party Democratic vote share: 0.4943

#

geoid_to_index = {geoid: idx for idx, geoid in enumerate(adjacency_graph.keys())}
index_to_geoid = {idx: geoid for geoid, idx in geoid_to_index.items()}
# nprecincts: int = len(geoid_to_index)

# Get the root geoid of the most D-packed neighborhood

root_geoid: str = ""
with smart_read(precincts_path) as precints_stream:
    line = precints_stream.readline()
    parsed_line = json.loads(line)
    root_geoid: str = parsed_line["geoid"]

pass  # for debugging

# Load the precinct neighborhoods

precincts: Dict[str, Dict[str, Any]] = dict()
with smart_read(neighborhoods_path) as input_stream:
    for i, line in enumerate(input_stream):
        parsed_line = json.loads(line)

        geoid: str = parsed_line["geoid"]
        precincts[geoid] = parsed_line["neighborhood"]

# Get the geoids for the precinct's neighborhood

district: List[str] = list()
bits = deserialize_bits(precincts[root_geoid])
neighborhood: List[str] = [
    index_to_geoid[idx] for idx in range(len(bits)) if get_bit(bits, idx)
]

pass  # for debugging

#         pop: int = data[geoid][total_pop_field]

#         Vf: float
#         fractional_seats: float
#         whole_seats: float
#         neighborhood: List[str]
#         Vf, fractional_seats, whole_seats = nh_partisan_lean(
#             neighborhood, data, dem_votes_field, rep_votes_field
#         )

#         record = {
#             "geoid": geoid,
#             "pop": pop,
#             "Vf": Vf,
#             "fractional_seats": fractional_seats,
#             "whole_seats": whole_seats,
#         }
#         print(json.dumps(record))

#         pass  # for debugging

# pass  # for debugging

### END ###
