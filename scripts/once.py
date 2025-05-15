#!/usr/bin/env python3

"""
DO ONE-TIME CALCULATIONS

For example:

$ scripts/once.py \
--state NC \
--plan-type congress \
--data testdata/examples/NC_input_data.v4.jsonl \
< temp/DEBUG_NC_congress_neighborhoods.jsonl \
> temp/DEBUG_NC_congress.json

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import Any, List, Dict, TextIO

import json

from rdapy import (
    load_data,
    smart_read,
    collect_metadata,
    sorted_geoids,
    calc_best_seats,
)

from rdapy.score import (
    index_data,
    get_datasets,
    get_fields,
    DatasetKey,
    calc_geographic_baseline,
)  # TODO - Integrate with the rest of the package


def main():
    """Evaluate the neighborhoods for each precinct."""

    args = parse_arguments()

    #

    data_map: Dict[str, Any]
    input_data: List[Dict[str, Any]]
    data_map, input_data = load_data(args.data)

    geoids: List[str] = sorted_geoids(input_data)
    metadata: Dict[str, Any] = collect_metadata(args.state, args.plan_type, geoids)

    n_districts: int = metadata["D"]
    election_datasets: List[DatasetKey] = get_datasets(data_map, "election")

    #

    data: Dict[str, Dict[str, Any]]
    geoids: List[str]  # NOTE - Sorted. Overwrites the above which is no longer needed.
    aggs: Dict[str, int]
    data, geoids, aggs = index_data(data_map, input_data, debug=args.debug)
    state_pop: int = aggs["state_pop"]

    # Read in the neighborhoods once

    neighborhoods: List[Dict[str, Any]] = list()
    by_dataset: Dict[str, float] = {}

    with smart_read(args.neighborhoods) as input_stream:
        for i, line in enumerate(input_stream):
            parsed_line = json.loads(line)
            neighborhoods.append(parsed_line)

    # Compute the geographic baseline for each election dataset

    for dataset in election_datasets:
        dem_votes_field: str = get_fields(data_map, "election", dataset)["dem_votes"]
        rep_votes_field: str = get_fields(data_map, "election", dataset)["rep_votes"]
        geographic_baseline: float = calc_geographic_baseline(
            neighborhoods,
            n_districts,
            state_pop,
            data,
            geoids,
            dem_votes_field,
            rep_votes_field,
        )
        by_dataset[dataset] = geographic_baseline

    record: Dict[str, Any] = {
        "geographic_baseline": by_dataset,
    }
    print(json.dumps(record))


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
        "--neighborhoods",
        type=str,
        help="The input stream of neighborhoods",
    )

    parser.add_argument("--debug", dest="debug", action="store_true", help="Debug mode")
    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()

    return args


if __name__ == "__main__":
    main()

### END ###
