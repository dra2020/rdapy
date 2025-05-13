#!/usr/bin/env python3

"""
EXPERIMENT: FIND THE "NEIGHBORHOOD" FOR EACH PRECINCT
for Jon Eguia & Jeff Barton's geographic (central) advantage metric

It's an expensive operation, so persist the results to disk for subsequent (re)use.

For example:

$ scripts/find_nhs.py \
--ndistricts 14 \
--data testdata/examples/NC_input_data.v4.jsonl \
--graph testdata/examples/NC_graph.json > path/to/neighborhoods.jsonl

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import Any, List, Dict

import json

from rdapy import (
    load_data,
    load_graph,
)

from rdapy.score import (
    index_data,
    DistanceLedger,
    Neighbor,
    make_neighborhood,
    index_geoids,
    init_bit_array,
    set_bit,
    serialize_bits,
    deserialize_bits,
)  # TODO - Integrate with the rest of the package


def main():
    """Find neighborhoods for each precinct."""

    args = parse_arguments()

    #

    data_map: Dict[str, Any]
    input_data: List[Dict[str, Any]]
    data_map, input_data = load_data(args.data)
    adjacency_graph: Dict[str, List[str]] = load_graph(args.graph)

    data: Dict[str, Dict[str, Any]]
    geoids: List[str]
    aggs: Dict[str, int]
    data, geoids, aggs = index_data(data_map, input_data, debug=args.debug)

    target_pop: int = aggs["state_pop"] // args.ndistricts
    estimated_estimated_vote_pct: float = (
        aggs["state_dem_votes"] / aggs["state_tot_votes"]
    )

    geoid_to_index: Dict[str, int] = index_geoids(geoids)
    nprecincts: int = len(geoid_to_index)

    # Process each precinct

    dl: DistanceLedger = DistanceLedger()

    for i, geoid in enumerate(geoids):
        nh_q: List[Neighbor] = make_neighborhood(
            geoid,
            data,
            adjacency_graph,
            ledger=dl,
            size=target_pop,
            slack=args.slack,
            debug=args.debug,
        )

        indexed_nh: List[int] = [
            geoid_to_index[id] for id in [node.geoid for node in nh_q]
        ]
        nneighbors: int = len(indexed_nh)
        checksum: int = sum(indexed_nh)
        if args.debug:
            assert (
                geoid_to_index[geoid] in indexed_nh
            ), f"Missing {geoid} in neighborhood"

        bits = init_bit_array(nprecincts)
        for offset in indexed_nh:
            if args.debug:
                assert offset < len(geoids), f"Index out of range for {geoid}"
            set_bit(bits, offset, True)

        serialized_bits = serialize_bits(bits, nprecincts)
        if args.debug:
            deserialized_bits = deserialize_bits(serialized_bits)
            assert deserialized_bits == bits, f"Failed to roundtrip bits for {geoid}"

        record = {
            "geoid": geoid,
            "size": nneighbors,
            "checksum": checksum,
            "neighborhood": serialized_bits,
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
        "--graph",
        type=str,
        help="Path to graph file",
    )

    parser.add_argument(
        "--slack", type=float, default=0.00, help="How much slack to allow"
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
