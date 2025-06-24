#!/usr/bin/env python3

"""
PRECOMPUTE BASELINES FOR SPECIFIED STATES

For example:

$ scripts/geographic-baseline/PRECOMPUTE.py \
--states __all__ \
--version v06 \
--cycle 2020 \
--neighborhoods ~/local/neighborhoods \
--baselines ~/local/precomputed \
--census T_20_CENS \
--vap V_20_VAP \
--cvap V_20_CVAP \
--elections __all__

$ scripts/geographic-baseline/PRECOMPUTE.py \
--states NC \
--version v06 \
--cycle 2020 \
--neighborhoods ~/local/neighborhoods \
--baselines ~/local/precomputed \
--census T_20_CENS \
--vap V_20_VAP \
--cvap V_20_CVAP \
--elections __all__

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import List

import os

from rdapy import DISTRICTS_BY_STATE


def main():
    """Precompute geographic baselines for all states & chambers."""

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
        print(f"Precomputing baselines for {xx} ({cycle}) ...")
        print()
        nh_dir: str = f"{args.neighborhoods}/{cycle}_VTD/{xx}"
        bl_dir: str = f"{args.baselines}/{cycle}_VTD/{xx}"

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

        # Map the data

        command: str = (
            f"""scripts/data/map_scoring_data.py \\
--geojson /tmp/{xx}/{xx}_{cycle}_VD_tabblock.vtd.datasets.geojson \\
--data-map /tmp/{xx}/{xx}_data_map.json \\
--census {args.census} \\
--vap {args.vap} \\
--cvap {args.cvap} \\
--elections {args.elections} \\
--version {version}
            """
        )
        os.system(command)

        # Extract the data

        command: str = (
            f"""scripts/data/extract_data.py \\
--geojson /tmp/{xx}/{xx}_{cycle}_VD_tabblock.vtd.datasets.geojson \\
--data-map /tmp/{xx}/{xx}_data_map.json \\
--graph /tmp/{xx}/{xx}_{cycle}_graph.json \\
--data /tmp/{xx}/{xx}_input_data.jsonl
        """
        )
        os.system(command)

        for chamber, ndistricts in DISTRICTS_BY_STATE[xx].items():
            if chamber == "congress" and ndistricts == 1:
                continue
            if ndistricts is None:
                continue

            # Precompute the baselines for the state & chamber

            command: str = (
                f"""scripts/geographic-baseline/precompute_baselines.py \\
--state {xx} \\
--plan-type {chamber} \\
--data /tmp/{xx}/{xx}_input_data.jsonl \\
< {nh_dir}/{xx}_{chamber}_neighborhoods.zip \\
> {bl_dir}/{xx}_{chamber}_precomputed.{version}.json
                """
            )
            os.system(command)
        print()

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
        "--neighborhoods",
        type=str,
        help="Directory where input neighborhood files are stored",
    )
    parser.add_argument(
        "--baselines",
        type=str,
        help="Directory where output baseline files should be stored",
    )
    parser.add_argument(
        "--cycle",
        help="The census cycle to use",
        type=str,
        default="2020",
    )

    parser.add_argument(
        "--census",
        help="The census dataset to use",
        type=str,
        default="T_20_CENS",  # Doesn't matter right now
    )
    parser.add_argument(
        "--vap",
        help="The VAP dataset to use",
        type=str,
        default="V_20_VAP",  # Doesn't matter right now
    )
    parser.add_argument(
        "--cvap",
        help="The VAP dataset to use",
        type=str,
        default="V_20_CVAP",  # Doesn't matter right now
    )

    parser.add_argument(
        "--elections",
        type=str,
        help="The election datasets to use",
        default="__all__",  # Get all elections
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
