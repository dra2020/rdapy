#!/bin/bash

echo "Rescoring FL ..."
scripts/experiments/RESCORE-SPLITTING.sh FL
echo

echo "Rescoring IL ..."
scripts/experiments/RESCORE-SPLITTING.sh IL
echo

echo "Rescoring MI ..."
scripts/experiments/RESCORE-SPLITTING.sh MI
echo

echo "Rescoring NC ..."
scripts/experiments/RESCORE-SPLITTING.sh NC
echo

echo "Rescoring NY ..."
scripts/experiments/RESCORE-SPLITTING.sh NY
echo

echo "Rescoring OH ..."
scripts/experiments/RESCORE-SPLITTING.sh OH
echo

# echo "Rescoring WI ..."
# scripts/experiments/RESCORE-SPLITTING.sh WI
# echo

echo "Done!"
echo