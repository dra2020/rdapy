#!/usr/bin/env python3

"""
WRITE SCORES
- Take in a stream of scores & by-district aggregates (JSONL)
- Write the scores to a CSV file
- Write the by-district aggregates to a JSONL file
- Write the metadata to a JSONL file

Usage:

scripts/write.py \
--data testdata/intermediate/NC_input_data.jsonl \
--scores temp/DEBUG_scores.csv \
--by-district temp/DEBUG_by-district.jsonl < testdata/intermediate/NC_congress_scores.100.jsonl

-or-

cat testdata/intermediate/NC_congress_scores.100.jsonl \
| scripts/write.py \
--data testdata/intermediate/NC_input_data.jsonl \
--scores temp/DEBUG_scores.csv \
--by-district temp/DEBUG_by-district.jsonl

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import Any, List, Dict

import csv

from rdapy import (
    load_data,
    write_json,
    smart_read,
    read_record,
    smart_write,
    format_scores,
    write_record,
)


def main() -> None:
    args: argparse.Namespace = parse_args()

    data_map: Dict[str, Any]
    data_map, _ = load_data(args.data)

    metadata_path: str = args.scores.replace(".csv", "_metadata.json")
    scores_metadata: Dict[str, Any] = dict()

    i: int = 0
    with smart_read(args.input) as input_stream:
        with smart_write(args.scores) as scores_stream:
            with smart_write(args.by_district) as by_district_stream:
                for line in input_stream:
                    record: Dict[str, Any] = read_record(line)
                    assert "_tag_" in record

                    if record["_tag_"] == "metadata":
                        scores_metadata = record["properties"]
                        scores_metadata.update(data_map)
                        write_json(metadata_path, scores_metadata)
                        continue

                    assert record["_tag_"] == "scores"

                    scores: Dict[str, Any] = {"name": record["name"]}
                    scores.update(record["scores"])

                    if i == 0:
                        cols: List[str] = list(scores.keys())
                        writer: csv.DictWriter = csv.DictWriter(
                            scores_stream, fieldnames=cols
                        )
                        writer.writeheader()
                    writer.writerow(format_scores(scores))

                    aggs: Dict[str, Any] = {
                        "_tag_": "by-district",
                        "name": record["name"],
                    }
                    aggs["by-district"] = record["aggregates"]
                    write_record(aggs, by_district_stream)

                    i += 1

    pass  # for debugging


def parse_args():
    """Parse command line arguments."""

    parser: ArgumentParser = argparse.ArgumentParser(
        description="Parse command line arguments."
    )

    parser.add_argument(
        "--input",
        type=str,
        help="The input stream of plans -- metadata or plan",
    )
    parser.add_argument(
        "--data",
        type=str,
        help="Path to input data file",
    )
    parser.add_argument(
        "--scores",
        help="The path the scores CSV to write",
        type=str,
    )
    parser.add_argument(
        "--by-district",
        type=str,
        dest="by_district",
        help="The path to the by-district aggregates JSON file to write",
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()

    return args


if __name__ == "__main__":
    main()

### END ###
