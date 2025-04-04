#!/usr/bin/env python3

"""
EXTRACT AN ADJACENCY GRAPH FROM A GEOJSON FILE

$ scripts/extract_graph.py \
--geojson testdata/data/NC_vtd_datasets.geojson \
--graph temp/DEBUG_graph.json

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


EPSILON: float = 1.0e-12
OUT_OF_STATE: str = "OUT_OF_STATE"


def main() -> None:
    """Extract census, demographic, election, and shape data from DRA's .geojson file."""

    args: Namespace = parse_args()

    # Load the geojson & create a rook adjacency graph

    with open(args.geojson, "r") as f:
        geojson: Dict[str, Any] = json.load(f)

    df: DataFrame = DataFrame([f.get("properties", {}) for f in geojson["features"]])
    gdf: GeoDataFrame = GeoDataFrame(df, geometry=[shape(f["geometry"]) for f in geojson["features"]])  # type: ignore
    graph: Dict[str, List[str]] = from_dataframe(gdf)

    # Add "operational contiguity" mods, if any

    if args.mods:
        mods: List = read_mods(args.mods)

        for mod in mods:
            graph = add_adjacency(graph, mod[1], mod[2])

    # Make sure the graph is consistent & fully connected

    if not is_consistent(graph):
        print(f"WARNING: Graph is not consistent.")

    geoids: List[str | int] = list(graph.keys())
    if not is_connected(geoids, graph):
        print(f"WARNING: Graph is not fully connected.")

    # Write the graph to a JSON file

    with open(args.graph, "w", encoding="utf-8") as f:
        json.dump(graph, f, ensure_ascii=False, indent=4)

    pass


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


def is_connected(geos: List[Any], adjacency: Dict[Any, List[Any]]) -> bool:
    """Make sure a graph is fully connected *internally*, i.e., w/o regard to the virtual state boundary "shapes".

    Kenshi's iterative implementation of the recursive algorithm

    geos - the list of geographies
    adjacency - the connectedness of the geos
    """
    visited: Set[Any] = set()

    all_geos: Set[Any] = set(geos)
    all_geos.discard(OUT_OF_STATE)

    start: str = next(iter(all_geos))
    assert start != OUT_OF_STATE

    to_process: List[Any] = [start]
    while to_process:
        node: Any = to_process.pop()
        visited.add(node)
        neighbors: List[Any] = list(adjacency[node])
        if OUT_OF_STATE in neighbors:
            neighbors.remove(OUT_OF_STATE)
        neighbors_to_visit: List[Any] = [
            n for n in neighbors if n in all_geos and n not in visited
        ]
        to_process.extend(neighbors_to_visit)

    return len(visited) == len(all_geos)


def parse_args() -> Namespace:
    """Parse command line arguments."""

    parser: ArgumentParser = argparse.ArgumentParser(
        description="Parse command line arguments."
    )

    parser.add_argument(
        "--geojson",
        help="The GeoJSON file",
        default="testdata/data/NC_vtd_datasets.geojson",
        type=str,
    )
    parser.add_argument(
        "--mods",
        help="An optional file containing contiguity modifications",
        type=str,
    )
    parser.add_argument(
        "--graph",
        help="The output JSON file containing the adjacency graph",
        default="temp/DEBUG_graph.json",
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
