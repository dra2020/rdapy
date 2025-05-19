#!/bin/bash

# Fix the graphs for AK, CA, HI, NY, RI

echo "Fixing the graph for AK ..."
scripts/utility/fix_graph.sh AK

echo "Fixing the graph for CA ..."
scripts/utility/fix_graph.sh CA

echo "Fixing the graph for HI ..."
scripts/utility/fix_graph.sh HI

echo "Fixing the graph for NY ..."
scripts/utility/fix_graph.sh NY

echo "Fixing the graph for RI ..."
scripts/utility/fix_graph.sh RI

echo "Done."