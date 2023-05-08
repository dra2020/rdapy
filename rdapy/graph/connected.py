#!/usr/bin/env python3

"""
CONTIGUOUS - Is a district in a plan fully connected?
"""

from typing import Any

from .constants import *


def is_connected(geos: list[Any], adjacency: dict[Any, list[Any]]) -> bool:
    """Is a graph is fully connected?
    i.e., w/o regard to the virtual state boundary "shapes".

    Kenshi's iterative implementation of the recursive algorithm

    geos - the list of geographies
    adjacency - the connectedness of the geos
    """
    visited: set[Any] = set()

    all_geos: set[Any] = set(geos)
    all_geos.discard(OUT_OF_STATE)

    start: str = next(iter(all_geos))
    assert start != OUT_OF_STATE

    to_process: list[Any] = [start]
    while to_process:
        node: Any = to_process.pop()
        visited.add(node)
        neighbors: list[Any] = list(adjacency[node])
        if OUT_OF_STATE in neighbors:
            neighbors.remove(OUT_OF_STATE)
        neighbors_to_visit: list[Any] = [
            n for n in neighbors if n in all_geos and n not in visited
        ]
        to_process.extend(neighbors_to_visit)

    return len(visited) == len(all_geos)


# LIMIT WHAT GETS EXPORTED.

__all__ = ["is_connected"]

### END ###
