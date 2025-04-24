---
layout: page
title: Alternative Formats
permalink: formats/
---

TODO

Two helper scripts make it easy to use other input formats, instead of the two described above.

This script takes a JSON file that has a `"plan"` key with a list of geoid:district assignment dictionaries and
produces a stream of JSON tagged records that can be input to the `aggregate.py` script.

```bash
scripts/from_json.py \
--input testdata/plans/NC_congress_plans.legacy.json
```

An example of this format can be found in `testdata/plans/` in `NC_congress_plans.legacy.json`.

Similarly, this script takes a list of CSV files, or a wildcard pattern for CSV files in a directory, and
synthesizes a stream of JSON tagged records that can be input to the `aggregate.py` script.

```bash
scripts/from_csvs.py \
--files testdata/plans/csvs/NC_congress.*.csv
```

An example of this are the CSV files in `testdata/plans/csvs/`.
