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

from typing import Any, List, Dict

import json

from rdapy import (
    load_data,
    smart_read,
    collect_metadata,
    geoids_from_precinct_data,
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

    geoids: List[str] = geoids_from_precinct_data(input_data)
    metadata: Dict[str, Any] = collect_metadata(args.state, args.plan_type, geoids)

    n_districts: int = metadata["D"]
    election_datasets: List[DatasetKey] = get_datasets(data_map, "election")

    #

    data: Dict[str, Dict[str, Any]]
    geoids: List[str]  # NOTE - Sorted. Overwrites the above which is no longer needed.
    aggs: Dict[str, int]
    data, geoids, aggs = index_data(data_map, input_data, debug=args.debug)
    state_pop: int = aggs["state_pop"]

    # TODO - DELETE
    # # Compute state-level values once

    # state_pop: int = aggs["state_pop"]
    # Vf: float = aggs["state_dem_votes"] / aggs["state_tot_votes"]
    # bestS: int = calc_best_seats(n_districts, Vf)

    # Add a geographic baseline to the state data

    with smart_read(args.neighborhoods) as input_stream:
        geographic_seats: float = calc_geographic_baseline(
            input_stream, n_districts, state_pop, data, geoids
        )

    record: Dict[str, Any] = {
        # "state_pop": state_pop,
        # "estimated_vote_pct": Vf,
        # "best_seats": bestS,  # Whole seats closest to proportional
        "geographic_seats": geographic_seats,
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
