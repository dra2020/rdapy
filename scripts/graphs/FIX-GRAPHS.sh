#!/bin/bash

CYCLE=2020
GRAPH_PATH=~/local/temp

# Fix the graphs for AK, CA, HI, NY, RI

echo "Fixing the graph for AK ..."
scripts/graphs/FIX-GRAPH.sh AK --cycle "$CYCLE" --graph-path "$GRAPH_PATH"

echo "Fixing the graph for CA ..."
scripts/graphs/FIX-GRAPH.sh CA --cycle "$CYCLE" --graph-path "$GRAPH_PATH"

echo "Fixing the graph for HI ..."
scripts/graphs/FIX-GRAPH.sh HI --cycle "$CYCLE" --graph-path "$GRAPH_PATH"

echo "Fixing the graph for NY ..."
scripts/graphs/FIX-GRAPH.sh NY --cycle "$CYCLE" --graph-path "$GRAPH_PATH"

echo "Fixing the graph for RI ..."
scripts/graphs/FIX-GRAPH.sh RI --cycle "$CYCLE" --graph-path "$GRAPH_PATH"

echo "Done."