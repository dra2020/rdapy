#!/usr/bin/env python3

"""
SUMMARIZE THE DISTRICT-LEVEL MMD SCORE FOR PLANS

Usage:

cat temp/LA_mmd_scores.jsonl \
| scripts/mmd/summarize_scores.py \
> temp/LA_mmd_scores.summaries.jsonl

"""

from typing import List, Dict, Any

import argparse
from argparse import ArgumentParser, Namespace

from collections import defaultdict
import csv

from rdapy import smart_read, smart_write, read_record, DEMOGRAPHICS


def main():
    """Read plans as JSONL from stdin and output data aggregated by district."""

    args = parse_arguments()

    with smart_read(args.input) as input_stream:
        with smart_write(args.output) as output_stream:
            i: int = 0
            for line in input_stream:
                record: Dict[str, Any] = read_record(line)

                assert "_tag_" in record

                assert "name" in record
                name: str = record["name"]
                plan_scores: Dict[str, Any] = {"name": record["name"]}

                assert "scores" in record
                district_scores: Dict[str, Any] = record["scores"]

                assert "census" in district_scores
                assert args.census in district_scores["census"]
                plan_scores["population_deviation"] = district_scores["census"][
                    args.census
                ]["population_deviation"]

                assert "cvap" in district_scores
                assert args.cvap in district_scores["cvap"]
                EI_matrix: List[Dict[str, float]] = district_scores["cvap"][args.cvap][
                    "EI"
                ]
                demos: List[str] = list(EI_matrix[0].keys())
                summaries: Dict[str, int] = defaultdict(int)
                for district in EI_matrix:
                    for demo in demos:
                        field: str = f"{demo}_EI"
                        summaries[field] += int(district[demo])
                    minority_EI: float = summaries.pop("minority_EI")
                    cumulative_EI: float = sum(summaries.values())
                    summaries["cumulative_EI"] = int(cumulative_EI)
                    summaries["coalition_EI"] = int(minority_EI)

                plan_scores.update(summaries)

                # Write scores in CSV format

                if i == 0:
                    cols: List[str] = list(plan_scores.keys())
                    writer: csv.DictWriter = csv.DictWriter(
                        output_stream, fieldnames=cols
                    )
                    writer.writeheader()
                writer.writerow(plan_scores)

                i += 1

    pass  # for debugging


def parse_arguments():
    """Parse command line arguments."""

    parser: ArgumentParser = argparse.ArgumentParser(
        description="Parse command line arguments."
    )

    parser.add_argument(
        "--census",
        help="The census dataset to use",
        type=str,
        default="T_20_CENS",
    )
    parser.add_argument(
        "--vap",
        help="The VAP dataset to use",
        type=str,
        default="V_20_VAP",
    )  # Not used
    parser.add_argument(
        "--cvap",
        help="The VAP dataset to use",
        type=str,
        default="V_22_CVAP",
    )

    def split_elections(s):
        return s.split(",")

    parser.add_argument(
        "--elections",
        type=split_elections,
        help="Comma-separated list of election datasets to use",
        default=["E_16-20_COMP"],  # Use `__all__` to get all elections
    )  # Not used

    parser.add_argument(
        "--input",
        type=str,
        help="The input stream -- district-level MMD scores as JSONL",
    )
    parser.add_argument(
        "--output",
        type=str,
        help="The output stream -- plan-level MMD scores as JSONL",
    )

    args: Namespace = parser.parse_args()

    return args


if __name__ == "__main__":
    main()

### END ###
