---
layout: page
title: Extracting Contiguity Graphs
permalink: extracting-graphs/
---

In order to extract precinct data from DRA's geojson files, 
you need to first extract fully connected adjacency graphs.
For that, you need the GeoJSON files that contain simplified shapes.

### Extract graphs for each state

First run this script.
It extracts adjacency graphs from the geojsons, and 
also saves precinct locations to /tmp files that can be used to generate contiguity mods, if necessary.

```bash
scripts/graphs/EXTRACT-GRAPHS.sh
```

### Fix graphs, as necessary

Any graphs that aren't fully connected will have "_NOT_CONNECTED" appended to their filename
in the output directory.

For those states, update and run this script to fix the graphs by adding connections.

```bash
scripts/graphs/FIX-GRAPHS.sh
```

Now you're ready to extract precinct data from the geojson files.
