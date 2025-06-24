# Workflow

## How & When to Generate Adjacency Graphs

When we get shapes for a new census, we need to generate adjacency graphs.
First, create the GeoJSON files that contain the simplified shapes.
The extract adjacency graphs from those shapes.

```bash
scripts/graphs/EXTRACT-GRAPHS.py \
--states __all__ \
--version v06 \
--cycle 2020 \
--output /path/to/output/directory
```

where

- `version` is the version of the GeoJSON files
- `cycle` is the census cycle
- `output` is the directory where the output files will be saved

If the geometry for a state is not fully connected, the output file will have
"_NOT_CONNECTED" appended to the filename. The precinct locations have been squirreled
away so they can be used to find edges to add to make the graph fully connected.

For those states, e.g., AK, CA, HI, NY, and RI in the 2020 cycle, edit and run the
`scripts/graphs/FIX-GRAPHS.py` script to add the missing edges. 

## How & When to Find Precinct Neighborhoods

When we get a new census, we also need to find precinct "neighborhoods" 
for Jon Eguia & Jeff Barton's geographic advantage metric.
It's an expensive operation, so persist the results somewhere for subsequent (re)use.

```bash
scripts/geographic-baseline/NEIGHBORHOODS.py \
--version v06 \
--cycle 2020 \
--census T_20_CENS \
--neighborhoods /path/to/neighborhoods
```

where `version` and `cycle` are the same as above, and 
`census` is the name of the new census dataset.

## How & When to Precompute Geographic Baselines

Whenever we add a dataset to the app and update the GeoJSON we publish,
we should update the geographic baselines for that state, so
we can calculate geographic advantages for that election.
Use the `scripts/geographic-baseline/PRECOMPUTE.py` script to do this.