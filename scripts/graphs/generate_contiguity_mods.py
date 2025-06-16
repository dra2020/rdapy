#!/usr/bin/env python3

"""
GENERATE CONTIGUITY MODS TO FULLY CONNECT AN ADJACENCY GRAPH

$ scripts/graphs/generate_contiguity_mods.py \
--graph /path/to/input-graph.json \
--locations /path/to/precinct-locations.json \
> /path/to/contiguity_mods.csv

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import Any, List, Dict

import os, sys, json


from rdapy import (
    load_graph,
    OUT_OF_STATE,
    is_connected,
    generate_contiguity_mods,
)

from rdapy import index_data


def main() -> None:
    """Generate 'mods' (additional connections) to fully connect an adjacency graph."""

    args: Namespace = parse_args()

    #

    # data_map: Dict[str, Any]
    # input_data: List[Dict[str, Any]]
    # data_map, input_data = load_data(args.data)
    adjacency_graph: Dict[str, List[str]] = load_graph(args.graph)
    with open(os.path.expanduser(args.locations), "r") as f:
        locations_by_geoid: Dict[str, Any] = json.load(f)

    #

    # data_by_geoid: Dict[str, Dict[str, Any]] = index_data(input_data)

    geoids: List[str] = list(adjacency_graph.keys())
    geoids.remove(OUT_OF_STATE)
    geoids.sort()

    if is_connected(geoids, adjacency_graph):
        print(f"Graph is fully connected.")
        sys.exit(0)

    # Graph is not fully connected.

    connections = generate_contiguity_mods(geoids, adjacency_graph, locations_by_geoid)

    # Generate these edges as additional connections ("mods")

    for _, _, data in connections:
        print(f"+,{data["geoid1"]},{data["geoid2"]}")

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
        required=True,
    )
    parser.add_argument(
        "--locations",
        help="The output JSON file containing preinct locations",
        type=str,
        required=True,
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()

    return args


if __name__ == "__main__":
    main()

### END ###
