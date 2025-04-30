#!/usr/bin/env python3

"""
EXPERIMENT: FIND DISTRICT CORES
for Jon Eguia & Jeff Barton's geographic (central) advantage metric

For example:

$ scripts/geographic-experiment/find_district_cores.py

"""

from typing import Any, List, Dict

import json, csv

from rdapy import (
    load_graph,
    smart_read,
    smart_write,
)

from rdapy.score.geographic import (
    index_geoids,
    reverse_index,
    get_neighborhood,
)

#

graph_path: str = "testdata/examples/NC_graph.json"

neighborhoods_path: str = "~/local/geographic/NC_precinct_neighborhoods.jsonl"
precincts_path: str = "~/local/geographic/NC_precinct_partisan.descending.jsonl"
csv_path: str = "-"

verbose: bool = True
debug: bool = True

#

adjacency_graph: Dict[str, List[str]] = load_graph(graph_path)
geoids: List[str] = list(adjacency_graph.keys())

#

geoid_to_index: Dict[str, int] = index_geoids(list(adjacency_graph.keys()))
index_to_geoid: Dict[int, str] = reverse_index(geoid_to_index)
nprecincts: int = len(geoid_to_index)

# Find the precincts with Vf >= 0.55 neighborhoods, i.e., uncompetitive D-packed

candidates: Dict[str, Dict[str, Any]] = dict()
with smart_read(precincts_path) as precints_stream:
    for i, line in enumerate(precints_stream):
        parsed_line = json.loads(line)

        geoid: str = parsed_line["geoid"]
        Vf: float = parsed_line["Vf"]
        candidates[geoid] = parsed_line.copy()

        if Vf < 0.55:
            break

        pass  # for debugging

# TODO - Find a set of disjoint (independent) district cores

pass  # for debugging

# # Load the precinct neighborhoods

# neighborhoods: Dict[str, Dict[str, Any]] = dict()
# with smart_read(neighborhoods_path) as input_stream:
#     for i, line in enumerate(input_stream):
#         parsed_line = json.loads(line)

#         geoid: str = parsed_line["geoid"]
#         neighborhoods[geoid] = parsed_line.copy()
#         # neighborhoods[geoid] = parsed_line["neighborhood"]

# # Get the geoids for the precinct's neighborhood

# neighborhood: List[str] = get_neighborhood(
#     geoid, neighborhoods[root_geoid], index_to_geoid, debug=debug
# )
# assert root_geoid in neighborhood, f"Missing {root_geoid} in its own neighborhood!"

# # Make a precinct-assignment dictionary

# assignments: List[Dict[str, Any]] = []
# for geoid in geoids:
#     district: int = 1 if geoid in neighborhood else 2  # HACK
#     assignments.append({"GEOID": geoid, "DISTRICT": district})

# with smart_write(csv_path) as assignment_stream:
#     for i, row in enumerate(assignments):
#         if i == 0:
#             cols: List[str] = list(row.keys())
#             writer: csv.DictWriter = csv.DictWriter(assignment_stream, fieldnames=cols)
#             writer.writeheader()

#         writer.writerow(row)


# pass  # for debugging

### END ###
