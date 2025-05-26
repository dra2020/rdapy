#!/bin/bash

# Fix the graphs for AK, CA, HI, NY, RI

echo "Fixing the graph for AK ..."
scripts/graphs/FIX-GRAPH.sh AK

echo "Fixing the graph for CA ..."
scripts/graphs/FIX-GRAPH.sh CA

echo "Fixing the graph for HI ..."
scripts/graphs/FIX-GRAPH.sh HI

echo "Fixing the graph for NY ..."
scripts/graphs/FIX-GRAPH.sh NY

echo "Fixing the graph for RI ..."
scripts/graphs/FIX-GRAPH.sh RI

echo "Done."