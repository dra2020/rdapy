#!/usr/bin/env python3

"""
A UTILITY SCRIPT TO COMPARE TWO ADJACENCY GRAPHS

Graphs are the same, iff:
- They have the same geoids (nodes)
- For each geoid, they have the same neighbors (edges)
- The geoids are in the same order
- The neighbors are in the same order

For example:

$ scripts/graphs/compare_2_graphs.py \
--graph1 /path/to/graph1.json \
--graph2 /path/to/graph2.json

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import List, Dict, Set

from rdapy import load_graph


def main() -> None:
    """Check whether two adjacency graphs are identical."""

    args: Namespace = parse_args()

    graph1: Dict[str, List[str]] = load_graph(args.graph1)
    graph2: Dict[str, List[str]] = load_graph(args.graph2)

    # The two graphs should have the same nodes (geoids)

    nodes1: Set[str] = set(graph1.keys())
    nodes2: Set[str] = set(graph2.keys())

    if nodes1 != nodes2:
        print()
        print(f"These graphs differ in geoids: {nodes1 ^ nodes2}")
        print()
    else:
        print("These graphs have the same geoids (nodes).")

    # The two graphs should have the same neighbors (edges)

    same_edges: bool = True
    for geoid in graph1.keys():
        edges1: Set[str] = set(graph1[geoid])
        edges2: Set[str] = set(graph2[geoid])
        if edges1 != edges2:
            same_edges = False
            print(f"These graphs differ in neighbors for {geoid}: {edges1 ^ edges2}")
            print()
    if same_edges:
        print("These graphs have the same neighbors (edges).")
    print()

    pass


def parse_args() -> Namespace:
    """Parse command line arguments."""

    parser: ArgumentParser = argparse.ArgumentParser(
        description="Parse command line arguments."
    )

    parser.add_argument(
        "--graph1",
        type=str,
        help="Path to the first adjacency graph JSON file",
    )
    parser.add_argument(
        "--graph2",
        help="Path to the second adjacency graph JSON file",
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
