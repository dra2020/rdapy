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
    --state)
      STATE="$2"
      shift 2
      ;;
    --plan-type)
      PLAN_TYPE="$2"
      shift 2
      ;;
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
if [[ -z "$STATE" || -z "$PLAN_TYPE" || -z "$GEOJSON" || -z "$DATA_MAP" || -z "$GRAPH" || -z "$PLANS" || -z "$SCORES" || -z "$BY_DISTRICT" ]]; then
  echo "Error: Missing required arguments"
  echo "Usage: SCORE.sh --state <xx> --plan-type <chamber> --geojson <path> --data-map <path> --graph <path> --plans <path> --scores <path> --by-district <path>"
  exit 1
fi


temp_data=$(mktemp /tmp/data.XXXXXX)

scripts/extract_data.py \
--geojson "$GEOJSON" \
--data-map "$DATA_MAP" \
--graph "$GRAPH" \
--data "$temp_data"

cat "$PLANS" \
| scripts/aggregate.py \
--state "$STATE" \
--plan-type "$PLAN_TYPE" \
--data "$temp_data" \
--graph "$GRAPH" 

echo
echo "Scoring plans ..."
echo

echo
echo "Writing scores to ${SCORES} and aggregates to ${BY_DISTRICT} ..."
echo

echo
echo "Done!"
echo
