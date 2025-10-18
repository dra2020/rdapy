#!/bin/bash

XX=WI
CHAMBER=congress

ENSEMBLE_ZIP=~/local/beta-ensembles/zipped/${XX}_${CHAMBER}.zip
UNZIP_DIR=/tmp/beta-ensembles

XZ_COMPRESSED=/tmp/${XX}_${CHAMBER}/${XX}_${CHAMBER}.jsonl.xz
ASSIGNMENT=/tmp/${XX}_${CHAMBER}/${XX}_${CHAMBER}_assignment.jsonl

scripts/formats/UNZIP-ENSEMBLE.sh --input $ENSEMBLE_ZIP --output $UNZIP_DIR

echo "Creating a human-readable JSONL ($ASSIGNMENT) from xz-compressed ($XZ_COMPRESSED)"

xz --decompress --stdout $XZ_COMPRESSED | bin/distill \
    --from compress \
    --to assignment \
    --output $ASSIGNMENT