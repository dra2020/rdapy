#!/usr/bin/env python3

"""
REPORT PRE-COMPUTED GEOGRAPHIC BASELINES

For example:

$ scripts/geographic-baseline/report_baselines.py

"""

import argparse
from argparse import ArgumentParser, Namespace

import os, json

from rdapy.score import DISTRICTS_BY_STATE


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
                f"~/local/geographic-baseline/{xx}_{chamber}_precomputed.json"
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

    parser.add_argument("--debug", dest="debug", action="store_true", help="Debug mode")
    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()

    return args


if __name__ == "__main__":
    main()

### END ###
