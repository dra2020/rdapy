#!/usr/bin/env python3

"""
A UTILITY SCRIPT TO COMPARE SETS OF ADJACENCY GRAPHS

NOTE - THE SCRIPT compare_2_graphs.py DOES A MORE COMPLETE COMPARISON

$ scripts/graphs/compare_graphs.py

"""

from typing import List, Dict, Tuple, Set

import os
from itertools import combinations

from rdapy import DISTRICTS_BY_STATE, load_graph


def main() -> None:
    """Check whether two sets of adjacency graph are the same."""

    graph_dirs: List[str] = ["vtd_data", "dra_data", "adjacency-graphs"]
    combos: List[tuple] = list(combinations(graph_dirs, 2))

    print()
    for dir1, dir2 in combos:
        print(f"Comparing graphs in {dir1} and {dir2}.")

        diff_geoids: List[Tuple[str, Set[str]]] = list()
        diff_connections: List[Tuple[str, str, Set[str]]] = list()
        bad_graphs: List[Tuple[str, str]] = list()

        for xx, _ in DISTRICTS_BY_STATE.items():
            try:
                graph_path = path_to_graph(dir1, xx)
                graph_dir = dir1
                graph1: Dict[str, List[str]] = load_graph(graph_path)

                graph_path = path_to_graph(dir2, xx)
                graph_dir = dir2
                graph2: Dict[str, List[str]] = load_graph(graph_path)

                pass

            except Exception as e:
                bad_graphs.append((xx, graph_dir))
                continue

            nodes1: Set[str] = set(graph1.keys())
            nodes2: Set[str] = set(graph2.keys())
            if nodes1 != nodes2:
                diff_geoids.append((xx, nodes1 ^ nodes2))
                continue

            for geoid in graph1.keys():
                edges1: Set[str] = set(graph1[geoid])
                edges2: Set[str] = set(graph2[geoid])
                if edges1 != edges2:
                    diff_connections.append((xx, geoid, edges1 ^ edges2))

        if diff_geoids:
            print(f"These graphs differ in some geoids:")
            for diff in diff_geoids:
                print(f"  {diff}")
        else:
            print("These graphs have the same geoids.")

        if diff_connections:
            print(f"These graphs differ in some connections:")
            for diff in diff_connections:
                print(f"  {diff}")
        else:
            print("These graphs have the same connections.")

        if bad_graphs:
            print(f"These graphs could not be loaded:")
            for diff in bad_graphs:
                print(f"  {diff}")
        else:
            print("All graphs loaded successfully.")
        print()

    pass


def path_to_graph(dir: str, xx: str) -> str:
    """Return the path to the graph directory."""

    graph_path: str

    if dir == "vtd_data":
        graph_path = os.path.expanduser(
            f"~/dev/vtd_data/2020_VTD/{xx}/{xx}_2020_graph.json"
        )
        return graph_path

    if dir == "dra_data":
        graph_path = os.path.expanduser(
            f"~/local/dra-data/data/{xx}/2020_VD/contiguity.json"
        )
        return graph_path

    if dir == "adjacency-graphs":
        graph_path = os.path.expanduser(
            f"~/local/adjacency-graphs/{xx}_2020_graph.json"
        )
        return graph_path

    assert False, f"Unknown directory: {dir}"


if __name__ == "__main__":
    main()

### END ###
