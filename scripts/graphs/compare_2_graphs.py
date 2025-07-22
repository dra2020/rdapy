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

    print()
    print("Comparing two adjacency graphs:")
    print(f"  - {args.graph1}, and")
    print(f"  - {args.graph2}")
    print()

    print("  Comparing geoids (nodes):")

    # Compare geoids (nodes)
    # The two graphs should have the same geoids (nodes) in the same order

    nodes1: List[str] = list(graph1.keys())
    nodes2: List[str] = list(graph2.keys())

    diff_geoids: Set[str] = set(nodes1) ^ set(nodes2)
    if diff_geoids:
        print(f"  - These graphs have some different geoids (nodes): {diff_geoids}")
    else:
        print("  - These graphs have the same geoids (nodes).")

    if not diff_geoids and nodes1 != nodes2:
        print(f"  - BUT some geoids (nodes) in these graphs are in different orders.")
    else:
        print("  - The geoids (nodes) in these graphs are in the same order.")
    print()

    print("  Comparing neighbors (edges):")

    # Compare neighbors (edges)
    # The two graphs should have the same neighbors (edges) in the same order

    same_edges: bool = True
    for geoid in graph1.keys():
        edges1: List[str] = list(graph1[geoid])
        edges2: List[str] = list(graph2[geoid])

        diff_neighbors: Set[str] = set(edges1) ^ set(edges2)
        if diff_neighbors:
            same_edges = False
            print(
                f"  - These graphs have different neighbors for {geoid}: {diff_neighbors}"
            )

        if not diff_neighbors and edges1 != edges2:
            same_edges = False
            print(f"  - The neighbors for {geoid} are in different orders.")

    if same_edges:
        print("  - These graphs have the same neighbors (edges) in the same order.")

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
