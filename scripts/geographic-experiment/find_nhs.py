#!/usr/bin/env python3

"""
EXPERIMENT: FIND THE "NEIGHBORHOOD" FOR EACH PRECINCT
for Jon Eguia & Jeff Barton's geographic (central) advantage metric

It's an expensive operation, so persist the results to disk for subsequent (re)use.

For example:

$ scripts/geographic-experiment/find_nhs.py

"""

from typing import Any, List, Dict, Deque

import json

from rdapy import (
    load_data,
    load_graph,
)

from rdapy.score import (
    get_dataset,
    DatasetKey,
    get_fields,
)

from rdapy.score.geographic import (
    DistanceLedger,
    Neighbor,
    make_neighborhood,
    index_geoids,
    init_bit_array,
    set_bit,
    serialize_bits,
    deserialize_bits,
)

#

xx: str = "NC"
plan_type: str = "congress"
ndistricts: int = 14
ncounties: int = 100
data_path: str = "testdata/examples/NC_input_data.v4.jsonl"
graph_path: str = "testdata/examples/NC_graph.json"

slack: float = 0.05

verbose: bool = True
debug: bool = True

granularity: int = ndistricts

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

# Setup data structures for the algorithm

geoids: List[str] = list()
state_pop: int = 0
data: Dict[str, Dict[str, Any]] = dict()

for precinct in input_data:
    geoid: str = precinct["geoid"]
    geoids.append(geoid)
    data[geoid] = dict()

    pop: int = precinct[total_pop_field]
    state_pop += pop
    data[geoid]["pop"] = pop
    data[geoid]["center"] = precinct["center"]
    data[geoid]["dem_votes"] = precinct[dem_votes_field]
    data[geoid]["tot_votes"] = precinct[dem_votes_field] + precinct[rep_votes_field]

target_pop: int = state_pop // granularity

geoid_to_index: Dict[str, int] = index_geoids(list(adjacency_graph.keys()))
nprecincts: int = len(geoid_to_index)

# Process each precinct

dl: DistanceLedger = DistanceLedger()

for i, geoid in enumerate(geoids):
    nh_q: Deque[Neighbor] = make_neighborhood(
        geoid,
        data,
        adjacency_graph,
        ledger=dl,
        target=target_pop,
        slack=slack,
        debug=debug,
    )

    indexed_nh: List[int] = [geoid_to_index[id] for id in [node.geoid for node in nh_q]]
    nneighbors: int = len(indexed_nh)
    checksum: int = sum(indexed_nh)
    assert geoid_to_index[geoid] in indexed_nh, f"Missing {geoid} in neighborhood"

    bits = init_bit_array(nprecincts)
    for offset in indexed_nh:
        set_bit(bits, offset, True)

    serialized_bits = serialize_bits(bits, nprecincts)
    if debug:
        deserialized_bits = deserialize_bits(serialized_bits)
        assert deserialized_bits == bits, f"Failed to roundtrip bits for {geoid}"

    record = {
        "geoid": geoid,
        "size": nneighbors,
        "checksum": checksum,
        "neighborhood": serialized_bits,
    }
    print(json.dumps(record))

    pass  # for debugging

pass  # for debugging

### END ###
