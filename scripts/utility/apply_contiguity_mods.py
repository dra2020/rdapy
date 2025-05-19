#!/usr/bin/env python3

"""
APPLY CONTIGUITY MODS TO FULLY CONNECT AN ADJACENCY GRAPH

$ scripts/utility/apply_contiguity_mods.py \
--graph ~/local/dra-to-publish/HI_2020_graph.json \
--mods ~/local/adjacency-graphs/HI_2020_contiguity_mods.csv \
> ~/local/adjacency-graphs/HI_2020_graph.json

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import Any, List, Dict, Set, Iterable
import os, sys, json, csv

from pandas import DataFrame
from geopandas import GeoDataFrame
from shapely.geometry import (
    shape,
    Polygon,
    MultiPolygon,
)
from libpysal.weights import Rook, WSP

from rdapy import is_consistent, is_connected, OUT_OF_STATE, load_graph


EPSILON: float = 1.0e-12


def main() -> None:
    """Update an adjacency graph with additional connections."""

    args: Namespace = parse_args()

    # Load the unmodified adjacency graph

    adjacency_graph: Dict[str, List[str]] = load_graph(args.graph)

    # Add "operational contiguity" mods, if any

    mods: List = read_mods(args.mods)

    for mod in mods:
        adjacency_graph = add_adjacency(adjacency_graph, mod[1], mod[2])

    # Make sure the graph is consistent & fully connected

    is_good: bool = True
    if not is_consistent(adjacency_graph):
        print(f"WARNING: Graph is not consistent.")
        is_good = False

    geoids: List[str | int] = list(adjacency_graph.keys())
    if not is_connected(geoids, adjacency_graph):
        print(f"WARNING: Graph is not fully connected.")
        is_good = False

    if not is_good:
        sys.exit(1)

    # Write the graph to STDOUT

    print(json.dumps(adjacency_graph, indent=4))


### HELPERS ###


def from_dataframe(df: GeoDataFrame, geoid_field: str = "id") -> Dict[str, List[str]]:
    """Extract a rook graph from a DataFrame."""

    g: Rook | WSP = Rook.from_dataframe(df, ids=geoid_field)
    assert isinstance(g, Rook)

    graph: Dict[str, List[str]] = (
        g.neighbors
    )  # Get rid of all the extraneous PySAL stuff
    shp_by_geoid: Dict[
        str,
        Polygon | MultiPolygon,
    ] = _index_shapes(df, geoid_field)
    graph: Dict[str, List[str]] = _add_out_of_state_neighbors(graph, shp_by_geoid)

    return graph


def _index_shapes(gdf: GeoDataFrame, geoid_field: str = "id") -> Dict[
    str,
    Polygon | MultiPolygon,
]:
    """Index the shapes by the geoid."""

    shapes_by_id: Dict[
        str,
        Polygon | MultiPolygon,
    ] = dict()

    for i, row in gdf.iterrows():
        geoid: str = getattr(row, geoid_field)
        shp: Polygon | MultiPolygon = shape(row["geometry"])  # type: ignore

        shapes_by_id[geoid] = shp

    return shapes_by_id


def _add_out_of_state_neighbors(
    graph: Dict[str, List[str]],
    shp_by_geoid: Dict[
        str,
        Polygon | MultiPolygon,
        # Point
        # | MultiPoint
        # | LineString
        # | MultiLineString
        # | Polygon
        # | MultiPolygon
        # | LinearRing
        # | GeometryCollection,
    ],
) -> Dict[str, List[str]]:
    """Add the virtual OUT_OF_STATE geoids to reflect interstate borders."""

    new_graph: Dict[str, List[str]] = dict()
    new_graph[OUT_OF_STATE] = []

    for node, neighbors in graph.items():
        new_graph[node] = []

        node_shp: Polygon | MultiPolygon = shp_by_geoid[node]
        perimeter: float = node_shp.length
        total_shared_border: float = 0.0

        for neighbor in neighbors:
            new_graph[node].append(neighbor)

            neighbor_shp: Polygon | MultiPolygon = shp_by_geoid[neighbor]
            shared_edge = node_shp.intersection(neighbor_shp)
            shared_border: float = shared_edge.length

            total_shared_border += shared_border

        if (perimeter - total_shared_border) > EPSILON:
            new_graph[node].append(OUT_OF_STATE)
            new_graph[OUT_OF_STATE].append(node)

    return new_graph


def read_mods(mods_csv) -> List:
    """Read a CSV file of modifications to a graph.

    Example:

    +, 440099902000, 440099901000
    """

    mods: List = list()

    try:
        # Get the full path to the .csv
        mods_path: str = os.path.expanduser(mods_csv)

        with open(mods_path, mode="r", encoding="utf-8-sig") as f_input:
            reader: Iterable[List[str]] = csv.reader(
                f_input, skipinitialspace=True, delimiter=",", quoting=csv.QUOTE_NONE
            )

            for row in reader:
                mods.append(row)

    except Exception:
        print("Exception reading mods.csv")
        sys.exit()

    return mods


def add_adjacency(
    graph: Dict[str, List[str]], node1: str | int, node2: str | int
) -> Dict[str, List[str]]:
    """Connect two nodes in the graph."""

    if node1 not in graph or node2 not in graph:
        raise ValueError("Both nodes must be in the graph to connect them.")

    graph[node1].append(node2)
    graph[node2].append(node1)

    return graph


def parse_args() -> Namespace:
    """Parse command line arguments."""

    parser: ArgumentParser = argparse.ArgumentParser(
        description="Parse command line arguments."
    )

    parser.add_argument(
        "--graph",
        help="The adjacency graph JSON file",
        type=str,
    )
    parser.add_argument(
        "--mods",
        help="A file containing contiguity modifications",
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
