#!/usr/bin/env python3

"""
SCORE MMD PLANS
- Take in a stream of plans & by-district aggregates (JSONL)
- Score each plan
- Write out a stream of scores along with by-district aggregates (JSONL)


Usage:

cat testdata/examples/NC_congress_aggs.100.jsonl \
| scripts/mmd/score_mmd.py \
--state NC \
--plan-type congress \
--data testdata/examples/NC_input_data.jsonl \
--graph testdata/examples/NC_graph.json > temp/TEST_scores.jsonl \
--districts 2 \
--magnitude 4

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

    data_map: Dict[str, Any]
    input_data: List[Dict[str, Any]]
    data_map, input_data = load_data(args.data)
    adjacency_graph: Dict[str, List[str]] = load_graph(args.graph)

    geoids: List[str] = sorted_geoids(input_data)
    metadata: Dict[str, Any] = collect_metadata(
        args.state, args.plan_type, geoids, districts_override=args.districts_override
    )

    with smart_read(args.input) as input_stream:
        with smart_write(args.output) as output_stream:
            score_mmd_plans(
                input_stream,
                output_stream,
                input_data,
                data_map,
                adjacency_graph,
                metadata,
                n_districts=args.districts_override,  # args.n_districts,
                district_magnitude=args.district_magnitude,
            )


def parse_arguments():
    """Parse command line arguments."""

    parser: ArgumentParser = argparse.ArgumentParser(
        description="Parse command line arguments."
    )

    parser.add_argument("--state", type=str, default="LA", help="State abbreviation")
    parser.add_argument(
        "--plan-type",
        type=str,
        dest="plan_type",
        default="lower",
        help="Plan type (e.g., congress)",
    )

    parser.add_argument(
        "--data",
        type=str,
        default="testdata/examples/NC_input_data.jsonl",  # TODO
        help="Path to input data file",
    )
    parser.add_argument(
        "--graph",
        type=str,
        default="testdata/examples/NC_graph.json",  # TODO
        help="Path to graph file",
    )

    # For MMD experiments
    parser.add_argument(
        "--districts-override",
        type=int,
        dest="districts_override",
        help="Number of districts to use for aggregation (overrides metadata)",
    )
    parser.add_argument(
        "--district-magnitude",
        type=int,
        default=4,
        dest="district_magnitude",
        help="Number of seats per district",
    )

    parser.add_argument(
        "--input",
        type=str,
        help="The input stream -- metadata or plan + by-district aggregates",
    )
    parser.add_argument(
        "--output",
        type=str,
        help="The output stream -- metadata or plan + scores + by-district aggregates",
    )

    args: Namespace = parser.parse_args()

    return args


if __name__ == "__main__":
    main()

### END ###
