#!/usr/bin/env python3

"""
GENERATE MODS FOR TO FULLY CONNECT AN ADJACENCY GRAPH

$ scripts/utility/generate_mods.py \
--graph ~/local/dra-to-publish/HI_2020_graph.json \
--data ~/local/temp-data/HI_input_data.v4.jsonl \
--mods temp/DEBUG_graph_mods.json

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import Any, List, Dict, Tuple, Set, NamedTuple

import sys
from itertools import combinations

import networkx as nx

from rdapy import (
    load_graph,
    OUT_OF_STATE,
    load_data,
    is_connected,
    connected_subsets,
)

from rdapy.score import index_data, DatasetKey, get_dataset, get_fields, DistanceLedger


class Island(NamedTuple):
    id: int
    population: int
    precincts: int
    coastal: List[str]
    inland: List[str]


class Connection(NamedTuple):
    from_geoid: str
    to_geoid: str
    distance: float


# class Edge(NamedTuple):
#     from_node: int
#     to_node: int
#     link: Connection


def main() -> None:
    """Generate 'mods' (additional connections) to fully connect an adjacency graph."""

    args: Namespace = parse_args()

    #

    data_map: Dict[str, Any]
    input_data: List[Dict[str, Any]]
    data_map, input_data = load_data(args.data)
    adjacency_graph: Dict[str, List[str]] = load_graph(args.graph)

    #

    data_by_geoid: Dict[str, Dict[str, Any]] = index_data(input_data)
    census_dataset: DatasetKey = get_dataset(data_map, "census")
    total_pop_field: str = get_fields(data_map, "census", census_dataset)["total_pop"]

    geoids: List[str] = list(adjacency_graph.keys())
    geoids.remove(OUT_OF_STATE)
    geoids.sort()

    if is_connected(geoids, adjacency_graph):
        print(f"Graph is fully connected.")
        sys.exit(0)

    print(f"WARNING: Graph is NOT fully connected!")

    # Find all the connected subsets of precincts

    subsets: List[Set[Any]] = connected_subsets(geoids, adjacency_graph)

    # Separate precincts into coastal and inland areas

    islands: List[Island] = list()

    for i, subset in enumerate(subsets):
        id: int = i
        pop: int = 0
        precincts: int = 0
        coastal: List[str] = list()
        inland: List[str] = list()

        for geoid in subset:
            precincts += 1
            pop += data_by_geoid[geoid][total_pop_field]

            is_coastal: bool = True if geoid in adjacency_graph[OUT_OF_STATE] else False
            if is_coastal:
                coastal.append(geoid)
            else:
                inland.append(geoid)

        islands.append(Island(id, pop, precincts, coastal, inland))

    # Find the distance between each pair of islands

    dl: DistanceLedger = DistanceLedger()

    n_islands: int = len(islands)
    island_pairs: List[Tuple[int, int]] = list(combinations(range(n_islands), 2))
    possible_edges: Dict[Tuple[int, int], List[Connection]] = dict()
    shortest_edges: Dict[Tuple[int, int], Connection] = dict()

    for pair in island_pairs:
        i1: int = pair[0]
        i2: int = pair[1]

        possible_edges[pair] = list()

        coast1: List[str] = islands[i1].coastal
        coast2: List[str] = islands[i2].coastal

        for c1 in coast1:
            for c2 in coast2:
                distance: float = dl.distance_between(
                    c1, data_by_geoid[c1]["center"], c2, data_by_geoid[c2]["center"]
                )
                edge: Connection = Connection(c1, c2, distance)
                possible_edges[pair].append(edge)
        possible_edges[pair].sort(key=lambda x: x.distance)
        shortest_edges[pair] = possible_edges[pair][0]

    # Find the minimum spanning tree

    G = nx.Graph()
    for i in range(n_islands):
        G.add_node(i)
    for pair in island_pairs:
        i1: int = pair[0]
        i2: int = pair[1]
        p1: str = shortest_edges[pair].from_geoid
        p2: str = shortest_edges[pair].to_geoid
        distance: float = shortest_edges[pair].distance
        G.add_edge(i1, i2, weight=distance, geoid1=p1, geoid2=p2)
    T = nx.minimum_spanning_tree(G)
    connections = sorted(T.edges(data=True))

    pass


### HELPERS ###


def parse_args() -> Namespace:
    """Parse command line arguments."""

    parser: ArgumentParser = argparse.ArgumentParser(
        description="Parse command line arguments."
    )

    parser.add_argument(
        "--graph",
        help="The output JSON file containing the adjacency graph",
        type=str,
    )
    parser.add_argument(
        "--data",
        type=str,
        help="Path to input data file",
    )
    parser.add_argument(
        "--mods",
        type=str,
        help="Path to output mods file",
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()

    return args


if __name__ == "__main__":
    main()

### END ###
