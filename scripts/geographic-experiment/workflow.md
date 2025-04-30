# Workflow for Boundary Analysis Experiment

TODO - Shrink neighborhood size to 90% of a target district size.

```bash
scripts/geographic-experiment/find_nhs.py > NC_precinct_neighborhoods.jsonl
scripts/geographic-experiment/check_nhs.py
```

```bash
scripts/geographic-experiment/check_nhs.py < NC_precinct_neighborhoods.jsonl
```

```bash
scripts/geographic-experiment/eval_nhs.py < NC_precinct_neighborhoods.jsonl > ~/local/geographic/NC_precinct_partisan.jsonl
```

```bash
jq -s 'sort_by(.Vf) | reverse[]' NC_precinct_partisan.jsonl | jq -c '.' > NC_precinct_partisan.descending.jsonl
```