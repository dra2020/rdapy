#!/bin/bash

# Default values
GEOJSON=""
GRAPH=""
PLANS=""
SCORES=""
MODE="all"
CENSUS="T_20_CENS"
VAP="V_20_VAP"
CVAP="V_22_CVAP" # TODO - Change this to '24' when available
ELECTIONS="E_16-20_COMP"
EXPAND_COMPOSITES=""
DISTRICTS_OVERRIDE=""
DISTRICT_MAGNITUDE=""

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
    --census)
      CENSUS="$2"
      shift 2
      ;;
    --vap)
      VAP="$2"
      shift 2
      ;;
    --cvap)
      CVAP="$2"
      shift 2
      ;;
    --elections)
      ELECTIONS="$2"
      shift 2
      ;;
    --expand-composites)
      EXPAND_COMPOSITES="--expand-composites"
      shift 1
      ;;
    --districts-override)
      DISTRICTS_OVERRIDE="$2"
      shift 2
      ;;
    --district-magnitude)
      DISTRICT_MAGNITUDE="$2"
      shift 2
      ;;
    *)
      echo "Unknown argument: $1"
      exit 1
      ;;
  esac
done

# Check if all required arguments are provided
if [[ -z "$STATE" || -z "$PLAN_TYPE" || -z "$GEOJSON" || -z "$GRAPH" || -z "$PLANS" || -z "$SCORES" || -z "$DISTRICTS_OVERRIDE" || -z "$DISTRICT_MAGNITUDE" ]]; then
  echo "Error: Missing required arguments"
  exit 1
fi

temp_data_map=$(mktemp /tmp/data-map.XXXXXX)
temp_data=$(mktemp /tmp/data.XXXXXX)

scripts/data/map_scoring_data.py \
--geojson "$GEOJSON" \
--census "$CENSUS" \
--vap "$VAP" \
--cvap "$CVAP" \
--elections "$ELECTIONS" \
--data-map "$temp_data_map" ${EXPAND_COMPOSITES:+$EXPAND_COMPOSITES}

scripts/data/extract_data.py \
--geojson "$GEOJSON" \
--data-map "$temp_data_map" \
--graph "$GRAPH" \
--data "$temp_data"

cat "$PLANS" \
| 
scripts/score/aggregate.py \
--state "$STATE" \
--plan-type "$PLAN_TYPE" \
--data "$temp_data" \
--graph "$GRAPH" \
--mode "$MODE" \
--districts-override "$DISTRICTS_OVERRIDE" \
| 
scripts/mmd/score_mmd.py \
--state "$STATE" \
--plan-type "$PLAN_TYPE" \
--data "$temp_data" \
--graph "$GRAPH" \
--districts-override "$DISTRICTS_OVERRIDE" \
--district-magnitude "$DISTRICT_MAGNITUDE" \
> "$SCORES"

echo
echo "Done!"
echo