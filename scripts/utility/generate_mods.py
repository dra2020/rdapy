#!/usr/bin/env python3

"""
GENERATE MODS FOR TO FULLY CONNECT AN ADJACENCY GRAPH

$ scripts/utility/generate_mods.py \
--graph ~/local/dra-to-publish/HI_2020_graph.json \
--mods temp/DEBUG_graph_mods.json

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import Any, List, Dict, Set, NamedTuple

import sys

from rdapy import (
    load_graph,
    OUT_OF_STATE,
    load_data,
    is_connected,
    connected_subsets,
)

from rdapy.score import index_data, DatasetKey, get_dataset, get_fields


class Island(NamedTuple):
    id: int
    population: int
    precincts: int
    coastal: List[str]
    inland: List[str]


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
    subsets: List[Set[Any]] = connected_subsets(geoids, adjacency_graph)
    islands: List[Island] = list()

    for i, subset in enumerate(subsets):
        id: int = i + 1
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

    # Sort islands by population
    islands.sort(key=lambda x: x.population, reverse=True)

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
