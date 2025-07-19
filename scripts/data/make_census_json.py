#!/usr/bin/env python3

"""
EXTRACT THE TOTAL POPULATION FROM A CENSUS 
from DRA's DEMOGRAPHIC DATA in their vtd_data REPO
for USE IN CREATING RECOM GRAPHS

For example:

$ scripts/extract_census.py \
--source ../../local/vtd_data/2020_VTD/NC/Demographic_Data_NC.v04.zip \
--output ../vtd_data/2020_VTD/NC/NC_2020_census.json \
--no-debug

For documentation, type:

$ scripts/extract_demographic_data.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import Any, List, Dict

import os

from vtd_data import (
    require_args,
    write_json,
    convert_filename,
    zipped_csv_rows,
)


def main() -> None:
    """Extract census & demographic data from DRA's zipfile published in dra2020/vtd_data.."""

    args: Namespace = parse_args()

    csv_file: str = convert_filename(os.path.basename(args.source))
    dataset: str = "T_20_CENS"
    field_label: str = "Total"
    total_pop_field: str = f"{dataset}_{field_label}"

    # Extract the census data

    census_data: Dict[str, int] = dict()
    for row in zipped_csv_rows(args.source, csv_file):
        census_data[row[args.geoid]] = int(row[total_pop_field])

    write_json(args.output, census_data)


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Extract census data from a dra2020/vtd_data CSV file."
    )

    parser.add_argument(
        "--source",
        help="The input zip file containing the data in a CSV file",
        type=str,
    )
    parser.add_argument(
        "--output",
        help="Where to write the output JSON file",
        type=str,
    )

    parser.add_argument(
        "--cycle",
        default="2020",
        help="The redistricting cycle (e.g., 2020)",
        type=str,
    )
    parser.add_argument(
        "--geoid",
        default="GEOID20",
        help="The geoid field",
        type=str,
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    # Enable debug/explicit mode
    parser.add_argument("--debug", default=True, action="store_true", help="Debug mode")
    parser.add_argument(
        "--no-debug", dest="debug", action="store_false", help="Explicit mode"
    )

    args: Namespace = parser.parse_args()

    # Default values for args in debug mode
    debug_defaults: Dict[str, Any] = {
        "source": "../../local/vtd_data/2020_VTD/NC/Demographic_Data_NC.v04.zip",
        "output": "../vtd_data/2020_VTD/NC/NC_2020_census.json",
    }
    args = require_args(args, args.debug, debug_defaults)

    return args


if __name__ == "__main__":
    main()

### END ###
