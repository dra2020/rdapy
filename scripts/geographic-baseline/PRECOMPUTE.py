#!/usr/bin/env python3

"""
TODO - PRECOMPUTE BASELINES FOR ALL STATES

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import List

from rdapy import DISTRICTS_BY_STATE

states: List[str] = [
    "AL",
    "AK",
    "AZ",
    "AR",
    "CA",
    "CO",
    "CT",
    "DE",
    "FL",
    "GA",
    "HI",
    "ID",
    "IL",
    "IN",
    "IA",
    "KS",
    "KY",
    "LA",
    "ME",
    "MD",
    "MA",
    "MI",
    "MN",
    "MS",
    "MO",
    "MT",
    "NE",
    "NV",
    "NH",
    "NJ",
    "NM",
    "NY",
    "NC",
    "ND",
    "OH",
    "OK",
    "OR",
    "PA",
    "RI",
    "SC",
    "SD",
    "TN",
    "TX",
    "UT",
    "VT",
    "VA",
    "WA",
    "WV",
    "WI",
    "WY",
]
states = ["NC"]


def main():
    """Precompute geographic baselines for all states & chambers."""

    args = parse_arguments()

    version: str = "v06"  # args.version
    neighborhoods_dir: str = "~/local/neighborhoods"  # args.neighborhoods
    baselines_dir: str = "~/local/precomputed"  # args.baselines

    #

    for xx, metadata in DISTRICTS_BY_STATE.items():

        # TODO - Download the GeoJSON

        # TODO - Unzip it

        # TODO - Map the data

        """
        VERSION=v5
        CENSUS=T_20_CENS
        VAP=V_20_VAP
        CVAP=V_20_CVAP
        ELECTIONS=__all__

        scripts/data/map_scoring_data.py \
        --geojson "${GEOJSON_PATH}"/_AL_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
        --data-map "${DATA_MAP_PATH}"/AL_data_map."${VERSION}".json \
        --census $CENSUS \
        --vap $VAP \
        --cvap $CVAP \
        --elections $ELECTIONS
        """

        # TODO - Extract the data

        """
        scripts/data/extract_data.py \
        --geojson "${GEOJSON_PATH}"/_AL_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
        --data-map "${DATA_MAP_PATH}"/AL_data_map."${VERSION}".json \
        --graph "${GRAPH_PATH}"/AL_"${CYCLE}"_graph.json \
        --data "${DATA_MAP_PATH}"/AL_input_data."${VERSION}".jsonl
        """

        for chamber, ndistricts in metadata.items():
            if chamber == "congress" and ndistricts == 1:
                continue
            if ndistricts is None:
                continue

            # TODO - Precompute the baselines for the state & chamber

    pass


def parse_arguments():
    """Parse command line arguments."""

    parser: ArgumentParser = argparse.ArgumentParser(
        description="Parse command line arguments."
    )

    parser.add_argument(
        "--version",
        type=str,
        help="Version of the GeoJSON data to use",
    )
    parser.add_argument(
        "--neighborhoods",
        type=str,
        help="Directory where input neighborhood files are stored",
    )
    parser.add_argument(
        "--baselines",
        type=str,
        help="Directory where output baseline files should be stored",
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
