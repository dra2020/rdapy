#!/bin/bash

XX=$1
CHAMBER=$2

## Unzip the R75 ensemble

echo "Unzipping R75 ensemble for ${XX}/${CHAMBER} ..."
ENSEMBLE_ZIP=~/local/beta-ensembles/zipped/${XX}_${CHAMBER}.zip
UNZIP_DIR=/tmp/${XX}_${CHAMBER}

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
XZ_COMPRESSED=/tmp/${XX}_${CHAMBER}/${XX}_${CHAMBER}/${ENSEMBLE_DIR}/${ENSEMBLE_XZ}.jsonl.xz
PLANS=/tmp/${XX}_${CHAMBER}/${XX}_${CHAMBER}_R75_plans.jsonl

xz --decompress --stdout "$XZ_COMPRESSED" | bin/distill \
    --from compress \
    --to assignment \
    --output "$PLANS"

### END ###