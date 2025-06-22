#!/usr/bin/env python3

"""
VERIFY THAN AN ADJACENCY GRAPH IS FULLY CONNECTED

Before running this script, extract the data from the GeoJSON package.

$ scripts/graphs/check_graph.py \
--state NC \
--data /path/to/NC_input_data.jsonl \
--graph /path/to/NC_2020_graph.json

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import Any, List, Dict

from rdapy import load_data, load_graph, sorted_geoids, is_connected, OUT_OF_STATE


def main() -> None:
    """Check whether an adjacency graph is fully connected."""

    args: Namespace = parse_args()

    #
    data_map: Dict[str, Any]
    input_data: List[Dict[str, Any]]
    data_map, input_data = load_data(args.data)
    adjacency_graph: Dict[str, List[str]] = load_graph(args.graph)

    #

    geoids: List[str] = sorted_geoids(input_data)

    if is_connected(geoids, adjacency_graph):
        print(f"Graph for {args.state} is fully connected.")
    else:
        print(f"WARNING: Graph for {args.state} is not fully connected!")


### HELPERS ###


def parse_args() -> Namespace:
    """Parse command line arguments."""

    parser: ArgumentParser = argparse.ArgumentParser(
        description="Parse command line arguments."
    )

    parser.add_argument("--state", type=str, help="State abbreviation")
    parser.add_argument(
        "--data",
        type=str,
        help="Path to input data file",
    )
    parser.add_argument(
        "--graph",
        help="The output JSON file containing the adjacency graph",
        type=str,
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()

    return args


if __name__ == "__main__":
    main()

### END ###
