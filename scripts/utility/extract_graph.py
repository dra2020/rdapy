#!/usr/bin/env python3

"""
EXTRACT AN ADJACENCY GRAPH FROM A GEOJSON FILE

$ scripts/utility/extract_graph.py \
--geojson /path/to/input.geojson \
--graph /path/to/output-graph.json

NOTE - If the graph is not fully connected, the output file will have
"_NOT_CONNECTED" appended to the filename.
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

from rdapy import is_consistent, is_connected, OUT_OF_STATE


EPSILON: float = 1.0e-12


def main() -> None:
    """Extract census, demographic, election, and shape data from DRA's .geojson file."""

    args: Namespace = parse_args()

    # Load the geojson & create a rook adjacency graph

    with open(args.geojson, "r") as f:
        geojson: Dict[str, Any] = json.load(f)

    df: DataFrame = DataFrame([f.get("properties", {}) for f in geojson["features"]])
    gdf: GeoDataFrame = GeoDataFrame(df, geometry=[shape(f["geometry"]) for f in geojson["features"]])  # type: ignore
    adjacency_graph: Dict[str, List[str]] = from_dataframe(gdf)

    # Check whether the graph is consistent & fully connected

    is_good: bool = True
    if not is_consistent(adjacency_graph):
        print(f"WARNING: Graph is not consistent.")
        is_good = False

    geoids: List[str | int] = list(adjacency_graph.keys())
    if not is_connected(geoids, adjacency_graph):
        print(f"WARNING: Graph is not fully connected.")
        is_good = False

    # Write the graph to a JSON file

    graph_path: str = os.path.abspath(args.graph)
    if not is_good:
        graph_path = os.path.splitext(graph_path)[0] + "_NOT_CONNECTED.json"

    with open(graph_path, "w", encoding="utf-8") as f:
        json.dump(adjacency_graph, f, ensure_ascii=False, indent=4)


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


def parse_args() -> Namespace:
    """Parse command line arguments."""

    parser: ArgumentParser = argparse.ArgumentParser(
        description="Parse command line arguments."
    )

    parser.add_argument(
        "--geojson",
        help="The GeoJSON file",
        type=str,
    )
    parser.add_argument(
        "--graph",
        help="The output JSON file containing the adjacency graph",
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
