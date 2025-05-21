#!/usr/bin/env python3

"""
EXTRACT SHAPE LOCATIONS FOR USE IN FIXING UP ADJACENCY GRAPHS

$ scripts/graphs/extract_locations.py \
--geojson /path/to/input.geojson \
--data-map /path/to/data_map.json \
> /path/to/locations.json

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import Any, Dict, Tuple

import json

from pandas import DataFrame
from geopandas import GeoDataFrame
from shapely.geometry import shape


def main() -> None:
    """Extract shape locations."""

    args: Namespace = parse_args()

    # Load the data map, the geojson file, & the adjacency graph

    with open(args.data_map, "r") as f:
        data_map: Dict[str, Any] = json.load(f)
    with open(args.geojson, "r") as f:
        geojson: Dict[str, Any] = json.load(f)

    # Index the shapes by geoid

    df: DataFrame = DataFrame([f.get("properties", {}) for f in geojson["features"]])
    gdf: GeoDataFrame = GeoDataFrame(df, geometry=[shape(f["geometry"]) for f in geojson["features"]])  # type: ignore

    # Collect the census, demographic, election, and shape data (including abstracts)

    location_by_geoid: Dict[str, Any] = dict()

    for feature in geojson["features"]:
        geoid: str = feature["properties"][data_map["geoid"]]

        # Use DRA's label coordinates as the "center" of the precinct
        center: Tuple[float, float] = (
            feature["properties"]["labelx"],
            feature["properties"]["labely"],
        )

        location_by_geoid[geoid] = center

    print(json.dumps(location_by_geoid))

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
        help="The file containing the data mapping for the input and output files",
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
