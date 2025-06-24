#!/usr/bin/env python3

"""
EXTRACT ADJACENCY GRAPHYS FOR SPECIFIED STATES

For example:

$ scripts/graphs/EXTRACT-GRAPHS.py \
--states __all__ \
--version v06 \
--cycle 2020 \
--output /path/to/output/directory

$ scripts/graphs/EXTRACT-GRAPHS.py \
--states NC \
--version v06 \
--cycle 2020 \
--output /path/to/output/directory

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import List

import os


def main():
    """Extract adjacency graphs for specified states."""

    args = parse_arguments()

    states: List[str] = (
        [
            "AL",
            "AK",
            "AZ",
            "AR",
            "CA",
            "CO",
            "CT",
            "DE",
            "FL",
            "GA",
            "HI",
            "ID",
            "IL",
            "IN",
            "IA",
            "KS",
            "KY",
            "LA",
            "ME",
            "MD",
            "MA",
            "MI",
            "MN",
            "MS",
            "MO",
            "MT",
            "NE",
            "NV",
            "NH",
            "NJ",
            "NM",
            "NY",
            "NC",
            "ND",
            "OH",
            "OK",
            "OR",
            "PA",
            "RI",
            "SC",
            "SD",
            "TN",
            "TX",
            "UT",
            "VT",
            "VA",
            "WA",
            "WV",
            "WI",
            "WY",
        ]
        if args.states == ["__all__"]
        else args.states
    )

    version: str = args.version
    cycle: str = args.cycle

    #

    print()
    for xx in states:
        print(f"Extracting an adjacency graph for {xx} ({cycle}) ...")
        print()

        # Remove any existing temporary files

        command: str = f"rm /tmp/{xx}_Geojson.zip"
        os.system(command)
        command: str = f"rm -rf /tmp/{xx}"
        os.system(command)

        # Download the GeoJSON

        command: str = (
            f"scripts/GET-GEOJSON.sh --state {xx} --output /tmp/{xx}_Geojson.zip --version {version}"
        )
        os.system(command)

        # Unzip it

        command: str = (
            f"scripts/UNZIP-GEOJSON.sh --input /tmp/{xx}_Geojson.zip --output /tmp/{xx}"
        )
        os.system(command)

        # Extract the graph

        command: str = (
            f"""scripts/graphs/extract_graph.py \\
--geojson /tmp/{xx}/{xx}_{cycle}_VD_tabblock.vtd.datasets.geojson \\
--graph {args.output}/{xx}_{cycle}_graph.json \\
--locations /tmp/{xx}_precinct_locations.json
            """
        )
        os.system(command)

    pass  # for debugging


def split_list(s):
    return s.split(",")


def parse_arguments():
    """Parse command line arguments."""

    parser: ArgumentParser = argparse.ArgumentParser(
        description="Parse command line arguments."
    )

    parser.add_argument(
        "--states",
        type=split_list,
        help="Comma-separated list of states to precompute baselines for",
        default=["__all__"],
    )

    parser.add_argument(
        "--version",
        type=str,
        help="Version of the GeoJSON data to use",
    )
    parser.add_argument(
        "--cycle",
        help="The census cycle to use",
        type=str,
        default="2020",
    )
    parser.add_argument(
        "--output",
        type=str,
        help="The output directory for the adjacency graphs",
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
