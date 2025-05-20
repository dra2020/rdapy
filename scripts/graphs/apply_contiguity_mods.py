#!/usr/bin/env python3

"""
APPLY CONTIGUITY MODS TO FULLY CONNECT AN ADJACENCY GRAPH

$ scripts/graph/apply_contiguity_mods.py \
--graph /path/to/input-graph.json \
--mods/path/to/contiguity_mods.csv \
> /path/to/output-graph.json

NOTE - Make sure the input and output graph files are different!
"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import Any, List, Dict, Set, Iterable
import os, sys, json, csv

from pandas import DataFrame
from geopandas import GeoDataFrame
from shapely.geometry import (
    shape,
    Polygon,
    MultiPolygon,
)
from libpysal.weights import Rook, WSP

from rdapy import is_consistent, is_connected, OUT_OF_STATE, load_graph


EPSILON: float = 1.0e-12


def main() -> None:
    """Update an adjacency graph with additional connections."""

    args: Namespace = parse_args()

    # Load the unmodified adjacency graph

    adjacency_graph: Dict[str, List[str]] = load_graph(args.graph)

    # Add "operational contiguity" mods, if any

    mods: List = read_mods(args.mods)

    for mod in mods:
        adjacency_graph = add_adjacency(adjacency_graph, mod[1], mod[2])

    # Make sure the graph is consistent & fully connected

    is_good: bool = True
    if not is_consistent(adjacency_graph):
        print(f"WARNING: Graph is not consistent.")
        is_good = False

    geoids: List[str | int] = list(adjacency_graph.keys())
    if not is_connected(geoids, adjacency_graph):
        print(f"WARNING: Graph is not fully connected.")
        is_good = False

    if not is_good:
        sys.exit(1)

    # Write the graph to STDOUT

    print(json.dumps(adjacency_graph, indent=4))


### HELPERS ###


def read_mods(mods_csv) -> List:
    """Read a CSV file of modifications to a graph.

    Example:

    +, 440099902000, 440099901000
    """

    mods: List = list()

    try:
        # Get the full path to the .csv
        mods_path: str = os.path.expanduser(mods_csv)

        with open(mods_path, mode="r", encoding="utf-8-sig") as f_input:
            reader: Iterable[List[str]] = csv.reader(
                f_input, skipinitialspace=True, delimiter=",", quoting=csv.QUOTE_NONE
            )

            for row in reader:
                mods.append(row)

    except Exception:
        print("Exception reading mods.csv")
        sys.exit()

    return mods


def add_adjacency(
    graph: Dict[str, List[str]], node1: str | int, node2: str | int
) -> Dict[str, List[str]]:
    """Connect two nodes in the graph."""

    if node1 not in graph or node2 not in graph:
        raise ValueError("Both nodes must be in the graph to connect them.")

    graph[node1].append(node2)
    graph[node2].append(node1)

    return graph


def parse_args() -> Namespace:
    """Parse command line arguments."""

    parser: ArgumentParser = argparse.ArgumentParser(
        description="Parse command line arguments."
    )

    parser.add_argument(
        "--graph",
        help="The adjacency graph JSON file",
        type=str,
    )
    parser.add_argument(
        "--mods",
        help="A file containing contiguity modifications",
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
