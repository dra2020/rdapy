#!/usr/bin/env python3

"""
GENERATE CONTIGUITY MODS TO FULLY CONNECT AN ADJACENCY GRAPH

$ scripts/graphs/generate_contiguity_mods.py \
--graph /path/to/input-graph.json \
--geojson /path/to/input.geojson \
> /path/to/contiguity_mods.csv

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import Any, List, Dict, Tuple, Set, NamedTuple
from itertools import combinations

import os, sys, json, math
import networkx as nx


from rdapy import (
    generate_contiguity_mods,
)

OUT_OF_STATE: str = "OUT_OF_STATE"


def main() -> None:
    """Generate 'mods' (additional connections) to fully connect an adjacency graph."""

    args: Namespace = parse_args()

    # Load a not-fully-connected adjacency graph

    with open(os.path.expanduser(args.graph), "r") as f:
        graph_data = json.load(f)
    adjacency_graph: Dict[str, List[str]] = {
        key: list(value) for key, value in graph_data.items()
    }

    # Extract precinct locations from the GeoJSON file

    with open(args.geojson, "r") as f:
        geojson: Dict[str, Any] = json.load(f)
    locations_by_geoid: Dict[str, Any] = dict()
    geoid_field: str = "id"

    for feature in geojson["features"]:
        geoid: str = feature["properties"][geoid_field]

        # Use the label coordinates as the "center" of the precinct
        center: Tuple[float, float] = (
            feature["properties"]["labelx"],
            feature["properties"]["labely"],
        )

        locations_by_geoid[geoid] = center

    geoids: List[str] = list(adjacency_graph.keys())
    geoids.remove(OUT_OF_STATE)
    geoids.sort()

    if is_connected(geoids, adjacency_graph):
        print(f"Graph is fully connected.")
        sys.exit(0)

    # Graph is not fully connected.

    # Find the minimum spanning tree of the graph, which will connect all the precincts

    connections = generate_contiguity_mods(geoids, adjacency_graph, locations_by_geoid)

    # Print it out as CSV rows

    for _, _, data in connections:
        print(f"+,{data["geoid1"]},{data["geoid2"]}")

    pass


#


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
    locations_by_geoid: Dict[str, Tuple[float, float]],
) -> List[Tuple[int, int, Dict[str, Any]]]:
    """Find all the connected subsets of precincts -- "islands" potentially including a mainland"""

    subsets: List[Set[Any]] = connected_subsets(geoids, adjacency_graph)

    # Segregate precincts into coasts and inland areas

    islands: List[Island] = list()

    for i, subset in enumerate(subsets):
        id: int = i
        precincts: int = 0
        coastal: List[str] = list()
        inland: List[str] = list()

        for geoid in subset:
            precincts += 1

            if geoid in adjacency_graph[OUT_OF_STATE]:
                coastal.append(geoid)
            else:
                inland.append(geoid)

        islands.append(Island(id, precincts, coastal, inland))

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
                    c1,
                    locations_by_geoid[c1],
                    c2,
                    locations_by_geoid[c2],
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


#


def distance_proxy(a: Tuple[float, float], b: Tuple[float, float]) -> float:
    """
    Calculate a proxy for the distance between two points expressed as (lon, lat) tuples.

    No need for sqrt() since we are only *comparing* distances.
    """

    lat_squared: float = (a[1] - b[1]) * (a[1] - b[1])
    lon_squared: float = (a[0] - b[0]) * (a[0] - b[0])

    return lat_squared + lon_squared


def distance(a: Tuple[float, float], b: Tuple[float, float]) -> float:
    """Calculate the distance between two points expressed as (lon, lat) tuples."""

    return math.sqrt((a[1] - b[1]) * (a[1] - b[1]) + (a[0] - b[0]) * (a[0] - b[0]))


def make_precinct_pair(precinct1: str, precinct2: str) -> Tuple[str, str]:
    """Return a pair of precincts in canonical sorted order."""

    return (precinct1, precinct2) if precinct1 < precinct2 else (precinct2, precinct1)


class DistanceLedger:
    """Compute and cache distances between pairs of precincts as needed."""

    def __init__(self):
        self.distances: Dict[Tuple[str, str], float] = dict()

    def distance_between(
        self,
        geoid1: str,
        center1: Tuple[float, float],
        geoid2: str,
        center2: Tuple[float, float],
    ) -> float:
        pair: Tuple[str, str] = make_precinct_pair(geoid1, geoid2)
        if pair in self.distances:
            return self.distances[pair]
        else:
            d: float = distance_proxy(center1, center2)
            self.distances[pair] = d
            return d


#


def parse_args() -> Namespace:
    """Parse command line arguments."""

    parser: ArgumentParser = argparse.ArgumentParser(
        description="Parse command line arguments."
    )

    parser.add_argument(
        "--graph",
        help="The output JSON file containing the adjacency graph",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--geojson",
        help="The GeoJSON file",
        type=str,
        required=True,
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()

    return args


if __name__ == "__main__":
    main()

### END ###
