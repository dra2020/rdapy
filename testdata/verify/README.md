# Aggregation & Scoring Baselines

The data in this directory can be used to verify the correctness of *changes* to aggregation and scoring.

To verify that changes to aggregation (e.g., refactoring) product the same results, run the following command.
The resulting JSONL should not show as changed.

```bash
cat testdata/verify/LA_congress_plans.jsonl \
| 
scripts/score/aggregate.py \
--state LA \
--plan-type congress \
--data testdata/verify/LA_input_data.jsonl \
--graph testdata/verify/LA_2020_graph.json \
--mode all \
--districts-override 6 > testdata/verify/LA_mmd_aggs.jsonl
```

Similarly, to verify that changes to scoring run the following command.
Both the resulting scores CSV and the by-district JSONL should not show as changed.

```bash
cat testdata/verify/LA_mmd_aggs.jsonl \
|
scripts/mmd/score_mmd.py \
--state LA \
--plan-type congress \
--data testdata/verify/LA_input_data.jsonl \
--graph testdata/verify/LA_2020_graph.json \
--districts-override 6 \
--district-magnitude 1 \
|
scripts/score/write.py \
--data testdata/verify/LA_input_data.jsonl \
--scores testdata/verify/LA_mmd_scores.csv \
--by-district testdata/verify/LA_mmd_by-district.jsonl
```