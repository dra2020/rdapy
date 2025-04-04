#!/bin/bash

# Default values
GEOJSON=""
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
if [[ -z "$GEOJSON" || -z "$GRAPH" || -z "$PLANS" || -z "$SCORES" || -z "$BY_DISTRICT" ]]; then
  echo "Error: Missing required arguments"
  echo "Usage: SCORE.sh --geojson <path> --graph <path> --plans <path> --scores <path> --by-district <path>"
  exit 1
fi

# Echo the required messages
echo
echo "Extracting data from ${GEOJSON} ..."
echo "Extracted graph at ${GRAPH} ..."
echo "Plans to be score at ${PLANS} ..."
echo "Aggregating data by district ..."
echo "Scoring plans ..."
echo "Writing scores to ${SCORES}..."
echo "Writing aggregates to ${BY_DISTRICT} ..."
echo "Done!"
echo
