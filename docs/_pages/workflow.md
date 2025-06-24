# Workflow

## How & When to Generate Adjacency Graphs

- scripts/graphs/EXTRACT-GRAPHS.py
- scripts/graphs/FIX-GRAPH.py <= edit
- scripts/graphs/FIX-GRAPHS.py

## How & When to Extract Data

TODO

## How & When to Find Precinct NeighborhoodsK

TODO

## How & When to Precompute Geographic Baselines

Whenever we add a dataset to the app and update the GeoJSON we publish,
we should update the geographic baselines for that state. Use the
`scripts/geographic-baseline/PRECOMPUTE.py` script to do this.