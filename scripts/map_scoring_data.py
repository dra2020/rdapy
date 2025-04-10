#!/usr/bin/env python3

"""
MAP SCORING DATA TO TO A GIVEN GEOJSON FILE

$ scripts/map_scoring_data.py \
--geojson ../../local/new/_NC_2020_VD_tabblock.vtd.datasets.geojson \
--data-map temp/TEST_data_map.json \

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import Any, List, Dict

import json, contextlib, os, sys

from pandas import DataFrame

from rdapy import smart_write

EPSILON: float = 1.0e-12
OUT_OF_STATE: str = "OUT_OF_STATE"


def main() -> None:
    """Extract census, demographic, election, and shape data from DRA's .geojson file."""

    args: Namespace = parse_args()

    input_elections: List[str] = (
        args.elections
        if isinstance(args.elections, list)
        else args.elections.split(",")
    )

    # Load the geojson

    with open(args.geojson, "r") as f:
        geojson: Dict[str, Any] = json.load(f)

    # Grab the datasets

    datasets: Dict[str, Any] = geojson["datasets"]

    # Expand the composite elections specified to include the constituent elections

    implied_elections: List[str] = input_elections.copy()
    for e in input_elections:
        if "members" in datasets[e]:
            for k, v in datasets[e]["members"].items():
                implied_elections.append(v)

    # with open(args.data_map, "r") as f:
    #     data_map: Dict[str, Any] = json.load(f)

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
        default="T_20_CENS",
    )
    parser.add_argument(
        "--vap",
        help="The VAP dataset to use",
        type=str,
        default="V_20_VAP",
    )
    parser.add_argument(
        "--cvap",
        help="The VAP dataset to use",
        type=str,
        default="V_20_CVAP",
    )
    parser.add_argument(
        "--elections",
        type=lambda s: s.split(","),
        help="Comma-separated list of election datasets to use",
        default=["E_16-20_COMP"],
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()

    return args


if __name__ == "__main__":
    main()

### END ###
