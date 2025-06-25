---
layout: page
title: Scoring for the Paper
permalink: paper/
---

TODO

scripts/GET-GEOJSON.sh \
--state NC \
--output /tmp/NC_Geojson.zip \
--version v06

scripts/UNZIP-GEOJSON.sh \
--input /tmp/NC_Geojson.zip \
--output /tmp/NC

scripts/score/SCORE.sh \
--state NC \
--plan-type congress \
--geojson /tmp/NC/NC_2020_VD_tabblock.vtd.datasets.geojson \
--census T_20_CENS \
--vap V_20_VAP \
--cvap V_20_CVAP \
--elections E_16-20_COMP \
--graph /tmp/NC/NC_2020_graph.json \
--plans testdata/plans/NC_congress_plans.tagged.jsonl \
--scores temp/TEST_scores.csv \
--by-district temp/TEST_by-district.jsonl