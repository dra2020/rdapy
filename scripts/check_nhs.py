#!/usr/bin/env python3

"""
EXPERIMENT: VERIFY THAT THE "NEIGHBORHOOD" FOR EACH PRECINCT ROUNDTRIPS

For example:

$ scripts/check_nhs.py \
--graph testdata/examples/NC_graph.json < path/to/neighborhoods.jsonl

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import Any, List, Dict

import json

from rdapy import load_graph, smart_read, OUT_OF_STATE

from rdapy.score import (
    index_geoids,
    reverse_index,
    unpack_neighborhood,
)  # TODO - Integrate with the rest of the package


def main():
    """Check that neighborhoods roundtrip properly."""

    args = parse_arguments()

    #

    adjacency_graph: Dict[str, List[str]] = load_graph(args.graph)

    geoids: List[str] = list(adjacency_graph.keys())
    if OUT_OF_STATE in geoids:
        print(f"Removing {OUT_OF_STATE} from geoids")
        geoids.remove(OUT_OF_STATE)
    geoids.sort()

    geoid_to_index: Dict[str, int] = index_geoids(geoids)
    index_to_geoid: Dict[int, str] = reverse_index(geoid_to_index)

    with smart_read(args.neighborhoods) as input_stream:
        for i, line in enumerate(input_stream):
            parsed_line = json.loads(line)

            geoid: str = parsed_line["geoid"]

            unpack_neighborhood(geoid, parsed_line, index_to_geoid, debug=True)


def parse_arguments():
    """Parse command line arguments."""

    parser: ArgumentParser = argparse.ArgumentParser(
        description="Parse command line arguments."
    )

    parser.add_argument(
        "--graph",
        type=str,
        help="Path to graph file",
    )
    parser.add_argument(
        "--neighborhoods",
        type=str,
        help="The input stream of neighborhoods",
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()

    return args


if __name__ == "__main__":
    main()

### END ###
