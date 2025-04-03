# Workflow

## Input Files / Streams

* GeoJSON (geojson)
* Data map (JSON)
* Plans (JSONL)

## Temporary Files

* Adjacency graph (JSON)
* Precinct data (JSONL)

## Output Files

* Scores (CSV)
* By-district measures (JSONL)
* Scores metadata (JSON)

## Scripts

* extract_graph.py -- These were already extracted and came from DRA.
* extract_data.py
* aggregate.jl -- reads metadata & plans from STDIN; writes metadata & district aggregates to STDOUT
* score.jl -- reads metadata & district aggregates from STDIN; writes metadata, scores, & by-district measures to STDOUT
* to_disk.jl -- writes metadata, scores, & by-district measures to separate files

## TODO

* Pass metadata through the pipeline
* Rationalize metadata access & derivation
* Rationalize precinct data access