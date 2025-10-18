#!/bin/bash

XX=$1

# Get the GeoJSON for the state & unzip it

scripts/GET-GEOJSON.sh \
--state "${XX}" \
--output /tmp/"${XX}"/"${XX}"_Geojson.zip \
--version v06

scripts/UNZIP-GEOJSON.sh \
--input /tmp/"${XX}"/"${XX}"_Geojson.zip \
--output /tmp/"${XX}"

GEOJSON=/tmp/${XX}/${XX}_2020_VD_tabblock.vtd.datasets.geojson
GRAPH=/tmp/${XX}/${XX}_2020_graph.json
CENSUS="T_20_CENS"
VAP="V_20_VAP"
CVAP="V_20_CVAP"
ELECTIONS="E_16-20_COMP"

# Extract the data for scoring

DATA_MAP=$(mktemp /tmp/"${XX}"/data-map.XXXXXX)
INPUT_DATA=$(mktemp /tmp/"${XX}"/data.XXXXXX)

scripts/data/map_scoring_data.py \
--geojson "$GEOJSON" \
--census "$CENSUS" \
--vap "$VAP" \
--cvap "$CVAP" \
--elections "$ELECTIONS" \
--data-map "$DATA_MAP"

scripts/data/extract_data.py \
--geojson "$GEOJSON" \
--data-map "$DATA_MAP" \
--graph "$GRAPH" \
--data "$INPUT_DATA"

# For each chamber, unzip the ensemble file, convert the R75 ensemble.xz to assignment format, and re-score it

echo ""
CHAMBERS=("congress" "upper" "lower")
for CHAMBER in "${CHAMBERS[@]}"; do

    ## Unzip the R75 ensemble

    echo "Unzipping R75 ensemble for ${XX}/${CHAMBER} ..."
    ENSEMBLE_ZIP=~/local/beta-ensembles/zipped/${XX}_${CHAMBER}.zip
    UNZIP_DIR=/tmp/${XX}

    scripts/experiments/UNZIP-ENSEMBLE.sh --input "$ENSEMBLE_ZIP" --output "$UNZIP_DIR"

    ## Convert the xz-compressed format to assignment format

    if [ "$CHAMBER" = "congress" ]; then
        THRESHOLD="01"
    else
        THRESHOLD="05"
    fi

    echo "Converting plans to assignment format ..."

    ENSEMBLE_DIR=${XX}_${CHAMBER}_T0.${THRESHOLD}_S0.75_R0_Vcut-edges-region-aware
    ENSEMBLE_XZ=${XX}_${CHAMBER}_T0.${THRESHOLD}_S0.75_R0_Vcut-edges-region-aware_ensemble
    XZ_COMPRESSED=/tmp/${XX}/${XX}_${CHAMBER}/${ENSEMBLE_DIR}/${ENSEMBLE_XZ}.jsonl.xz
    PLANS=/tmp/${XX}/${XX}_${CHAMBER}_R75_plans.jsonl
    SCORES=/tmp/${XX}/${XX}_${CHAMBER}_R75_scores.csv

    xz --decompress --stdout "$XZ_COMPRESSED" | bin/distill \
        --from compress \
        --to assignment \
        --output "$PLANS"

    ## Re-score the ensemble

    echo "Re-scoring the ensemble ..."

    scripts/experiments/JUST-SCORE.sh \
    --state "$XX" \
    --plan-type "$CHAMBER" \
    --data "$INPUT_DATA" \
    --graph "$GRAPH" \
    --plans "$PLANS" \
    --scores "$SCORES"

done