# How to Generate Contiguity Graphs

Generate fully connected adjacency graphs before extracting precinct data from geojson files.

First, extract graphs for each state.
The script saves precinct locations in /tmp files that can be used to generate contiguity mods
to make graphs fully connected.

```bash
scripts/graphs/EXTRACT-GRAPHS.sh
```

Then add connections to make the graphs fully connected.
Any graphs that aren't fully connected will have "_NOT_CONNECTED" appended to their filename
in the output directory.

For those states, update and run this script to fix the graphs.

```bash
scripts/graphs/FIX-GRAPHS.sh
```

Now you're ready to extract precinct data from the geojson files.
