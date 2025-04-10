#!/usr/bin/env python3

"""
MAP SCORING DATA TO TO A GIVEN GEOJSON FILE

$ scripts/map_scoring_data.py \
--geojson ../../local/new/_NC_2020_VD_tabblock.vtd.datasets.geojson \
--data-map temp/TEST_data_map.json \

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
        help="The output JSON data map file",
        type=str,
    )
    parser.add_argument(
        "--census",
        help="The census dataset to use",
        type=str,
        default="census",
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()

    return args


if __name__ == "__main__":
    main()

### END ###
