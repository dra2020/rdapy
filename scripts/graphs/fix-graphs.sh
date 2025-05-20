#!/bin/bash

# Fix the graphs for AK, CA, HI, NY, RI

echo "Fixing the graph for AK ..."
scripts/graph/fix-graph.sh AK

echo "Fixing the graph for CA ..."
scripts/graph/fix-graph.sh CA

echo "Fixing the graph for HI ..."
scripts/graph/fix-graph.sh HI

echo "Fixing the graph for NY ..."
scripts/graph/fix-graph.sh NY

echo "Fixing the graph for RI ..."
scripts/graph/fix-graph.sh RI

echo "Done."