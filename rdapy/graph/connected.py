#!/usr/bin/env python3

"""
CONTIGUOUS - Is a district in a plan fully connected?
"""

from typing import Any, List, Dict, Set

from .constants import *


def is_consistent(graph: Dict[str, List[str]]) -> bool:
    """Make sure each node is in every neighbor's neighbor list"""

    for node, neighbors in graph.items():
        for neighbor in neighbors:
            neighbor_neighbors: List[str] = graph[neighbor]
            if node in neighbor_neighbors:
                pass
            else:
                return False

    return True


def is_connected(ids: List[Any], graph: Dict[str, List[str]]) -> bool:
    """Is a district fully connected?
    i.e., w/o regard to the virtual state boundary "shapes".

    Kenshi's iterative implementation of the recursive algorithm

    ids - the list of ids for the geographies
    graph - the connectedness (adjacency) of the geos
    """
    visited: Set[Any] = set()

    all_geos: Set[Any] = set(ids)
    all_geos.discard(OUT_OF_STATE)

    start: str = next(iter(all_geos))

    to_process: List[Any] = [start]
    while to_process:
        node: Any = to_process.pop()
        visited.add(node)
        neighbors: List[Any] = list(graph[node])
        if OUT_OF_STATE in neighbors:
            neighbors.remove(OUT_OF_STATE)
        neighbors_to_visit: List[Any] = [
            n for n in neighbors if n in all_geos and n not in visited
        ]
        to_process.extend(neighbors_to_visit)

    return len(visited) == len(all_geos)


def connected_subsets(ids: List[Any], graph: Dict[str, List[str]]) -> List[Set[Any]]:
    """Find the connected subsets of a list of ids."""

    remaining_geos: Set[Any] = set(ids)
    remaining_geos.discard(OUT_OF_STATE)

    subsets: List[Set[Any]] = list()

    while remaining_geos:
        visited: Set[Any] = set()

        start: str = next(iter(remaining_geos))

        to_process: List[Any] = [start]
        while to_process:
            node: Any = to_process.pop()
            visited.add(node)
            neighbors: List[Any] = list(graph[node])
            if OUT_OF_STATE in neighbors:
                neighbors.remove(OUT_OF_STATE)
            neighbors_to_visit: List[Any] = [
                n for n in neighbors if n in remaining_geos and n not in visited
            ]
            to_process.extend(neighbors_to_visit)

        subsets.append(visited)
        remaining_geos -= visited

    return subsets


### END ###
