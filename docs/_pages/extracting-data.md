---
layout: page
title: Extracting Data
permalink: extracting-data/
---

With fully connected adjacency graphs in hand, you can extract precinct data 
for scoring from the DRA geojson files.

### Create data maps

```bash
scripts/data/MAP-DATA.sh
```

### Extract data from geojson files

```bash
scripts/data/EXTRACT-DATA.sh
```

Now the data are extracted from the geojson files and are ready to use for scoring.