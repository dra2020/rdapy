#!/usr/bin/env python3

"""
MAP SCORING DATA TO TO A GIVEN GEOJSON FILE

$ scripts/map_scoring_data.py \
--geojson ../../local/geojson_data/new/_NC_2020_VD_tabblock.vtd.datasets.geojson \
--data-map temp/TEST_data_map.json

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import Any, List, Dict

import json

from rdapy import smart_write


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

    data_map: Dict[str, Any] = make_map()

    print(data_map)

    # with open(args.data_map, "r") as f:
    #     data_map: Dict[str, Any] = json.load(f)

    pass


def make_map():
    """Make a data map for extracting data & shapes from a geojson file."""

    data_map: Dict[str, Any] = {
        "version": 4,
        "source": "../../local/geojson_data/new/",
        "path": "_NC_2020_VD_tabblock.vtd.datasets.geojson",
        "geoid": "id",
        "census": {"fields": {"total_pop": "Total"}, "datasets": ["T_20_CENS"]},
        "vap": {
            "fields": {
                "total_vap": "Total",
                "white_vap": "White",
                "hispanic_vap": "Hispanic",
                "black_vap": "Black",
                "native_vap": "Native",
                "asian_vap": "Asian",
                "pacific_vap": "Pacific",
                "minority_vap": "Min_derived",
            },
            "datasets": ["V_20_VAP"],
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
                "minority_cvap": "Min_derived",
            },
            "datasets": ["V_20_CVAP"],
        },
        "election": {
            "fields": {"tot_votes": "Total", "dem_votes": "Dem", "rep_votes": "Rep"},
            "datasets": [
                "E_16-20_COMP",
                "E_20_PRES",
                "E_20_GOV",
                "E_20_SEN",
                "E_16_PRES",
                "E_20_AG",
                "E_16_SEN",
            ],
        },
        "shapes": {
            "fields": {"geometry": "geometry"},
            "datasets": ["DRA_simplified_shapes"],
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
        type=str,
        default="v4",  # DRA's published geojson files
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()

    return args


if __name__ == "__main__":
    main()

### END ###
