---
layout: page
title: Boosting Scoring Throughput
permalink: throughput/
---

By default, the `SCORE.sh` scripts calculates all metrics ("scores") for all plans in an input ensemble.
When the ensemble is large, this can take a long time.

You can use a combination of two techniques to increase scoring throughput:

1.  "Shard" the ensemble of plans into files with fewer plans, e.g., divide it into 10 smaller files, and score the shards in parallel.
2.  Score independent categories of metrics&mdash;"general", "partisan", "minority", "compactness", and "splitting"&mdash;separately and in parallel.

When used together, you can substantially boost throughput.

Used together, the basic process is as follows:

*   Shard the ensemble of plans, e.g., into 10.
*   Score each category of metrics for each shard separately, using the `--mode` arg on `SCORE.sh`.
*   "Vertically" concatenate each set of shards back into one file of scores -or- by-district measurements for each category, and
  - Optionally, "horiztonally" join all the categories files into one overall scores or by-district file.  

There are three utility bash scripts in the `scripts` directory to support this:

*   `SHARD.sh` &ndash; e.g., `scripts/SHARD.sh /path/to/plans.jsonl`
*   `CONCAT_FILES.sh` &ndash; `scripts/CONCAT_FILES.sh /path/to/csvs "NC_congress_scores_compactness_*.csv"` or `scripts/CONCAT_FILES.sh /path/to/csvs "NC_congress_by-district_compactness_*.jsonl" --no-header`
*   `JOIN_CSVS.sh` &ndash; e.g., `scripts/JOIN_CSVS.sh /path/to/csvs "NC_congress_scores_*.csv"`

The `SCORE.sh` script takes an optional `--mode` argument to specify which category of metrics to calculate. 
The default is to calculate all categories.