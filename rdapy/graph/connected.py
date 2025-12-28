#!/usr/bin/env python3

"""
CONTIGUOUS - Is a district in a plan fully connected?
"""

from typing import Any, List, Dict, Set, Tuple, NamedTuple

from itertools import combinations
import networkx as nx

from ..base import OUT_OF_STATE, DistanceLedger


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
    """Find the connected subsets of precincts in a graph."""

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


def canonical_pair(geoid1: str, geoid2: str) -> Tuple[str, str]:
    """Return a canonical ordering of a pair of geoids."""

    if geoid1 < geoid2:
        return (geoid1, geoid2)
    else:
        return (geoid2, geoid1)


class Island(NamedTuple):
    id: int
    precincts: int
    coastal: List[str]
    inland: List[str]
    counties: List[str]


class Connection(NamedTuple):
    from_geoid: str
    to_geoid: str
    distance: float


def subset_islands(
    islands: List[Island], county: str, verbose: bool = False
) -> List[Island]:
    """Return the list of 'islands' that include a given county."""

    subset: List[Island] = list()

    for island in islands[:-1]:
        if county in island.counties:
            subset.append(island)
        else:
            if verbose:
                print(
                    f"- Excluded island {island.id} from {county} county connections ..."
                )

    # Include the mainland if it has the island county
    mainland: Island = islands[-1]
    if county in mainland.counties:
        # # Prune the mainland 'island' to only include precincts in the county
        # coastal_precincts: List[str] = [c for c in mainland.coastal if county in c]
        # inland_precincts: List[str] = [i for i in mainland.inland if county in i]
        # precincts: int = len(coastal_precincts) + len(inland_precincts)
        # mainland = Island(
        #     mainland.id,
        #     precincts,
        #     coastal_precincts,
        #     inland_precincts,
        #     [county],
        # )

        # Add the mainland, but allow the shortest connections to any of its precincts
        subset.append(mainland)

        if verbose:
            print(f"- Included mainland 'island' in {county} county connections ...")

    return subset


def generate_contiguity_mods(
    geoids: List[str],
    adjacency_graph: Dict[str, List[str]],
    locations_by_geoid: Dict[str, Tuple[float, float]],
    verbose: bool = False,
) -> List[Tuple[str, str]]:
    """
    Generate connections (edges) between all 'islands' potentially including a mainland.
    - Minimimally connect all islands together.
    - Also connect islands (and the mainland) that share counties.
    """

    precinct_subsets: List[Set[Any]] = connected_subsets(geoids, adjacency_graph)

    # Segregate precincts into coastal and inland areas

    islands: List[Island] = list()

    for i, connected_precincts in enumerate(precinct_subsets):
        id: int = i
        precincts: int = 0
        coastal: List[str] = list()
        inland: List[str] = list()
        counties: Set[str] = set()

        for geoid in connected_precincts:
            precincts += 1

            if geoid in adjacency_graph[OUT_OF_STATE]:
                coastal.append(geoid)
            else:
                inland.append(geoid)

            county: str = geoid[2:5]
            counties.add(county)

        islands.append(Island(id, precincts, coastal, inland, list(counties)))

    # Find the island counties

    islands.sort(key=lambda x: x.precincts)
    island_counties: Set[str] = set()
    for island in islands[:-1]:
        island_counties.update(island.counties)

    if verbose:
        print(f"Identified {len(islands)} 'islands':")
        for i in islands:
            shore: str = i.coastal[0] if len(i.coastal) == 1 else "many"
            print(
                f"- Island {i.id}: {i.precincts} precincts, coastal: {len(i.coastal)} ({shore}), inland: {len(i.inland)}, counties: {i.counties}"
            )

    # Find shortest connections for all 'islands' together and for each island county

    auto_connections: Set[Tuple[str, str]] = set()

    for county in ["_all_"] + list(island_counties):
        if verbose:
            if county == "_all_":
                print(f"Finding shortest connections between all 'islands' ...")
            else:
                print(
                    f"Finding shortest connections between 'islands' in {county} county ..."
                )

        dl: DistanceLedger = DistanceLedger()

        island_subset: List[Island] = (
            islands if county == "_all_" else subset_islands(islands, county, verbose)
        )
        mainland: int = len(island_subset) - 1
        island_pairs: List[Tuple[int, int]] = list(
            combinations(range(len(island_subset)), 2)
        )
        possible_edges: Dict[Tuple[int, int], List[Connection]] = dict()
        shortest_edges: Dict[Tuple[int, int], Connection] = dict()

        for pair in island_pairs:
            possible_edges[pair] = list()

            for c1 in island_subset[pair[0]].coastal:
                for c2 in island_subset[pair[1]].coastal:
                    distance: float = dl.distance_between(
                        c1,
                        locations_by_geoid[c1],
                        c2,
                        locations_by_geoid[c2],
                    )
                    g1, g2 = canonical_pair(c1, c2)
                    edge: Connection = Connection(g1, g2, distance)
                    possible_edges[pair].append(edge)

            possible_edges[pair].sort(key=lambda x: x.distance)
            shortest_edges[pair] = possible_edges[pair][0]

            if verbose and mainland in pair:
                from_geoid: str = shortest_edges[pair].from_geoid
                to_geoid: str = shortest_edges[pair].to_geoid
                mainland_precinct: str = (
                    from_geoid
                    if from_geoid in island_subset[mainland].coastal
                    else to_geoid
                )
                print(f"- Mainland precinct: {mainland_precinct}")

        # Find the shortest distance paths that fully connect the islands, using a minimum spanning tree

        G = nx.Graph()
        for i in range(len(island_subset)):
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
        branches = sorted(T.edges(data=True))
        for _, _, data in branches:
            g1: str = data["geoid1"]
            g2: str = data["geoid2"]

            if not ((g1, g2) in auto_connections):
                if verbose:
                    print(f"- Connecting {g1} to {g2} ...")
                auto_connections.add((g1, g2))

    return list(auto_connections)


### END ###
