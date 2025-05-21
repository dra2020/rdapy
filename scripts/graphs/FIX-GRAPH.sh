#!/bin/bash

CYCLE=2020
GRAPH_PATH=~/local/adjacency-graphs
DATA_PATH=~/local/temp-data
VERSION=v5


# Check if state code argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <state_code>"
    echo "Example: $0 AK"
    exit 1
fi

# Store state code from argument
STATE=$1

scripts/graphs/generate_contiguity_mods.py \
--graph ${GRAPH_PATH}/"${STATE}"_${CYCLE}_graph_NOT_CONNECTED.json \
--data ${DATA_PATH}/"${STATE}"_input_data.${VERSION}.jsonl \
> ${GRAPH_PATH}/"${STATE}"_${CYCLE}_contiguity_mods.csv \

scripts/graphs/apply_contiguity_mods.py \
--graph ${GRAPH_PATH}/"${STATE}"_${CYCLE}_graph_NOT_CONNECTED.json \
--mods ${GRAPH_PATH}/"${STATE}"_${CYCLE}_contiguity_mods.csv \
> ${GRAPH_PATH}/"${STATE}"_${CYCLE}_graph.json