#!/bin/bash

# Default values
GEOJSON=""
GRAPH=""
PLANS=""
SCORES=""
BY_DISTRICT=""
MODE="all"
CENSUS="T_20_CENS"
VAP="V_20_VAP"
CVAP="V_20_CVAP"
ELECTION="E_16-20_COMP"

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
      ELECTION="$2"
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
  echo "Optional arguments:"
  echo "  --mode <mode>         Analysis mode (default: all)"
  echo "  --census <census>     Census data to use (default: T_20_CENS)"
  echo "  --vap <vap>           Voting age population data to use (default: V_20_VAP)"
  echo "  --cvap <cvap>         Citizen voting age population data to use (default: V_20_CVAP)"
  echo "  --elections <elec>    Election data to use (default: E_16-20_COMP)"
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
--data-map "$temp_data_map" \
--census "$CENSUS" \
--vap "$VAP" \
--cvap "$CVAP" \
--elections "$ELECTION"

scripts/extract_data.py \
--geojson "$GEOJSON" \
--data-map "$temp_data_map" \
--graph "$GRAPH" \
--data "$temp_data"

# TODO - Find precinct neighborhoods
# TODO - Calculate state-level values

cat "$PLANS" \
| 
scripts/aggregate.py \
--state "$STATE" \
--plan-type "$PLAN_TYPE" \
--data "$temp_data" \
--graph "$GRAPH" \
--mode "$MODE" \
| 
scripts/score.py \
--state "$STATE" \
--plan-type "$PLAN_TYPE" \
--data "$temp_data" \
--graph "$GRAPH" \
--mode "$MODE" \
|
scripts/write.py \
--data "$temp_data" \
--scores "$SCORES" \
--by-district "$BY_DISTRICT"

echo
echo "Done!"
echo