#!/usr/bin/env python3

"""
EXPERIMENT: GEOGRAPHIC SEATS AND ADVANTAGE
"""

from typing import Any, List, Dict, Deque

from rdapy import (
    load_data,
    load_graph,
    collect_metadata,
    geoids_from_precinct_data,
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
    neighborhood_results,
)

#

xx: str = "NC"
plan_type: str = "congress"
ndistricts: int = 14
ncounties: int = 100
data_path: str = "testdata/examples/NC_input_data.v4.jsonl"
graph_path: str = "testdata/examples/NC_graph.json"
verbose: bool = True
debug: bool = False

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

print(f"State population: {state_pop}")
dl: DistanceLedger = DistanceLedger()

for granularity in [ndistricts, ncounties]:
    print(f"Granularity: {granularity}")
    target_pop: int = state_pop // granularity
    print(f"Target population: {target_pop}")

    # Process each precinct

    tot_seats_whole: float = 0.0
    tot_seats_fractional: float = 0.0
    for i, geoid in enumerate(geoids):
        nh_q: Deque[Neighbor] = make_neighborhood(
            geoid,
            data,
            adjacency_graph,
            ledger=dl,
            target=target_pop,
        )

        pop: int = nh_q[0].pop
        Vf: float
        fractional_seats: float
        whole_seats: float
        Vf, fractional_seats, whole_seats = neighborhood_results(nh_q)

        proportion: float = ndistricts * (pop / state_pop)

        tot_seats_whole += whole_seats * proportion
        tot_seats_fractional += fractional_seats * proportion

        if verbose:
            print(
                f"{i},{geoid},{Vf:.2f},{fractional_seats:.2f},{whole_seats:f},{tot_seats_whole:f},{tot_seats_fractional:f}"
            )

        pass

    print(
        f"Geographic seats: {tot_seats_whole:.2f} | {tot_seats_fractional:f}, for neighorhood granualarity {granularity}"
    )
    break  # Just neighborhood size = district size for now

pass

### END ###
