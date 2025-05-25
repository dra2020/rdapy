# How to Generate Contiguity Graphs

Generate fully connected adjacency graphs before extracting precinct data from geojson files.

First, extract graphs for each state.
The script saves precinct locations in /tmp files that can be used to generate contiguity mods
to make graphs fully connected.

```bash
scripts/graphs/EXTRACT-GRAPHS.sh
```

Any graphs that aren't fully connected will have "_NOT_CONNECTED" appended to their filename
in the output directory.

```bash
scripts/graphs/CHECK-GRAPHS.sh
```

Update this to graph precinct locations into a temporary JSON file.

```bash
scripts/graphs/FIX-GRAPHS.sh
```

TODO -- WIP
