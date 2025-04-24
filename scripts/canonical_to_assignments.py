#!/usr/bin/env python3

"""
CONVERT GERRYTOOLS CANONICAL FORMAT TO GEOID:DISTRICT ASSIGNMENTS
- Take in a stream of canonical plans (JSONL) and
- The associated ReCom graph, and
- Write out a stream of plans as simple dictionaries of geoid:district pairs (JSONL)

Usage:

cat testdata/plans/canonical/NC_congress_plans.canonical.jsonl \
| scripts/canonical_to_assignments.py \
--graph testdata/plans/canonical/NC_congress_recom_graph.seeded.json > temp/TEST_plans.jsonl

"""

from typing import Any, Dict, List

import argparse
from argparse import ArgumentParser, Namespace

from rdapy import (
    load_data,
    load_graph,
    collect_metadata,
    geoids_from_precinct_data,
    smart_read,
    smart_write,
    aggregate_plans,
)


def main():
    """Read canonical plans as JSONL from STDIN and output geoid:district assignments to STDOUT."""

    args = parse_arguments()

    # adjacency_graph: Dict[str, List[str]] = load_graph(args.graph)

    with smart_read(args.input) as input_stream:
        with smart_write(args.output) as output_stream:
            for line in input_stream:
                print(line, file=output_stream)
                # print(json.dumps(parsed_line), file=output_stream)


def parse_arguments():
    """Parse command line arguments."""

    parser: ArgumentParser = argparse.ArgumentParser(
        description="Parse command line arguments."
    )

    parser.add_argument(
        "--graph",
        type=str,
        help="Path to the ReCom graph file used to produce the canonical plans",
    )

    parser.add_argument(
        "--input",
        type=str,
        help="The input stream of canonical plans",
    )
    parser.add_argument(
        "--output",
        type=str,
        help="The output stream of simple geoid:district assignments",
    )

    args: Namespace = parser.parse_args()

    return args


if __name__ == "__main__":
    main()

### END ###
