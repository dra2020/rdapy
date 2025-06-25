---
layout: page
title: Workflow
permalink: workflow/
---

TODO

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

When we get a new census, we need to two things so we can calculate Jon Eguia & Jeff Barton's 
geographic advantage metric. 
One is find precinct "neighborhoods" for each state and chamber combination.
These only need to be found once per census cycle as neighborhods only depend on total population and precinct adjacency.

```bash
scripts/geographic-baseline/NEIGHBORHOODS.py \
--version v06 \
--cycle 2020 \
--census T_20_CENS \
--neighborhoods /path/to/neighborhoods
```

where `version` and `cycle` are the same as above, and 
`census` is the name of the new census dataset.

This is a *very* long-running script--it takes nearly 10 hours on an M4 MacBook!--so the resulting files should be saved.
Moreover, because they are quite large, neighborhoods are stored in a highly compressed and then zip'd format.

## How & When to Precompute Geographic Baselines

Once we have determined precinct neighborhoods for the census cycle, the other thing we need to do
is calculate geographic baselines for each state and chamber combination.

```bash
scripts/geographic-baseline/PRECOMPUTE.py \
--states __all__ \
--version v06 \
--cycle 2020 \
--neighborhoods /path/to/neighborhoods \
--baselines /path/to/precomputed-baselines \
--elections __all__
```

where `version` and `cycle` are the same as above.

The geographic baselines for a state then need to be updated every time a new election is available for that state.

```bash
scripts/geographic-baseline/PRECOMPUTE.py \
--states NC \
--version v06 \
--cycle 2020 \
--neighborhoods /path/to/neighborhoods \
--baselines /path/to/precomputed-baselines \
--elections __all__
```

These files should again be saved.

Right now, the only thing we precompute is geographic baselines.
Other one-time preprocessing could, however, be added to this script in the future.

You can produce a report of the geographic baselines, using this script.

```bash
scripts/geographic-baseline/report_baselines.py
```

Once geographic baselines are computed, you can use them in scoring.
