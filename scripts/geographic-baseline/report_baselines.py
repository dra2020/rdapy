#!/usr/bin/env python3

"""
REPORT PRE-COMPUTED GEOGRAPHIC BASELINES

For example:

$ scripts/geographic-baseline/report_baselines.py \
--baseline /path/to/baselines \
--version v06 \
--cycle 2020

"""

import argparse
from argparse import ArgumentParser, Namespace

import os, json

from rdapy import DISTRICTS_BY_STATE


def main():
    """Check that neighborhoods roundtrip properly."""

    args = parse_arguments()

    #

    i: int = 0
    for xx, metadata in DISTRICTS_BY_STATE.items():
        for chamber, ndistricts in metadata.items():
            if chamber == "congress" and ndistricts == 1:
                continue
            if ndistricts is None:
                continue

            i += 1

            baseline_path: str = (
                f"{args.baselines}/{args.cycle}_VTD/{xx}/{xx}_{chamber}_precomputed.{args.version}.json"
            )

            with open(os.path.expanduser(baseline_path), "r") as f:
                baselines = json.load(f)["geographic_baseline"]

            combo: str = f"{xx}/{chamber}:"

            print(f"{combo:<16} {"Fract":>} / {"Whole":>}")
            for dataset, values in baselines.items():
                print(
                    f"  {dataset:<14} {values["fractional_seats"]:>5.2f} / {values["whole_seats"]:>5.2f}"
                )
            print()


def parse_arguments():
    """Parse command line arguments."""

    parser: ArgumentParser = argparse.ArgumentParser(
        description="Parse command line arguments."
    )

    parser.add_argument(
        "--baselines",
        type=str,
        help="Directory where the baseline files are",
    )
    parser.add_argument(
        "--version",
        type=str,
        help="Version of the GeoJSON data used for the baselines",
    )
    parser.add_argument(
        "--cycle",
        help="The census cycle to use",
        type=str,
        default="2020",
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
