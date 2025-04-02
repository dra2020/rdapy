#!/usr/bin/env python3

"""
SCORE AN ENSEMBLE OF MAPS

For example:

v3 data:

$ scripts/score_ensemble.py \
--state NC \
--plan-type congress \
--plans testdata/ensemble/NC20C_plans_SAMPLE_100.jsonl \
--data ../vtd_data/2020_VTD/NC/NC_input_data.v3.jsonl \
--scores temp/TEST_scores.csv \
--by-district temp/TEST_by-district.jsonl \
--log temp/TEST_scores_log.txt \
--no-debug

v2 data:

$ scripts/score_ensemble.py \
--state NC \
--plan-type congress \
--plans testdata/ensemble/NC20C_plans_SAMPLE_100.jsonl \
--data ../vtd_data/2020_VTD/NC/NC_input_data.v2.jsonl \
--scores temp/NC20C_scores_all.csv \
--by-district temp/NC20C_by-district_all.jsonl \
--log temp/NC20C_scores_all_log.txt \
--no-debug

v1 data:

$ scripts/score_ensemble.py \
--state NC \
--plan-type congress \
--plans testdata/ensemble/NC20C_plans_SAMPLE_100.jsonl \
--data ../vtd_data/2020_VTD/NC/NC_input_data.v1.jsonl \
--scores temp/NC20C_scores_all.csv \
--by-district temp/NC20C_by-district_all.jsonl \
--log temp/NC20C_scores_all_log.txt \
--no-debug


For documentation, type:

$ scripts/score_ensemble.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace
from typing import Any, List, Dict, OrderedDict

import os, csv
from collections import OrderedDict

from rdapy import (
    unpack_input_data,
    geoids_from_precinct_data,
    collect_metadata,
    write_json,
    smart_read,
    read_record,
    smart_write,
    format_scores,
    capture_warnings,
    MetadataRecord,
    write_record,
    score_ensemble,
)


def main() -> None:
    args: argparse.Namespace = parse_args()

    if args.verbose:
        print("args:", args)

    input_metadata: Dict[str, Any]
    precinct_data: List[Dict[str, Any]]
    adjacency_graph: Dict[str, List[str]]
    input_metadata, precinct_data, adjacency_graph = unpack_input_data(args.data)
    geoids: List[str] = geoids_from_precinct_data(precinct_data)
    metadata: Dict[str, Any] = collect_metadata(args.state, args.plan_type, geoids)

    # Read the ensemble metadata & write the scores metadata
    with smart_read(args.plans) as ensemble_stream:
        line = ensemble_stream.readline()
        record: Dict[str, Any] = read_record(line)
        assert record["_tag_"] == "metadata"
        scores_metadata: Dict[str, Any] = record["properties"]
        scores_metadata.update(input_metadata)

    metadata_path: str = args.scores.replace(".csv", "_metadata.json")
    write_json(metadata_path, scores_metadata)

    # Score the plans in the ensemble
    with smart_read(args.plans) as ensemble_stream:
        with open(os.path.expanduser(args.log), "w") as log_stream:
            with capture_warnings(log_stream) as handler:
                scores_records: List[OrderedDict[str, Any]]
                by_district_records: List[Dict[str, Any]]
                scores_records, by_district_records = score_ensemble(
                    ensemble_stream,
                    precinct_data,
                    adjacency_graph,
                    metadata,
                    which=args.mode,
                    data_metadata=input_metadata,
                    verbose=args.verbose,
                )

    # Write the per-plan scores to a CSV file
    with smart_write(args.scores) as scores_stream:
        for i, record in enumerate(scores_records):
            try:
                if i == 0:
                    cols: List[str] = list(record.keys())
                    writer: csv.DictWriter = csv.DictWriter(
                        scores_stream, fieldnames=cols
                    )
                    writer.writeheader()

                writer.writerow(format_scores(record))
            except Exception as e:
                print(f"Exception writing scores: {e}")
                print(f"Mode: {args.mode}, columns: {cols}")
                print(f"Record {i}: {record}")

    # Write by_district_records to a JSON file
    with smart_write(args.by_district) as by_district_stream:
        # Write the scores metadata record to the by-district file
        metadata_record: MetadataRecord = {
            "_tag_": "metadata",
            "properties": scores_metadata,
        }
        write_record(metadata_record, by_district_stream)

        for plan in by_district_records:
            record: Dict[str, Any] = {
                "_tag_": "by-district",
                "name": plan["map"],
                "by-district": plan["by-district"],
            }
            write_record(record, by_district_stream)

    pass


def parse_args():
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Score an ensemble of plans. Defaults are for debugging only."
    )

    parser.add_argument(
        "--state",
        help="The two-character state code (e.g., NC)",
        type=str,
        default="NC",
    )
    parser.add_argument(
        "--plan-type",
        type=str,
        dest="plan_type",
        help="The type of districts (congress, upper, lower)",
        default="congress",
    )
    parser.add_argument(
        "--plans",
        type=str,
        help="Ensemble of plans to score in a JSON file",
        default="testdata/ensemble/NC20C_plans_SAMPLE_100.jsonl",
    )
    parser.add_argument(
        "--data",
        type=str,
        help="The input data JSON file",
        default="../vtd_data/2020_VTD/NC/NC_input_data.v3.jsonl",
    )
    parser.add_argument(
        "--scores",
        type=str,
        help="The output scores CSV file",
        default="temp/TEST_scores.csv",
    )
    parser.add_argument(
        "--by-district",
        type=str,
        dest="by_district",
        help="The by-district aggregates JSON file",
        default="temp/TEST_by-district.jsonl",
    )
    parser.add_argument(
        "--log",
        type=str,
        help="Log TXT file",
        default="temp/TEST_scores_log.txt",
    )
    parser.add_argument(
        "--mode",
        choices=["all", "general", "partisan", "minority", "compactness", "splitting"],
        default="all",
        help="Processing mode to use (default: normal)",
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()

    return args


if __name__ == "__main__":
    main()

### END ###
