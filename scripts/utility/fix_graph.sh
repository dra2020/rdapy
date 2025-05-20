#!/bin/bash

CYCLE=2020
GRAPH_PATH=~/local/adjacency-graphs
DATA_PATH=~/local/temp-data


# Check if state code argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <state_code>"
    echo "Example: $0 AK"
    exit 1
fi

# Store state code from argument
STATE=$1

scripts/utility/generate_contiguity_mods.py \
--graph ${GRAPH_PATH}/"${STATE}"_${CYCLE}_graph_NOT_CONNECTED.json \
--data ${DATA_PATH}/"${STATE}"_input_data.v4.jsonl \
> ${GRAPH_PATH}/"${STATE}"_contiguity_mods.py \

scripts/utility/apply_contiguity_mods.py \
--graph ${GRAPH_PATH}/"${STATE}"_${CYCLE}_graph_NOT_CONNECTED.json \
--mods ${GRAPH_PATH}/"${STATE}"_${CYCLE}_contiguity_mods.csv \
> ${GRAPH_PATH}/"${STATE}"_${CYCLE}_graph.json