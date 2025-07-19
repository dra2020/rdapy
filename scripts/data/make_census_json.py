#!/usr/bin/env python3

"""
MAKE A GEOID:POPULATION JSON FILE
from the JSONL data extracted from a DRA GeoJSON file 

This is a helper script so that other legacy scripts don't need to be modified.

For example:

$ scripts/data/make_census_json.py \
--input /path/to/input_data.jsonl \
--output /path/to/output/census.json 

For documentation, type:

$ scripts/data/make_census_json.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import Any, List, Dict

import os

from rdapy import load_data, write_json


def main() -> None:
    """Make a census.json file from the JSONL input data for a state."""

    args: Namespace = parse_args()

    data_map: Dict[str, Any]
    input_data: List[Dict[str, Any]]
    data_map, input_data = load_data(args.input)

    total_pop_field: str = f"{args.dataset}_{args.field}"
    pop_by_geoid: Dict[str, int] = dict()
    for row in input_data:
        geoid: str = row["geoid"]
        pop: int = row[total_pop_field]
        pop_by_geoid[geoid] = pop

    write_json(args.output, pop_by_geoid)


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Parse command line arguments."
    )

    parser.add_argument(
        "--input",
        help="The JSONL input data file",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--output",
        help="The output JSON file",
        type=str,
        required=True,
    )

    parser.add_argument(
        "--dataset",
        type=str,
        default="T_20_CENS",
        help="The input JSONL file",
    )
    parser.add_argument(
        "--field",
        type=str,
        default="Total",
        help="The total population census field",
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()

    return args


if __name__ == "__main__":
    main()

### END ###
