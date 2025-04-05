#!/bin/bash

# Default values
GEOJSON=""
DATA_MAP=""
GRAPH=""
PLANS=""
SCORES=""
BY_DISTRICT=""

# Parse command line arguments
while [[ $# -gt 0 ]]; do
  case "$1" in
    --geojson)
      GEOJSON="$2"
      shift 2
      ;;
    --data-map)
      DATA_MAP="$2"
      shift 2
      ;;
    --graph)
      GRAPH="$2"
      shift 2
      ;;
    --plans)
      PLANS="$2"
      shift 2
      ;;
    --scores)
      SCORES="$2"
      shift 2
      ;;
    --by-district)
      BY_DISTRICT="$2"
      shift 2
      ;;
    *)
      echo "Unknown argument: $1"
      exit 1
      ;;
  esac
done

# Check if all required arguments are provided
if [[ -z "$GEOJSON" || -z "$DATA_MAP" || -z "$GRAPH" || -z "$PLANS" || -z "$SCORES" || -z "$BY_DISTRICT" ]]; then
  echo "Error: Missing required arguments"
  echo "Usage: SCORE.sh --geojson <path> --data-map <path> --graph <path> --plans <path> --scores <path> --by-district <path>"
  exit 1
fi

# Echo the required messages
echo
echo "Extracting data from ${GEOJSON} using ${DATA_MAP}..."
echo

# scripts/extract_data.py \
# --geojson testdata/data/NC_vtd_datasets.geojson \
# --data-map testdata/data/NC_data_map.json \
# --graph testdata/intermediate/NC_graph.json \
# --data temp/DEBUG_input_data.jsonl

echo
echo "Extracted graph at ${GRAPH} ..."
echo

echo
echo "Plans to be score at ${PLANS} ..."
echo

echo
echo "Aggregating data by district ..."
echo

echo
echo "Scoring plans ..."
echo

echo
echo "Writing scores to ${SCORES} and aggregates to ${BY_DISTRICT} ..."
echo

echo
echo "Done!"
echo
