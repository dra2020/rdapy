#!/bin/bash

python3 graph/recom_graph.py \
--data ../vtd_data/2020_VTD/NC/NC_2020_census.json \
--graph ../vtd_data/2020_VTD/NC/NC_2020_graph.json \
--output ~/Downloads/NC20C_recom_graph.unseeded.json

python3 seeding/partition.py \
--input ~/Downloads/NC20C_recom_graph.unseeded.json \
--output ~/Downloads/NC20C_recom_graph.seeded.json \
--N 14 \
--epsilon 0.01 \
--pop_col TOTAL_POP \
--surcharge COUNTY=0.0 \
--random_spanning kruskal

python3 scripts/ensemble_metadata.py \
--state NC \
--plan-type congress \
--sample-size 100 \
--sample-rate 1 \
--offset 0 \
--recom-graph ~/Downloads/NC20C_recom_graph.seeded.json \
--data ../vtd_data/2020_VTD/NC/NC_input_data.jsonl \
--output ~/Downloads/NC20C_recom_metadata.jsonl

python3 scripts/frcw_ensemble.py --metadata ~/Downloads/NC20C_recom_metadata.jsonl --no-debug > ~/Downloads/NC_congress_plans.canonical.jsonl