# How to Generate Contiguity Graphs

First generate fully connected adjacency graphs, then extract precinct data from geojson files.

## Extract graphs for each state

Run this script.
It saves extracts graphs from the geojsons, and 
save precinct locations to /tmp files that can be used to generate contiguity mods.

```bash
scripts/graphs/EXTRACT-GRAPHS.sh
```

## Fix graphs, as necessary

Add connections to make the graphs fully connected.
Any graphs that aren't fully connected will have "_NOT_CONNECTED" appended to their filename
in the output directory.

For those states, update and run this script to fix the graphs.

```bash
scripts/graphs/FIX-GRAPHS.sh
```

Now you're ready to extract precinct data from the geojson files.
