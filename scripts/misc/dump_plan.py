#!/usr/bin/env python3

"""
DUMP A PLAN BY NAME TO A CSV FROM A 'TAGGED' FORMAT ENSEMBLE 
- Take in a file of uncompressed, tagged plans (JSONL), and
- A plan name
- Write a precinct-assignment file (CSV) for the given plan name

Usage:

scripts/misc/dump_plan.py \
--plans /path/to/plans.jsonl \
--csv /path/to/output.csv

"""

from typing import Any, Dict, List

import argparse
from argparse import ArgumentParser, Namespace

import os, json, sys, csv

from rdapy import smart_read


def main():
    """Dump a plan by name to a CSV."""

    args = parse_arguments()

    plans_path: str = args.plans
    plan_name: str = args.plan
    csv_path: str = args.csv

    with smart_read(os.path.expanduser(plans_path)) as input_stream:
        i: int = 0
        for line in input_stream:
            try:
                parsed_line = json.loads(line)

                if "_tag_" not in parsed_line:
                    continue

                if parsed_line["_tag_"] != "plan":
                    continue

                name: str = parsed_line["name"]
                if name != plan_name:
                    continue

                plan: List[Dict[str, Any]] = [
                    {"GEOID": str(k), "DISTRICT": int(v)}
                    for k, v in parsed_line["plan"].items()
                ]

                with open(os.path.expanduser(csv_path), "w", newline="") as csv_file:
                    for i, row in enumerate(plan):
                        if i == 0:
                            cols: List[str] = list(row.keys())
                            writer: csv.DictWriter = csv.DictWriter(
                                csv_file, fieldnames=cols
                            )
                            writer.writeheader()

                        writer.writerow(row)

                pass

            except json.JSONDecodeError as e:
                print(f"Error: Invalid JSON: {e}", file=sys.stderr)
            except Exception as e:
                print(f"Error processing record: {e}", file=sys.stderr)


def parse_arguments():
    """Parse command line arguments."""

    parser: ArgumentParser = argparse.ArgumentParser(
        description="Parse command line arguments."
    )

    parser.add_argument(
        "--plans",
        type=str,
        # required=True,
        help="Path to plans file (JSONL)",
    )
    parser.add_argument(
        "--plan",
        type=str,
        # required=True,
        help="The name of the plan to dump",
    )
    parser.add_argument(
        "--csv",
        type=str,
        # required=True,
        help="Path to output CSV file",
    )

    args: Namespace = parser.parse_args()

    return args


if __name__ == "__main__":
    main()

### END ###
