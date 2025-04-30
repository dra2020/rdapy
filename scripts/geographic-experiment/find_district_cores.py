#!/usr/bin/env python3

"""
EXPERIMENT: FIND DISTRICT CORES
for Jon Eguia & Jeff Barton's geographic (central) advantage metric

For example:

$ scripts/geographic-experiment/find_district_cores.py

"""

from typing import Any, List, Dict, Set

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
precincts_path: str = "~/local/geographic/NC_precinct_partisan-lean.jsonl"
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

# Load the precinct neighborhoods

neighborhoods: Dict[str, Dict[str, Any]] = dict()
with smart_read(neighborhoods_path) as nh_stream:
    for i, line in enumerate(nh_stream):
        parsed_line = json.loads(line)

        geoid: str = parsed_line["geoid"]
        neighborhoods[geoid] = parsed_line.copy()

# Load the precinct partisan leanings

precincts: List[Dict[str, Any]] = list()
with smart_read(precincts_path) as precincts_stream:
    for i, line in enumerate(precincts_stream):
        parsed_line = json.loads(line)
        precincts.append(parsed_line)

### Find prototypical D-packed, R-packed, and competitive district cores ###

seen: Set[str] = set()
D_packed: List[Dict[str, Any]] = list()
precincts.sort(key=lambda x: x["Vf"])

for i, precinct in enumerate(precincts):
    if precinct["Vf"] < 0.55:
        continue

    geoid: str = precinct["geoid"]
    neighborhood: List[str] = get_neighborhood(
        geoid, neighborhoods[geoid], index_to_geoid, debug=False
    )

    if set(neighborhood).isdisjoint(seen):
        D_packed.append({"geoid": geoid, "neighborhood": neighborhood})
        seen.update(neighborhood)

seen: Set[str] = set()
R_packed: List[Dict[str, Any]] = list()
precincts.sort(key=lambda x: x["Vf"], reverse=True)

for i, precinct in enumerate(precincts):
    if precinct["Vf"] > 0.45:
        continue

    geoid: str = precinct["geoid"]
    neighborhood: List[str] = get_neighborhood(
        geoid, neighborhoods[geoid], index_to_geoid, debug=False
    )

    if set(neighborhood).isdisjoint(seen):
        R_packed.append({"geoid": geoid, "neighborhood": neighborhood})
        seen.update(neighborhood)

seen: Set[str] = set()
competitive: List[Dict[str, Any]] = list()
precincts.sort(key=lambda x: abs(1.0 - x["Vf"]))

for i, precinct in enumerate(precincts):
    if precinct["Vf"] < 0.45 or precinct["Vf"] > 0.55:
        continue

    geoid: str = precinct["geoid"]
    neighborhood: List[str] = get_neighborhood(
        geoid, neighborhoods[geoid], index_to_geoid, debug=False
    )

    if set(neighborhood).isdisjoint(seen):
        competitive.append({"geoid": geoid, "neighborhood": neighborhood})
        seen.update(neighborhood)

# See if which sets of distrit cores are disjoint


# def are_disjoint_lists_of_sets(list_of_sets1, list_of_sets2):
#     # Flatten each list of sets into a single set
#     flattened_set1 = set().union(*list_of_sets1)
#     flattened_set2 = set().union(*list_of_sets2)

#     # Check if the flattened sets are disjoint
#     return flattened_set1.isdisjoint(flattened_set2)


D_packed_precincts: List[str] = list()
for i, district in enumerate(D_packed):
    D_packed_precincts.extend(district["neighborhood"])

R_packed_precincts: List[str] = list()
for i, district in enumerate(R_packed):
    R_packed_precincts.extend(district["neighborhood"])

competitive_precincts: List[str] = list()
for i, district in enumerate(R_packed):
    competitive_precincts.extend(district["neighborhood"])

if set(D_packed_precincts).isdisjoint(R_packed_precincts):
    print("D-packed and R-packed precincts are disjoint")
else:
    print("D-packed and R-packed precincts are NOT disjoint!")

if set(D_packed_precincts).isdisjoint(competitive_precincts):
    print("D-packed and competitive precincts are disjoint")
else:
    print("D-packed and competitive precincts are NOT disjoint!")

if set(R_packed_precincts).isdisjoint(competitive_precincts):
    print("R-packed and competitive precincts are disjoint")
else:
    print("R-packed and competitive precincts are NOT disjoint!")

pass  # for debugging

# neighborhood: List[str] = get_neighborhood(
#     geoid, neighborhoods[root_geoid], index_to_geoid, debug=debug
# )
# assert (
#     root_geoid in neighborhood
# ), f"Missing {root_geoid} in its own neighborhood!"


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
