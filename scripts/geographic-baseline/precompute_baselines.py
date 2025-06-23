#!/usr/bin/env python3

"""
PRECOMPUTE ONE-TIME CALCULATIONS

For example:

$ scripts/geographic-baseline/once.py \
--state NC \
--plan-type congress \
--data testdata/examples/NC_input_data.jsonl \
< testdata/examples/NC_congress_neighborhoods.jsonl \
> temp/TEST_precomputed.json

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import Any, List, Dict

import json

from rdapy import (
    load_data,
    smart_read,
    collect_metadata,
    sorted_geoids,
    index_data,
    get_dataset,
    get_datasets,
    get_fields,
    DatasetKey,
    index_geoids,
    reverse_index,
    unpack_neighborhood,
    calc_geographic_baseline,
)


def main():
    """Evaluate the neighborhoods for each precinct."""

    args = parse_arguments()

    #

    data_map: Dict[str, Any]
    input_data: List[Dict[str, Any]]
    data_map, input_data = load_data(args.data)

    #

    geoids: List[str] = sorted_geoids(input_data)
    metadata: Dict[str, Any] = collect_metadata(args.state, args.plan_type, geoids)
    n_districts: int = metadata["D"]

    census_dataset: DatasetKey = get_dataset(data_map, "census")
    total_pop_field: str = get_fields(data_map, "census", census_dataset)["total_pop"]
    state_pop: int = sum([precinct[total_pop_field] for precinct in input_data])

    election_datasets: List[DatasetKey] = get_datasets(data_map, "election")

    data_by_geoid: Dict[str, Dict[str, Any]] = index_data(input_data)

    # Read in & unpack the neighborhoods once

    neighborhoods: List[Dict[str, Any]] = list()
    geoid_to_index: Dict[str, int] = index_geoids(geoids)
    index_to_geoid: Dict[int, str] = reverse_index(geoid_to_index)

    with smart_read(args.neighborhoods) as input_stream:
        for i, line in enumerate(input_stream):
            parsed_line = json.loads(line)

            geoid: str = parsed_line["geoid"]
            neighborhood: List[str] = unpack_neighborhood(
                geoid, parsed_line, index_to_geoid, debug=args.debug
            )
            neighborhoods.append({"geoid": geoid, "neighborhood": neighborhood})

    # Compute the geographic baseline for each election dataset

    by_dataset: Dict[str, Any] = {}
    for dataset in election_datasets:
        dem_votes_field: str = get_fields(data_map, "election", dataset)["dem_votes"]
        rep_votes_field: str = get_fields(data_map, "election", dataset)["rep_votes"]

        fractional_seats: float
        whole_seats: float
        fractional_seats, whole_seats = calc_geographic_baseline(
            neighborhoods,
            n_districts,
            state_pop,
            data_by_geoid,
            geoids,
            total_pop_field,
            dem_votes_field,
            rep_votes_field,
        )

        by_dataset[dataset] = {
            "fractional_seats": fractional_seats,
            "whole_seats": whole_seats,
        }

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
