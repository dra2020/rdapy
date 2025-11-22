#!/usr/bin/env python3

"""
EXTRACT DATA & SHAPES FROM A GEOJSON FILE

$ scripts/data/extract_data.py \
--geojson testdata/examples/NC_vtd_datasets.geojson \
--data-map testdata/examples/NC_data_map.json \
--graph testdata/examples/NC_graph.json \
--data temp/TEST_input_data.jsonl

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import Any, List, Dict, TextIO

import json

from pandas import DataFrame
from geopandas import GeoDataFrame
from shapely.geometry import (
    shape,
    Polygon,
    MultiPolygon,
    Point,
)

from rdapy import smart_write, index_shapes, abstract_data, abstract_shape


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
    )  # OUTPUT

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()

    return args


if __name__ == "__main__":
    main()

### END ###
