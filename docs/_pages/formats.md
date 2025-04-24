---
layout: page
title: Alternative Formats
permalink: formats/
---

These are helper scripts to convert other input formats into a format that the `aggregate.py` script can consume.

#### Converting from JSON

This script takes a JSON file that has a `"plan"` key with a list of geoid:district assignment dictionaries and
produces a stream of JSON tagged records that can be input to the `aggregate.py` script.
The output is streamed to STDOUT if a file is not specified, so it can be piped into the `aggregate.py` script.
It writes the rest of the JSON properties as a metadata record.

```bash
scripts/from_json.py \
--input testdata/plans/NC_congress_plans.legacy.json
```

An example of this format can be found in `testdata/plans/` in `NC_congress_plans.legacy.json`.

#### Converting from CSV

Similarly, this script takes a list of CSV files, or a wildcard pattern for CSV files in a directory, and
synthesizes a stream of JSON tagged records.
The output is streamed to STDOUT if a file is not specified, so it can be piped into the `aggregate.py` script.

```bash
scripts/from_csvs.py \
--files testdata/plans/csvs/NC_congress.*.csv
```

An example of how this could be used are the CSV files in `testdata/plans/csvs/`.

#### Converting from GerryTools Canonical Format

Finally, this script takes the "canonical" output from GerryTools (e.g., `frcw.rs`) and 
converts it the tagged JSONL assignment format.
As with the scripts above,
the output is streamed to STDOUT if a file is not specified, so it can be piped into the `aggregate.py` script.

```bash
cat testdata/plans/canonical/NC_congress_plans.canonical.jsonl \
| scripts/canonical_to_assignments.py \
--graph testdata/plans/canonical/NC_congress_recom_graph.seeded.json
```
