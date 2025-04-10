#!/bin/bash

# Default values
GEOJSON=""
GRAPH=""
PLANS=""
SCORES=""
BY_DISTRICT=""
MODE="all"

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
    --mode)
      MODE="$2"
      shift 2
      ;;
    *)
      echo "Unknown argument: $1"
      exit 1
      ;;
  esac
done

# Check if all required arguments are provided
if [[ -z "$STATE" || -z "$PLAN_TYPE" || -z "$GEOJSON" || -z "$GRAPH" || -z "$PLANS" || -z "$SCORES" || -z "$BY_DISTRICT" ]]; then
  echo "Error: Missing required arguments"
  echo "Usage: SCORE.sh --state <xx> --plan-type <chamber> --geojson <path> --graph <path> --plans <path> --scores <path> --by-district <path>"
  exit 1
fi

# Validate the mode argument
valid_modes=("all" "general" "partisan" "minority" "compactness" "splitting")
is_valid_mode=false

for valid_mode in "${valid_modes[@]}"; do
  if [[ "$MODE" == "$valid_mode" ]]; then
    is_valid_mode=true
    break
  fi
done

if [[ "$is_valid_mode" == false ]]; then
  echo "Error: Invalid mode '$MODE'. Must be one of: all, general, partisan, minority, compactness, splitting"
  exit 1
fi

temp_data_map=$(mktemp /tmp/data-map.XXXXXX)
temp_data=$(mktemp /tmp/data.XXXXXX)

scripts/map_scoring_data.py \
--geojson "$GEOJSON" \
--data-map "$temp_data_map"

scripts/extract_data.py \
--geojson "$GEOJSON" \
--data-map "$temp_data_map" \
--graph "$GRAPH" \
--data temp/TEST_input_data.jsonl

echo
echo "Done!"
echo
