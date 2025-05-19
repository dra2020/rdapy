#!/usr/bin/env python3

"""
EXTRACT DATA & SHAPES FROM A GEOJSON FILE

$ scripts/extract_data.py \
--geojson testdata/data/NC_vtd_datasets.v3.geojson \
--data-map testdata/examples/NC_data_map.v3.json \
--graph testdata/examples/NC_graph.json \
--data temp/DEBUG_input_data.jsonl

$ scripts/extract_data.py \
--geojson testdata/data/NC_vtd_datasets.v4.geojson \
--data-map testdata/examples/NC_data_map.v4.json \
--graph testdata/examples/NC_graph.json \
--data temp/DEBUG_input_data.jsonl

$ scripts/extract_data.py \
--geojson testdata/data/NC_vtd_datasets.v4.geojson \
--data-map testdata/examples/NC_data_map.v4.json \
--graph testdata/examples/NC_graph.json \
--data testdata/examples/NC_input_data.v4.jsonl

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import Any, List, Dict, Tuple, TextIO, Optional, Generator

import json, contextlib, os, sys

from pandas import DataFrame
from geopandas import GeoDataFrame
from shapely.geometry import (
    shape,
    Polygon,
    MultiPolygon,
    Point,
)

from rdapy import smart_write

EPSILON: float = 1.0e-12
OUT_OF_STATE: str = "OUT_OF_STATE"


def main() -> None:
    """Extract census, demographic, election, and shape data from DRA's .geojson file."""

    args: Namespace = parse_args()

    # Load the data map, the geojson file, & the adjacency graph

    with open(args.data_map, "r") as f:
        data_map: Dict[str, Any] = json.load(f)
    with open(args.geojson, "r") as f:
        geojson: Dict[str, Any] = json.load(f)
    with open(args.graph, "r") as f:
        graph: Dict[str, List[str]] = json.load(f)

    # Index the shapes by geoid

    df: DataFrame = DataFrame([f.get("properties", {}) for f in geojson["features"]])
    gdf: GeoDataFrame = GeoDataFrame(df, geometry=[shape(f["geometry"]) for f in geojson["features"]])  # type: ignore
    shp_by_geoid: Dict[str, Polygon | MultiPolygon] = index_shapes(gdf)

    # Collect the census, demographic, election, and shape data (including abstracts)

    by_geoid: Dict[str, Any] = dict()

    for feature in geojson["features"]:
        geoid: str = feature["properties"][data_map["geoid"]]
        precinct_data: Dict[str, Any] = {"geoid": geoid}

        # Cull the census, demographic, election, and shape data

        data_abstract: Dict[str, Any] = abstract_data(feature, data_map)
        precinct_data.update(data_abstract)

        # Abstract the shape

        shp: Polygon | MultiPolygon = shp_by_geoid[geoid]
        shp_abstract: Dict[str, Any] = abstract_shape(shp_by_geoid, graph, geoid, shp)
        # Override the 'center' with DRA's label coordinates
        shp_abstract["center"] = (
            feature["properties"]["labelx"],
            feature["properties"]["labely"],
        )
        precinct_data.update(shp_abstract)

        by_geoid[geoid] = precinct_data

    # Format the data as JSONL records & write them disk

    records: List[Dict[str, Any]] = [
        {"geoid": geoid, **values} for geoid, values in by_geoid.items()
    ]

    with smart_write(args.data) as output_stream:
        # Write the scores metadata record to the by-district file
        metadata_record: Dict[str, Any] = {
            "_tag_": "metadata",
            "properties": data_map,
        }
        write_record(metadata_record, output_stream)

        for record in records:
            record: Dict[str, Any] = {
                "_tag_": "precinct",
                "data": record,
            }
            write_record(record, output_stream)

    pass


### HELPERS ###


def index_shapes(gdf: GeoDataFrame, geoid_field: str = "id") -> Dict[
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


def abstract_data(feature, data_map: Dict[str, Any]) -> Dict[str, Any]:
    """Abstract the census, demographic, election, and shape data from a GeoJSON feature"""

    data_abstract: Dict[str, Any] = dict()

    qualified_field: str
    for dataset_type in ["census", "vap", "cvap", "election", "shapes"]:
        datasets: List[str] = data_map[dataset_type]["datasets"]
        for dataset in datasets:
            match dataset_type:
                case "shapes":
                    field: str = "geometry"
                    qualified_field = f"{field}"
                    data_abstract[qualified_field] = feature[
                        data_map["shapes"]["fields"][field]
                    ]
                case "census" | "vap" | "cvap" | "election":
                    fields: Dict[str, str] = data_map[dataset_type]["fields"]
                    i: int = 0
                    j: int = 0
                    for k, v in fields.items():
                        if dataset_type == "vap" and k == "minority_vap":
                            continue
                        if dataset_type == "cvap" and k == "minority_cvap":
                            continue
                        i += 1
                        qualified_field = f"{dataset}_{v}"
                        data_abstract[qualified_field] = 0  # Guard against missing data
                        if dataset in feature["properties"]["datasets"]:
                            data_abstract[qualified_field] = feature["properties"][
                                "datasets"
                            ][dataset][v]
                        else:
                            j += 1
                            id: str = feature["properties"]["id"]
                            print(
                                f"WARNING: Dataset {dataset} not in feature {id}'s properties! {j} of {i}"
                            )

                    if dataset_type == "vap" or dataset_type == "cvap":
                        minority_field: str = f"minority_{dataset_type}"
                        total_field: str = f"total_{dataset_type}"
                        white_field: str = f"white_{dataset_type}"
                        qualified_field = f"{dataset}_{fields[minority_field]}"
                        total: int = data_abstract[f"{dataset}_{fields[total_field]}"]
                        white: int = data_abstract[f"{dataset}_{fields[white_field]}"]
                        minority: int = total - white
                        data_abstract[qualified_field] = minority
                case _:
                    raise ValueError(f"Unknown dataset type: {dataset_type}")

    return data_abstract


def abstract_shape(
    shp_by_geoid: Dict[str, Polygon | MultiPolygon],
    neighbors_by_geoid: Dict[str, Any],
    geoid: str,
    shp: Polygon | MultiPolygon,
) -> Dict[str, Any]:
    """Abstract the shape"""

    center: Tuple[float, float] = find_center(shp)
    area: float = shp.area

    arcs: Dict[str, float] = dict()  # The shared border lengths by neighbor
    neighbors: List[str] = neighbors_by_geoid[geoid]
    perimeter: float = shp.length
    total_shared_border: float = 0.0

    for neighbor in neighbors:
        if neighbor == OUT_OF_STATE:
            continue
        if neighbor not in shp_by_geoid:
            print(f"WARNING: {neighbor} not in shapes by geoid!")
            continue

        neighbor_shp: Polygon | MultiPolygon = shp_by_geoid[neighbor]

        shared_edge = shp.intersection(neighbor_shp)
        shared_border: float = shared_edge.length

        arcs[neighbor] = shared_border
        total_shared_border += shared_border

    remaining: float = perimeter - total_shared_border
    if remaining > EPSILON:
        arcs[OUT_OF_STATE] = remaining

    ch = shp.convex_hull
    pts: List[Tuple[float, float]] = list(ch.exterior.coords)  # type: ignore

    shp_abstract: Dict[str, Any] = {
        "center": center,
        "area": area,
        "arcs": arcs,
        "exterior": pts,
    }

    return shp_abstract


def find_center(shp) -> Tuple[float, float]:
    """Get a centroid-like point guaranteed to be w/in the feature"""

    x: float = shp.centroid.x
    y: float = shp.centroid.y

    if not shp.contains(Point(x, y)):
        pt: Point = shp.representative_point()
        x: float = pt.x
        y: float = pt.y

    return x, y


def write_record(record: Any, outstream: TextIO) -> None:
    """
    Write a record as a JSONL "line" to a file

    The indent=None forces the JSON to be written on a single line
    NOTE - Don't sort the keys, i.e., keep them in the same order as specified.

    NOTE - The version in ensemble_io.py sorts the keys which breaks SCORE.sh. Not sure why.
    """

    json.dump(record, outstream, indent=None)
    outstream.write("\n")


def parse_args() -> Namespace:
    """Parse command line arguments."""

    parser: ArgumentParser = argparse.ArgumentParser(
        description="Parse command line arguments."
    )

    parser.add_argument(
        "--geojson",
        help="The input GeoJSON file",
        type=str,
    )
    parser.add_argument(
        "--data-map",
        dest="data_map",
        help="The file containing the data mapping for the input and output files",
        type=str,
    )
    parser.add_argument(
        "--graph",
        help="The adjacency graph JSON file",
        type=str,
    )
    parser.add_argument(
        "--data",
        help="The output JSON file",
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
