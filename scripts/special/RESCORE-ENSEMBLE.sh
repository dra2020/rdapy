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

# For each chamber, unzip the ensemble file, convert the R75 ensemble.xz to assignment format, and re-score it

echo ""
CHAMBERS=("congress" "upper" "lower")
for CHAMBER in "${CHAMBERS[@]}"; do

    ## Unzip the R75 ensemble

    echo "Unzipping R75 ensemble for ${XX}/${CHAMBER} ..."
    ENSEMBLE_ZIP=~/local/beta-ensembles/zipped/${XX}_${CHAMBER}.zip
    UNZIP_DIR=/tmp/${XX}

    scripts/special/UNZIP-ENSEMBLE.sh --input "$ENSEMBLE_ZIP" --output "$UNZIP_DIR"

    ## Convert the xz-compressed format to assignment format

    if [ "$CHAMBER" = "congress" ]; then
        THRESHOLD="01"
    else
        THRESHOLD="05"
    fi

    echo "Converting it to assignment format ..."
    ENSEMBLE_DIR=${XX}_${CHAMBER}_T0.${THRESHOLD}_S0.75_R0_Vcut-edges-region-aware
    ENSEMBLE_XZ=${XX}_${CHAMBER}_T0.${THRESHOLD}_S0.75_R0_Vcut-edges-region-aware_ensemble
    XZ_COMPRESSED=/tmp/${XX}/${XX}_${CHAMBER}/${ENSEMBLE_DIR}/${ENSEMBLE_XZ}.jsonl.xz
    ASSIGNMENT=/tmp/${XX}/${XX}_${CHAMBER}_R75_plans.jsonl

    xz --decompress --stdout "$XZ_COMPRESSED" | bin/distill \
        --from compress \
        --to assignment \
        --output "$ASSIGNMENT"

    ## Re-score the ensemble

    echo "TODO -- Re-scoring the ensemble ..."

done