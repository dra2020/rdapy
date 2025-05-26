#!/usr/bin/env python3

"""
CREATE A TAGGED ASSIGNMENT-FORMAT JSONL FROM A LIST OF PRECINCT-ASSIGNMENT FILES (CSVS).

NOTE - This script assumes that all the CSV files are for the same state and plan type.

$ scripts/from_csvs.py \
--files testdata/plans/csvs/NC_congress.001.csv \
--output temp/TEST_plans.jsonl

-or-

$ scripts/from_csvs.py \
--files testdata/plans/csvs/NC_congress.*.csv \
--output temp/TEST_plans.jsonl

For documentation, type:

$ scripts/from_csvs.py -h

"""

import argparse

from typing import Any, Dict, List

import os
import glob
from pathlib import Path

from rdapy import (
    read_csv,
    smart_write,
    write_record,
    PlanRecord,
    MetadataRecord,
)


def main():
    """Convert one or more precinct-assignment CSVs into a tagged JSONL ensemble file."""

    args: argparse.Namespace = parse_args()

    absolute_paths = get_absolute_paths(args.files)

    ensemble_metadata: Dict[str, Any] = {"method": "From CSVs"}
    if args.state:
        ensemble_metadata["state"] = args.state
    if args.plan_type:
        ensemble_metadata["plan_type"] = args.plan_type
    ensemble_metadata["size"] = len(absolute_paths)
    ensemble_metadata["files"] = absolute_paths

    with smart_write(args.output) as ensemble_stream:
        metadata_record: MetadataRecord = {
            "_tag_": "metadata",
            "properties": ensemble_metadata,
        }
        write_record(metadata_record, ensemble_stream)

        for plan_path in absolute_paths:
            plan_csv: List[Dict[str, int]] = read_csv(plan_path, [str, int])
            assignments: Dict[str, int] = invert_plan(plan_csv)

            filename = Path(plan_path).name
            plan_record: PlanRecord = {
                "_tag_": "plan",
                "name": filename,
                "plan": assignments,
            }
            write_record(plan_record, ensemble_stream)


def get_absolute_paths(file_paths):
    """Convert relative paths to absolute paths and expand wildcards."""

    expanded_paths = []
    for path in file_paths:
        # Expand any wildcards in the path
        matched_paths = glob.glob(path)
        if matched_paths:
            # If the pattern matched any files, add them all
            expanded_paths.extend(matched_paths)
        else:
            # If no files matched, keep the original path (it will fail later if the file doesn't exist)
            expanded_paths.append(path)

    # Convert to absolute paths
    return [os.path.abspath(path) for path in expanded_paths]


def invert_plan(plan_csv: List[Dict[str, int]]) -> Dict[str, int]:
    """Convert a preinct-assignment CSV into a dictionary of precincts and districts."""

    geoid_fields: List[str] = ["GEOID", "GEOID20", "GEOID30"]
    district_fields: List[str] = ["District", "DISTRICT"]

    keys: List[str] = list(plan_csv[0].keys())

    geoid_field: str = list(set(geoid_fields) & set(keys))[0]
    district_field: str = list(set(district_fields) & set(keys))[0]

    return {str(row[geoid_field]): int(row[district_field]) for row in plan_csv}


def parse_args():
    parser = argparse.ArgumentParser(
        description="Make an ensemble from a list of precinct-assignment files."
    )
    parser.add_argument(
        "--state",
        help="An optional two-character state code (e.g., NC)",
        type=str,
    )
    parser.add_argument(
        "--plan-type",
        type=str,
        help="An optional type of districts (congress, upper, lower)",
    )
    parser.add_argument(
        "-f",
        "--files",
        nargs="+",
        required=True,
        help="One or more relative file paths to precinct-assignment files (CSVs).",
    )
    parser.add_argument(
        "--output",
        type=str,
        help="The uncompressed, tagged output JSONL file",
    )

    args = parser.parse_args()

    return args


if __name__ == "__main__":
    main()

### END ###
