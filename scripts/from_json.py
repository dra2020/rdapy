#!/usr/bin/env python3

"""
CONVERT AN ENSEMBLE IN LEGACY JSON FORMAT
  - JSON
  - Plans in a 'plans' list
  - Everything else is metadata 
TO THE TAGGED ASSIGNMENT-FORMAT JSONL
  - A metadata record
  - A plan record for each plan

For example:

$ scripts/from_json.py \
--input testdata/input/NC_congress_plans.legacy.json \
--output temp/TEST_plans.jsonl

-or-

$ scripts/from_json.py \
--input testdata/input/NC_congress_plans.legacy.json

For documentation, type:

$ scripts/from_json.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import Any, List, Dict

import os

from rdapy import (
    read_json,
    MetadataRecord,
    PlanRecord,
    smart_write,
    write_record,
)


def main() -> None:
    """Convert an ensemble in legacy JSON format to new uncompressed assignment format JSONL."""

    args: argparse.Namespace = parse_args()

    #

    legacy: Dict[str, Any] = read_json(os.path.expanduser(args.input))
    plans: List[Dict[str, Any]] = legacy.pop("plans")
    metadata: Dict[str, Any] = legacy

    with smart_write(args.output) as ensemble_stream:
        metadata_record: MetadataRecord = {
            "_tag_": "metadata",
            "properties": metadata,
        }
        write_record(metadata_record, ensemble_stream)

        for plan_entry in plans:
            plan_record: PlanRecord = {
                "_tag_": "plan",
                "name": plan_entry["name"],
                "plan": plan_entry["plan"],
            }
            write_record(plan_record, ensemble_stream)

    pass


def parse_args():
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Convert an ensemble in legacy JSON format to new uncompressed assignment format JSONL."
    )

    parser.add_argument(
        "--input",
        type=str,
        required=True,
        help="Ensemble of plans in legacy JSON format",
    )
    parser.add_argument(
        "--output",
        type=str,
        help="The uncompressed, tagged output JSONL file",
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()

    return args


if __name__ == "__main__":
    main()

### END ###
