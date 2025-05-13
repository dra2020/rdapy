#!/usr/bin/env python3

"""
EXPERIMENT: CALCULATE THE GEOGRAPHIC BASELINE
using Jon Eguia & Jeff Barton's geographic (central) advantage metric

For example:

$ scripts/calc_geographic_baseline.py \
--ndistricts 14 \
--data testdata/examples/NC_input_data.v4.jsonl < path/to/neighborhoods.jsonl > path/to/state.json

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import Any, List, Dict

import json

from rdapy import (
    load_data,
    smart_read,
    calc_best_seats,
)

from rdapy.score import (
    index_data,
    calc_geographic_baseline,
    # index_geoids,
    # reverse_index,
    # unpack_neighborhood,
    # nh_partisan_lean,
)  # TODO - Integrate with the rest of the package


def main():
    """Evaluate the neighborhoods for each precinct."""

    args = parse_arguments()

    #

    data_map: Dict[str, Any]
    input_data: List[Dict[str, Any]]
    data_map, input_data = load_data(args.data)

    data: Dict[str, Dict[str, Any]]
    geoids: List[str]
    aggs: Dict[str, int]
    data, geoids, aggs = index_data(data_map, input_data, debug=args.debug)

    # TODO - A proof of concept that state-level values can be computed once

    state_pop: int = aggs["state_pop"]
    Vf: float = aggs["state_dem_votes"] / aggs["state_tot_votes"]
    bestS: int = calc_best_seats(args.ndistricts, Vf)

    # Add a geographic baseline to the state data

    with smart_read(args.neighborhoods) as input_stream:
        geographic_seats: float = calc_geographic_baseline(
            input_stream, args.ndistricts, state_pop, data, geoids
        )

        # geoid_to_index: Dict[str, int] = index_geoids(geoids)
        # index_to_geoid: Dict[int, str] = reverse_index(geoid_to_index)

        # geographic_seats: float = 0.0

        # for i, line in enumerate(input_stream):
        #     parsed_line = json.loads(line)

        #     geoid: str = parsed_line["geoid"]

        #     neighborhood: List[str] = unpack_neighborhood(
        #         geoid, parsed_line, index_to_geoid, debug=args.debug
        #     )

        #     pop: int = data[geoid]["pop"]

        #     Vf: float
        #     fractional_seats: float
        #     whole_seats: float
        #     neighborhood: List[str]
        #     Vf, fractional_seats, whole_seats = nh_partisan_lean(neighborhood, data)

        #     proportion: float = args.ndistricts * (pop / state_pop)
        #     geographic_seats += fractional_seats * proportion

    # TODO - A proof of concept that state-level values can be computed once

    record: Dict[str, Any] = {
        "state_pop": state_pop,
        "estimated_vote_pct": Vf,
        "best_seats": bestS,  # Whole seats closest to proportional
        "geographic_seats": geographic_seats,
    }
    print(json.dumps(record))


def parse_arguments():
    """Parse command line arguments."""

    parser: ArgumentParser = argparse.ArgumentParser(
        description="Parse command line arguments."
    )

    parser.add_argument("--ndistricts", type=int, help="The number of districts")

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
