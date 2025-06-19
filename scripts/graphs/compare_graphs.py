#!/usr/bin/env python3

"""
A UTILITY SCRIPT TO COMPARE SETS OF ADJACENCY GRAPHS

$ scripts/graphs/compare_graphs.py \
--one  ~/local/adjacency-graphs \
--two ~/local/dra-to-publish

"""

from typing import List, Dict

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

        diff_geoids: List[str] = list()
        diff_connections: List[str] = list()
        bad_graphs: List[str] = list()

        for xx, _ in DISTRICTS_BY_STATE.items():
            try:
                graph_path = path_to_graph(dir1, xx)
                graph1: Dict[str, List[str]] = load_graph(graph_path)

                graph_path = path_to_graph(dir2, xx)
                graph2: Dict[str, List[str]] = load_graph(graph_path)

                pass

            except Exception as e:
                bad_graphs.append(xx)
                continue

            if set(graph1.keys()) != set(graph2.keys()):
                diff_geoids.append(xx)
                continue

            for geoid in graph1.keys():
                if (
                    set(graph1[geoid]) != set(graph2[geoid])
                    and xx not in diff_connections
                ):
                    diff_connections.append((xx))

        if diff_geoids:
            print(f"These graphs differ in some geoids: {diff_geoids}.")
        else:
            print("These graphs have the same geoids.")

        if diff_connections:
            print(f"These graphs differ in some connections: {diff_connections}.")
        else:
            print("These graphs have the same connections.")

        if bad_graphs:
            print(f"These graphs could not be loaded: {bad_graphs}.")
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
