#!/usr/bin/env python3

"""
A UTILITY SCRIPT TO COMPARE SETS OF ADJACENCY GRAPHS

$ scripts/graphs/compare_graphs.py \
--one  ~/local/adjacency-graphs \
--two ~/local/dra-to-publish

"""

from typing import List, Dict

import os

from rdapy import DISTRICTS_BY_STATE, load_graph


def main() -> None:
    """Check whether two sets of adjacency graph are the same."""

    # dir1: str = "~/local/adjacency-graphs"
    dir1: str = "~/local/dra-to-publish"
    # dir2: str = "~/local/dra-to-publish"
    dir2: str = "~/local/dra-data/data"

    print(f"Comparing graphs in {dir1} and {dir2}.")

    diff_geoids: List[str] = list()
    diff_connections: List[str] = list()
    bad_graphs: List[str] = list()

    for xx, _ in DISTRICTS_BY_STATE.items():
        try:
            file1: str = f"{xx}_2020_graph.json"
            # file2: str = f"{xx}_2020_graph.json"
            file2: str = f"contiguity.json"

            graph_path = os.path.expanduser(dir1 + "/" + file1)
            graph1: Dict[str, List[str]] = load_graph(graph_path)

            # graph_path = os.path.expanduser(dir2 + "/" + file2)
            graph_path = os.path.expanduser(dir2 + f"/{xx}/2020_VD/" + file2)
            graph2: Dict[str, List[str]] = load_graph(graph_path)

        except Exception as e:
            bad_graphs.append(xx)
            continue

        if set(graph1.keys()) != set(graph2.keys()):
            diff_geoids.append(xx)
            continue

        for geoid in graph1.keys():
            if set(graph1[geoid]) != set(graph2[geoid]) and xx not in diff_connections:
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

    pass


if __name__ == "__main__":
    main()

### END ###
