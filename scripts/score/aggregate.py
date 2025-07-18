#!/usr/bin/env python3

"""
AGGREGATE DATA & SHAPES BY DISTRICT FOR PLANS
- Take in a stream of plans (JSONL)
- Aggregate data by district
- Write out a stream of plans with by-district aggregates (JSONL)

Usage:

cat testdata/plans/NC_congress_plans.tagged.jsonl \
| scripts/score/aggregate.py \
--state NC \
--plan-type congress \
--data testdata/examples/NC_input_data.jsonl \
--graph testdata/examples/NC_graph.json > temp/TEST_aggs.jsonl

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
    aggregate_plans,
)


def main():
    """Read plans as JSONL from stdin and output data aggregated by district."""

    args = parse_arguments()

    data_map: Dict[str, Any]
    input_data: List[Dict[str, Any]]
    data_map, input_data = load_data(args.data)
    adjacency_graph: Dict[str, List[str]] = load_graph(args.graph)

    geoids: List[str] = sorted_geoids(input_data)
    metadata: Dict[str, Any] = collect_metadata(args.state, args.plan_type, geoids)

    with smart_read(args.input) as input_stream:
        with smart_write(args.output) as output_stream:
            aggregate_plans(
                input_stream,
                output_stream,
                input_data,
                data_map,
                adjacency_graph,
                metadata,
                args.mode,
            )


def parse_arguments():
    """Parse command line arguments."""

    parser: ArgumentParser = argparse.ArgumentParser(
        description="Parse command line arguments."
    )

    parser.add_argument("--state", type=str, help="State abbreviation")
    parser.add_argument(
        "--plan-type",
        type=str,
        dest="plan_type",
        help="Plan type (e.g., congress)",
    )

    parser.add_argument(
        "--data",
        type=str,
        help="Path to input data file",
    )
    parser.add_argument(
        "--graph",
        type=str,
        help="Path to graph file",
    )
    parser.add_argument(
        "--mode",
        choices=["all", "general", "partisan", "minority", "compactness", "splitting"],
        default="all",
        help="Processing mode to use (default: normal)",
    )

    parser.add_argument(
        "--input",
        type=str,
        help="The input stream of plans -- metadata or plan",
    )
    parser.add_argument(
        "--output",
        type=str,
        help="The output stream -- metadata or plan + by-district aggregates",
    )

    args: Namespace = parser.parse_args()

    return args


if __name__ == "__main__":
    main()

### END ###
