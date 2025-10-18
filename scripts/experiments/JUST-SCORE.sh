#!/bin/bash

# Default values
STATE=""
PLAN_TYPE=""
INPUT_DATA=""
GRAPH=""
PLANS=""
SCORES=""

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
    --data)
      INPUT_DATA="$2"
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
    *)
      echo "Unknown argument: $1"
      exit 1
      ;;
  esac
done

# Check if all required arguments are provided
if [[ -z "$STATE" || -z "$PLAN_TYPE" || -z "$INPUT_DATA" || -z "$GRAPH" || -z "$PLANS" || -z "$SCORES" ]]; then
  echo "Error: Missing required arguments"
  echo "Usage: JUST-SCORE.sh --state <xx> --plan-type <chamber> --data <path> --graph <path> --plans <path> --scores <path>"
  exit 1
fi

cat "$PLANS" \
| 
scripts/score/aggregate.py \
--state "$STATE" \
--plan-type "$PLAN_TYPE" \
--data "$INPUT_DATA" \
--graph "$GRAPH" \
--mode splitting \
| 
scripts/score/score.py \
--state "$STATE" \
--plan-type "$PLAN_TYPE" \
--data "$INPUT_DATA" \
--graph "$GRAPH" \
--mode splitting \
|
scripts/score/write.py \
--data "$INPUT_DATA" \
--scores "$SCORES" \
--by-district /dev/null 

echo
echo "Done!"
echo