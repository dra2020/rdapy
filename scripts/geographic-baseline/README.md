# How to Pre-compute Geographic Baselines

With:

* DRA GeoJSON's in `~/local/dra-to-publish/` and
* Fully connected adjancency graphs in `~/local/adjacency-graphs/`

create data maps

```bash
scripts/geographic-baseline/MAP-DATA.sh
```

TODO - Do the graph stuff here.

and extract the data to `~/local/temp-data`.

```bash
scripts/geographic-baseline/EXTRACT-DATA.sh
```

  - FIND-NEIGHORHOODS.sh
  - CHECK-NEIGHBORHOODS.sh
  - ONCE.sh
  - report_baselines.py