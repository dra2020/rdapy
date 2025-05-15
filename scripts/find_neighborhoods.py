#!/usr/bin/env python3

"""
EXPERIMENT: FIND THE "NEIGHBORHOOD" FOR EACH PRECINCT
for Jon Eguia & Jeff Barton's geographic (central) advantage metric

It's an expensive operation, so persist the results to disk for subsequent (re)use.

For example:

$ scripts/find_neighborhoods.py \
--state NC \
--plan-type congress \
--data testdata/examples/NC_input_data.v4.jsonl \
--graph testdata/examples/NC_graph.json \
> temp/DEBUG_NC_congress_neighborhoods.jsonl

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import Any, List, Dict

import json

from rdapy import (
    load_data,
    load_graph,
    collect_metadata,
    sorted_geoids,
)

from rdapy.score import (
    index_data,
    get_dataset,
    DatasetKey,
    get_fields,
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

    data_by_geoid: Dict[str, Dict[str, Any]] = index_data(input_data)
    geoids: List[str] = sorted_geoids(input_data)

    metadata: Dict[str, Any] = collect_metadata(args.state, args.plan_type, geoids)
    n_districts: int = metadata["D"]

    #

    census_dataset: DatasetKey = get_dataset(data_map, "census")
    total_pop_field: str = get_fields(data_map, "census", census_dataset)["total_pop"]
    state_pop: int = sum([precinct[total_pop_field] for precinct in input_data])
    target_pop: int = state_pop // n_districts

    geoid_to_index: Dict[str, int] = index_geoids(geoids)
    nprecincts: int = len(geoid_to_index)

    # Process each precinct

    dl: DistanceLedger = DistanceLedger()

    for i, geoid in enumerate(geoids):
        nh_q: List[Neighbor] = make_neighborhood(
            geoid,
            data_by_geoid,
            total_pop_field,
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
