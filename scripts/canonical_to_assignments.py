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

import json
from collections import defaultdict

from gerrychain import Graph

from rdapy import smart_read, smart_write


def main():
    """Read canonical plans as JSONL from STDIN and output geoid:district assignments to STDOUT."""

    args = parse_arguments()

    recom_graph: Graph = Graph.from_json(args.graph)
    geoids = [
        recom_graph.nodes[node].get(args.geoid) for node in list(recom_graph.nodes())
    ]

    with smart_read(args.input) as input_stream:
        with smart_write(args.output) as output_stream:
            for line in input_stream:
                parsed_line = json.loads(line)

                name: str = parsed_line["sample"]

                districts: dict[int, set[int]] = defaultdict(set)
                for precinct, district in enumerate(parsed_line["assignment"]):
                    districts[district].add(precinct)

                assignments: dict[str, int] = {
                    geoids[index]: district
                    for district, precincts in districts.items()
                    for index in precincts
                }

                record: Dict[str, Any] = {
                    "_tag_": "plan",
                    "name": name,
                    "plan": assignments,
                }

                print(json.dumps(record), file=output_stream)


def parse_arguments():
    """Parse command line arguments."""

    parser: ArgumentParser = argparse.ArgumentParser(
        description="Parse command line arguments."
    )

    parser.add_argument(
        "--graph",
        type=str,
        required=True,
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
    parser.add_argument(
        "--geoid",
        type=str,
        default="GEOID",
        help="The geoid key in the ReCom graph",
    )

    args: Namespace = parser.parse_args()

    return args


if __name__ == "__main__":
    main()

### END ###
