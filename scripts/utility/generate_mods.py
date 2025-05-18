#!/usr/bin/env python3

"""
GENERATE MODS FOR TO FULLY CONNECT AN ADJACENCY GRAPH

$ scripts/utility/generate_mods.py \
--graph ~/local/dra-to-publish/HI_2020_graph.json \
--mods temp/DEBUG_graph_mods.json

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import Any, List, Dict
import json

from rdapy import load_data, load_graph, sorted_geoids, is_connected, OUT_OF_STATE


def main() -> None:
    """Generate 'mods' (additional connections) to fully connect an adjacency graph."""

    args: Namespace = parse_args()

    #

    adjacency_graph: Dict[str, List[str]] = load_graph(args.graph)

    #

    geoids: List[str] = list(adjacency_graph.keys())
    geoids.remove(OUT_OF_STATE)
    geoids.sort()

    if is_connected(geoids, adjacency_graph):
        print(f"Graph is fully connected.")
    else:
        print(f"WARNING: Graph is NOT fully connected!")


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
