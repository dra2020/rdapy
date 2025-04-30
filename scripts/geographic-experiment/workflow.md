# Workflow for Boundary Analysis Experiment

```bash
scripts/geographic-experiment/find_nhs.py > NC_precinct_neighborhoods.jsonl
```

```bash
scripts/geographic-experiment/check_nhs.py < NC_precinct_neighborhoods.jsonl
```
...


```bash
jq -s 'sort_by(.Vf) | reverse[]' NC_precinct_partisan.jsonl | jq -c '.' > NC_precinct_partisan.sorted.jsonl
```