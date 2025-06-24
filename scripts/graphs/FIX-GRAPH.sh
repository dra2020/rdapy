#!/bin/bash

#!/bin/bash

# Initialize variables
CYCLE=""
GRAPH_PATH=""
STATE=""

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -c|--cycle)
            CYCLE="$2"
            shift 2
            ;;
        -g|--graph-path)
            GRAPH_PATH="$2"
            shift 2
            ;;
        -h|--help)
            echo "Usage: $0 -c <cycle> -g <graph_path> <state_code>"
            echo "  -c, --cycle       Election cycle year"
            echo "  -g, --graph-path  Path to adjacency graphs directory"
            echo "  -h, --help        Show this help message"
            echo "Example: $0 -c 2020 -g /path/to/adjacency-graphs AK"
            exit 0
            ;;
        -*)
            echo "Unknown option $1"
            exit 1
            ;;
        *)
            if [ -z "$STATE" ]; then
                STATE="$1"
            else
                echo "Too many positional arguments"
                exit 1
            fi
            shift
            ;;
    esac
done

# Check if all required arguments are provided
if [ -z "$CYCLE" ] || [ -z "$GRAPH_PATH" ] || [ -z "$STATE" ]; then
    echo "Error: Missing required arguments"
    echo "Usage: $0 -c <cycle> -g <graph_path> <state_code>"
    echo "Example: $0 -c 2020 -g /path/to/adjacency-graphs AK"
    exit 1
fi

scripts/graphs/generate_contiguity_mods.py \
--graph "${GRAPH_PATH}"/"${STATE}"_"${CYCLE}"_graph_NOT_CONNECTED.json \
--locations /tmp/"${STATE}"_precinct_locations.json \
> "${GRAPH_PATH}"/"${STATE}"_"${CYCLE}"_contiguity_mods.csv

scripts/graphs/apply_contiguity_mods.py \
--graph "${GRAPH_PATH}"/"${STATE}"_"${CYCLE}"_graph_NOT_CONNECTED.json \
--mods "${GRAPH_PATH}"/"${STATE}"_"${CYCLE}"_contiguity_mods.csv \
> "${GRAPH_PATH}"/"${STATE}"_"${CYCLE}"_graph.json