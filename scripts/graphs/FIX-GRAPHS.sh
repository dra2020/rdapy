#!/bin/bash

# Fix the graphs for AK, CA, HI, NY, RI

echo "Fixing the graph for AK ..."
scripts/graph/FIX-GRAPH.sh AK

echo "Fixing the graph for CA ..."
scripts/graph/FIX-GRAPH.sh CA

echo "Fixing the graph for HI ..."
scripts/graph/FIX-GRAPH.sh HI

echo "Fixing the graph for NY ..."
scripts/graph/FIX-GRAPH.sh NY

echo "Fixing the graph for RI ..."
scripts/graph/FIX-GRAPH.sh RI

echo "Done."