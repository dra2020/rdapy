#!/usr/bin/env python3
"""
Aggregate data & shapes by district

Usage: 

scripts/aggregate.py \
--state NC \
--plan-type congress \
--data testdata/NC/extracted/NC_input_data.jsonl \
--data-map testdata/NC/data/NC_data_map.json \
--graph testdata/NC/extracted/NC_graph.json < testdata/NC/ensemble/NC_congress_plans.1K.jsonl

-or-

cat testdata/NC/ensemble/NC_congress_plans.1K.jsonl \
| scripts/aggregate.py \
--state NC \
--plan-type congress \
--data testdata/NC/extracted/NC_input_data.jsonl \
--data-map testdata/NC/data/NC_data_map.json \
--graph testdata/NC/extracted/NC_graph.json > temp/DEBUG_OUTPUT.jsonl

-or-

time cat testdata/NC/ensemble/NC_congress_plans.1K.jsonl \
| scripts/aggregate.py \
--state NC \
--plan-type congress \
--data testdata/NC/extracted/NC_input_data.jsonl \
--data-map testdata/NC/data/NC_data_map.json \
--graph testdata/NC/extracted/NC_graph.json > /dev/null


"""

from typing import Any, Dict, List

import argparse
import json
import sys


def main():
    """Read plans as JSONL from stdin and output data aggregated by district."""

    args = parse_arguments()

    with open(args.data_map, "r") as f:
        data_map: Dict[str, Any] = json.load(f)
    with open(args.data, "r") as f:
        input_data: List[Dict[str, Any]] = [
            json.loads(line) for line in open(args.data, "r", encoding="utf-8")
        ]
    with open(args.graph, "r") as f:
        graph: Dict[str, List[str]] = json.load(f)

    # Process each line from stdin
    for line in sys.stdin:
        try:
            # Parse the input line as JSON
            record = json.loads(line)

            # Simply print the record to stdout
            # This is the basic functionality you requested
            print(json.dumps(record))

            # For more advanced processing, you could modify the record here
            # using the auxiliary data and arguments before printing

        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON: {e}", file=sys.stderr)
        except Exception as e:
            print(f"Error processing record: {e}", file=sys.stderr)


def parse_arguments():
    """Parse command line arguments. Defaults for debugging only."""

    parser = argparse.ArgumentParser(description="Process and aggregate election data.")

    parser.add_argument("--state", type=str, default="NC", help="State abbreviation")
    parser.add_argument(
        "--plan-type",
        type=str,
        dest="plan_type",
        default="congress",
        help="Plan type (e.g., congress)",
    )
    parser.add_argument(
        "--data",
        type=str,
        default="testdata/NC/extracted/NC_input_data.jsonl",
        help="Path to input data file",
    )
    parser.add_argument(
        "--data-map",
        type=str,
        dest="data_map",
        default="testdata/NC/data/NC_data_map.json",
        help="Path to data mapping file",
    )
    parser.add_argument(
        "--graph",
        type=str,
        default="testdata/NC/extracted/NC_graph.json",
        help="Path to graph file",
    )

    return parser.parse_args()


if __name__ == "__main__":
    main()

### END ###
