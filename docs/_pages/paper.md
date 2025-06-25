---
layout: page
title: Scoring for the Paper
permalink: paper/
---

This is a private page that describes how to score plans for Todd & Alec's paper:
"Parameter Effects in ReCom Ensembles."

To score an ensemble, there are three steps.

First, download the DRA GeoJSON package for the state you're scoring.
For example, for North Carolina:

```bash
scripts/GET-GEOJSON.sh \
--state NC \
--output /tmp/NC_Geojson.zip \
--version v06
```

Use the `v06` version of the GeoJSONs.

Next, unzip the GeoJSON package to a temporary directory.

```bash
scripts/UNZIP-GEOJSON.sh \
--input /tmp/NC_Geojson.zip \
--output /tmp/NC
```

The unzipped GeoJSON directory will contain four files:
- A license file
- A README file
- A GeoJSON like this `NC_2020_VD_tabblock.vtd.datasets.geojson`, and
- An adjacency graphy like this `NC_2020_graph.json`

which you can use as input to the scoring scripts.

You only need to do those two steps once per state (while the temporary files are around).

Then, for each ensemble you want to score, use the `SCORE.sh` script.
It creates the data map, extracts the input data from the GeoJSON, aggregates the data by district,
scores the plans, and then outputs the scores in CSV format and the by-district aggregates as JSONL.

```bash
scripts/score/SCORE.sh \
--state NC \
--plan-type congress \
--geojson /tmp/NC/NC_2020_VD_tabblock.vtd.datasets.geojson \
--census T_20_CENS \
--vap V_20_VAP \
--cvap V_20_CVAP \
--elections E_16-20_COMP \
--graph /tmp/NC/NC_2020_graph.json \
--plans /path/to/plans.jsonl \
--scores /path/to/scores.csv \
--by-district /path/to/by-district.jsonl
```

Use these dataset keys.
There is a sample ensemble (100 plans) in `testdata/plans/NC_congress_plans.tagged.jsonl`
You can score just one category at a time with this script, e.g., 
general, partisan, minority, compactness, and splitting,
which will (obviously) produce separate sets of output files.
The default is to score all categories and produce one set. 