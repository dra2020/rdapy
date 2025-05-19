#!/usr/bin/env python3

"""
CONTIGUOUS - Is a district in a plan fully connected?
"""

from typing import Any, List, Dict, Set, Tuple, NamedTuple

from itertools import combinations
import networkx as nx

from .constants import *
from ..score.aggregate import DatasetKey, get_dataset, get_fields
from ..score.geographic import DistanceLedger


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


class Island(NamedTuple):
    id: int
    population: int
    precincts: int
    coastal: List[str]
    inland: List[str]


class Connection(NamedTuple):
    from_geoid: str
    to_geoid: str
    distance: float


def generate_contiguity_mods(
    geoids: List[str],
    adjacency_graph: Dict[str, List[str]],
    data_by_geoid: Dict[str, Dict[str, Any]],
) -> List[Connection]:
    """Find all the connected subsets of precincts ("islands" including a mainland)"""

    census_dataset: DatasetKey = get_dataset(data_map, "census")
    total_pop_field: str = get_fields(data_map, "census", census_dataset)["total_pop"]

    subsets: List[Set[Any]] = connected_subsets(geoids, adjacency_graph)

    # Segregate precincts into coasts and inland areas

    islands: List[Island] = list()

    for i, subset in enumerate(subsets):
        id: int = i
        pop: int = 0
        precincts: int = 0
        coastal: List[str] = list()
        inland: List[str] = list()

        for geoid in subset:
            precincts += 1
            pop += data_by_geoid[geoid][total_pop_field]

            if geoid in adjacency_graph[OUT_OF_STATE]:
                coastal.append(geoid)
            else:
                inland.append(geoid)

        islands.append(Island(id, pop, precincts, coastal, inland))

    # Find the shortest distance between each pair of islands

    dl: DistanceLedger = DistanceLedger()

    island_pairs: List[Tuple[int, int]] = list(combinations(range(len(islands)), 2))
    possible_edges: Dict[Tuple[int, int], List[Connection]] = dict()
    shortest_edges: Dict[Tuple[int, int], Connection] = dict()

    for pair in island_pairs:
        possible_edges[pair] = list()

        for c1 in islands[pair[0]].coastal:
            for c2 in islands[pair[1]].coastal:
                distance: float = dl.distance_between(
                    c1, data_by_geoid[c1]["center"], c2, data_by_geoid[c2]["center"]
                )
                edge: Connection = Connection(c1, c2, distance)
                possible_edges[pair].append(edge)
        possible_edges[pair].sort(key=lambda x: x.distance)
        shortest_edges[pair] = possible_edges[pair][0]

    # Find the shortest distance paths that fully connect the islands, using a minimum spanning tree

    G = nx.Graph()
    for i in range(len(islands)):
        G.add_node(i)
    for pair in island_pairs:
        G.add_edge(
            pair[0],
            pair[1],
            weight=shortest_edges[pair].distance,
            geoid1=shortest_edges[pair].from_geoid,
            geoid2=shortest_edges[pair].to_geoid,
        )
    T = nx.minimum_spanning_tree(G)
    connections = sorted(T.edges(data=True))

    return connections


### END ###
