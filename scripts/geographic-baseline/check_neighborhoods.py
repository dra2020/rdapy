#!/usr/bin/env python3

"""
EXPERIMENT: VERIFY THAT THE "NEIGHBORHOOD" FOR EACH PRECINCT ROUNDTRIPS

For example:

$ scripts/geographic-baseline/check_neighborhoods.py \
--data testdata/examples/NC_input_data.v4.jsonl \
< temp/DEBUG_NC_congress_neighborhoods.jsonl

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import List, Dict, Any

import json

from rdapy import load_data, sorted_geoids, smart_read, OUT_OF_STATE

from rdapy.score import (
    index_geoids,
    reverse_index,
    unpack_neighborhood,
)  # TODO - Integrate with the rest of the package


def main():
    """Check that neighborhoods roundtrip properly."""

    args = parse_arguments()

    #

    data_map: Dict[str, Any]
    input_data: List[Dict[str, Any]]
    data_map, input_data = load_data(args.data)

    #

    geoids: List[str] = sorted_geoids(input_data)

    geoid_to_index: Dict[str, int] = index_geoids(geoids)
    index_to_geoid: Dict[int, str] = reverse_index(geoid_to_index)

    with smart_read(args.neighborhoods) as input_stream:
        for i, line in enumerate(input_stream):
            parsed_line = json.loads(line)

            geoid: str = parsed_line["geoid"]

            unpack_neighborhood(geoid, parsed_line, index_to_geoid, debug=args.debug)


def parse_arguments():
    """Parse command line arguments."""

    parser: ArgumentParser = argparse.ArgumentParser(
        description="Parse command line arguments."
    )

    parser.add_argument(
        "--data",
        type=str,
        help="Path to input data file",
    )
    parser.add_argument(
        "--neighborhoods",
        type=str,
        help="The input stream of neighborhoods",
    )

    parser.add_argument("--debug", dest="debug", action="store_true", help="Debug mode")
    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()

    return args


if __name__ == "__main__":
    main()

### END ###
