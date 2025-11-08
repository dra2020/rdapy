#!/usr/bin/env python3

"""
SUMMARIZE THE DISTRICT-LEVEL MMD SCORE FOR PLANS

Usage:

cat temp/LA_mmd_scores.jsonl \
| scripts/mmd/summarize_scores.py \
> temp/LA_mmd_scores.summaries.jsonl

"""

from typing import Any, Dict, List

import argparse
from argparse import ArgumentParser, Namespace

from rdapy import (
    load_data,
    load_graph,
    collect_metadata,
    sorted_geoids,
    smart_read,
    smart_write,
    score_mmd_plans,
)


def main():
    """Read plans as JSONL from stdin and output data aggregated by district."""

    args = parse_arguments()

    with smart_read(args.input) as input_stream:
        with smart_write(args.output) as output_stream:
            i: int = 0
            for line in input_stream:
                print(line.strip(), file=output_stream)


def parse_arguments():
    """Parse command line arguments."""

    parser: ArgumentParser = argparse.ArgumentParser(
        description="Parse command line arguments."
    )

    parser.add_argument(
        "--input",
        type=str,
        help="The input stream -- district-level MMD scores as JSONL",
    )
    parser.add_argument(
        "--output",
        type=str,
        help="The output stream -- plan-level MMD scores as JSONL",
    )

    args: Namespace = parser.parse_args()

    return args


if __name__ == "__main__":
    main()

### END ###
