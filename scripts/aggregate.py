#!/usr/bin/env python3
"""
Aggregate data & shapes by district

Usage: 

scripts/aggregate.py \
--state NC \
--plan-type congress \
--data testdata/NC/extracted/NC_input_data.jsonl \
--graph testdata/NC/extracted/NC_graph.json < testdata/NC/ensemble/NC_congress_plans.1K.jsonl

-or-

cat testdata/NC/ensemble/NC_congress_plans.1K.jsonl \
| scripts/aggregate.py \
--state NC \
--plan-type congress \
--data testdata/NC/extracted/NC_input_data.jsonl \
--graph testdata/NC/extracted/NC_graph.json > temp/DEBUG_OUTPUT.jsonl

-or-

time cat testdata/NC/ensemble/NC_congress_plans.1K.jsonl \
| scripts/aggregate.py \
--state NC \
--plan-type congress \
--data testdata/NC/extracted/NC_input_data.jsonl \
--graph testdata/NC/extracted/NC_graph.json > /dev/null


"""

from typing import Any, Dict, List

import argparse
import json
import sys

from rdapy import (
    load_data,
    load_graph,
    collect_metadata,
    geoids_from_precinct_data,
    aggregate_districts,
)


def main():
    """Read plans as JSONL from stdin and output data aggregated by district."""

    args = parse_arguments()

    data_map: Dict[str, Any]
    input_data: List[Dict[str, Any]]
    data_map, input_data = load_data(args.data)
    adjacency_graph = load_graph(args.graph)

    geoids: List[str] = geoids_from_precinct_data(input_data)
    metadata: Dict[str, Any] = collect_metadata(args.state, args.plan_type, geoids)

    # Process each line from stdin
    j: int = 0
    for i, line in enumerate(sys.stdin):
        try:
            # Parse the JSON string into a dictionary
            parsed_line = json.loads(line)

            # Process each input line (some of which may not be plans)
            if "_tag_" not in parsed_line and is_flat_dict(parsed_line):
                # Case 1: No "_tag_" key and simple dict - process the line as geoid:district pairs

                j += 1
                assignments = {str(k): int(v) for k, v in parsed_line.items()}
                plan_with_aggs = aggregate_districts(
                    assignments,
                    input_data,
                    adjacency_graph,
                    metadata,
                    which=args.mode,
                    data_metadata=data_map,
                )
                print(json.dumps(plan_with_aggs), file=sys.stdout)

            elif "_tag_" in parsed_line and parsed_line["_tag_"] == "plan":
                # Case 2: Has "_tag_" key with value "plan" - reset the plan to value of the "plan" key and process

                j += 1
                assignments = {str(k): int(v) for k, v in parsed_line["plan"].items()}
                plan_with_aggs = aggregate_districts(
                    assignments,
                    input_data,
                    adjacency_graph,
                    metadata,
                    which=args.mode,
                    data_metadata=data_map,
                )
                print(json.dumps(plan_with_aggs), file=sys.stdout)

            elif "_tag_" in parsed_line and parsed_line["_tag_"] == "metadata":
                # Case 3: Has "_tag_" key with value "metadata" - pass it along

                print(json.dumps(parsed_line), file=sys.stdout)
                continue

            else:
                # Case 4: Something else - skip the line, e.g., adjacency graph, etc.

                continue

            # TODO - DELETE
            if j == 1:
                break

            pass

        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON: {e}", file=sys.stderr)
        except Exception as e:
            print(f"Error processing record: {e}", file=sys.stderr)


def is_flat_dict(d: Dict[str, Any]) -> bool:
    """Is a dictionary just key:value pairs that are strings or integers?"""

    for v in d.values():
        if not (isinstance(v, int) or isinstance(v, str)):
            return False

    return True


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
        "--graph",
        type=str,
        default="testdata/NC/extracted/NC_graph.json",
        help="Path to graph file",
    )
    parser.add_argument(
        "--mode",
        choices=["all", "general", "partisan", "minority", "compactness", "splitting"],
        default="all",
        help="Processing mode to use (default: normal)",
    )

    return parser.parse_args()


if __name__ == "__main__":
    main()

### END ###
