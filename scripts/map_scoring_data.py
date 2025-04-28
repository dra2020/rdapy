#!/usr/bin/env python3

"""
MAP SCORING DATA TO TO A GIVEN GEOJSON FILE

$ scripts/map_scoring_data.py \
--geojson testdata/data/NC_vtd_datasets.v4.geojson \
--data-map temp/DEBUG_data_map.json

$ scripts/map_scoring_data.py \
--geojson testdata/data/NC_vtd_datasets.v4.geojson \
--data-map testdata/examples/NC_data_map.v4.json

NOTE -- The default datasets are for 2020 census, VAP, and CVAP data,
and the composite election dataset for 2016-2020 elections.

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import Any, List, Dict

import os, json

from rdapy import write_json


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
                if v in datasets:
                    implied_elections.append(v)

    # Get the directory and filename of the geojson file
    directory: str
    filename: str
    directory, filename = os.path.split(args.geojson)

    data_mapping: Dict[str, Any] = make_map(
        census=args.census,
        vap=args.vap,
        cvap=args.cvap,
        elections=implied_elections,
        dir=directory,
        file=filename,
        version=args.version,
    )

    write_json(args.data_map, data_mapping)

    pass  # For debugging


def make_map(
    *,
    census: str,
    vap: str,
    cvap: str,
    elections: List[str],
    dir: str,
    file: str,
    version: int,
) -> Dict[str, Any]:
    """Make a data map for extracting data & shapes from a geojson file."""

    data_map: Dict[str, Any] = {
        "version": version,
        "directory": dir,
        "file": file,
        "geoid": "id",
        "census": {"fields": {"total_pop": "Total"}, "datasets": [census]},
        "vap": {
            "fields": {
                "total_vap": "Total",
                "white_vap": "White",
                "hispanic_vap": "Hispanic",
                "black_vap": "Black",
                "native_vap": "Native",
                "asian_vap": "Asian",
                "pacific_vap": "Pacific",
                "minority_vap": "DERIVED",
            },
            "datasets": [vap],
        },
        "cvap": {
            "fields": {
                "total_cvap": "Total",
                "white_cvap": "White",
                "hispanic_cvap": "Hispanic",
                "black_cvap": "Black",
                "native_cvap": "Native",
                "asian_cvap": "Asian",
                "pacific_cvap": "Pacific",
                "minority_cvap": "DERIVED",
            },
            "datasets": [cvap],
        },
        "election": {
            "fields": {"tot_votes": "Total", "dem_votes": "Dem", "rep_votes": "Rep"},
            "datasets": elections,
        },
        "shapes": {
            "fields": {"geometry": "geometry"},
            "datasets": ["S_20_DRA"],
        },
    }

    return data_map


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
        "--version",
        help="The version # to use",
        type=int,
        default=4,  # DRA's published geojson files
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()

    return args


if __name__ == "__main__":
    main()

### END ###
