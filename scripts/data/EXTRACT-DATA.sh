#!/bin/bash

CYCLE=2020
GEOJSON_PATH=~/local/dra-to-publish # TODO
DATA_MAP_PATH=temp
VERSION=v5
GRAPH_PATH=~/local/adjacency-graphs # TODO

echo Extracting AL data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_AL_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/AL_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/AL_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/AL_input_data."${VERSION}".jsonl

echo Extracting AK data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_AK_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/AK_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/AK_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/AK_input_data."${VERSION}".jsonl

echo Extracting AZ data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_AZ_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/AZ_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/AZ_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/AZ_input_data."${VERSION}".jsonl

echo Extracting AR data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_AR_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/AR_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/AR_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/AR_input_data."${VERSION}".jsonl

echo Extracting CA data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_CA_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/CA_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/CA_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/CA_input_data."${VERSION}".jsonl

echo Extracting CO data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_CO_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/CO_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/CO_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/CO_input_data."${VERSION}".jsonl

echo Extracting CT data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_CT_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/CT_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/CT_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/CT_input_data."${VERSION}".jsonl

echo Extracting DE data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_DE_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/DE_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/DE_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/DE_input_data."${VERSION}".jsonl

echo Extracting FL data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_FL_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/FL_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/FL_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/FL_input_data."${VERSION}".jsonl

echo Extracting GA data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_GA_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/GA_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/GA_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/GA_input_data."${VERSION}".jsonl

echo Extracting HI data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_HI_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/HI_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/HI_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/HI_input_data."${VERSION}".jsonl

echo Extracting ID data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_ID_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/ID_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/ID_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/ID_input_data."${VERSION}".jsonl

echo Extracting IL data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_IL_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/IL_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/IL_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/IL_input_data."${VERSION}".jsonl

echo Extracting IN data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_IN_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/IN_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/IN_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/IN_input_data."${VERSION}".jsonl

echo Extracting IA data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_IA_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/IA_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/IA_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/IA_input_data."${VERSION}".jsonl

echo Extracting KS data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_KS_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/KS_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/KS_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/KS_input_data."${VERSION}".jsonl

echo Extracting KY data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_KY_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/KY_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/KY_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/KY_input_data."${VERSION}".jsonl

echo Extracting LA data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_LA_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/LA_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/LA_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/LA_input_data."${VERSION}".jsonl

echo Extracting ME data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_ME_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/ME_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/ME_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/ME_input_data."${VERSION}".jsonl

echo Extracting MD data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_MD_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/MD_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/MD_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/MD_input_data."${VERSION}".jsonl

echo Extracting MA data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_MA_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/MA_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/MA_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/MA_input_data."${VERSION}".jsonl

echo Extracting MI data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_MI_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/MI_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/MI_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/MI_input_data."${VERSION}".jsonl

echo Extracting MN data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_MN_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/MN_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/MN_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/MN_input_data."${VERSION}".jsonl

echo Extracting MS data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_MS_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/MS_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/MS_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/MS_input_data."${VERSION}".jsonl

echo Extracting MO data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_MO_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/MO_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/MO_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/MO_input_data."${VERSION}".jsonl

echo Extracting MT data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_MT_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/MT_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/MT_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/MT_input_data."${VERSION}".jsonl

echo Extracting NE data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_NE_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/NE_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/NE_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/NE_input_data."${VERSION}".jsonl

echo Extracting NV data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_NV_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/NV_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/NV_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/NV_input_data."${VERSION}".jsonl

echo Extracting NH data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_NH_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/NH_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/NH_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/NH_input_data."${VERSION}".jsonl

echo Extracting NJ data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_NJ_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/NJ_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/NJ_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/NJ_input_data."${VERSION}".jsonl

echo Extracting NM data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_NM_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/NM_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/NM_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/NM_input_data."${VERSION}".jsonl

echo Extracting NY data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_NY_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/NY_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/NY_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/NY_input_data."${VERSION}".jsonl

echo Extracting NC data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_NC_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/NC_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/NC_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/NC_input_data."${VERSION}".jsonl

echo Extracting ND data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_ND_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/ND_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/ND_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/ND_input_data."${VERSION}".jsonl

echo Extracting OH data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_OH_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/OH_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/OH_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/OH_input_data."${VERSION}".jsonl

echo Extracting OK data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_OK_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/OK_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/OK_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/OK_input_data."${VERSION}".jsonl

echo Extracting OR data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_OR_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/OR_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/OR_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/OR_input_data."${VERSION}".jsonl

echo Extracting PA data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_PA_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/PA_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/PA_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/PA_input_data."${VERSION}".jsonl

echo Extracting RI data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_RI_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/RI_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/RI_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/RI_input_data."${VERSION}".jsonl

echo Extracting SC data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_SC_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/SC_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/SC_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/SC_input_data."${VERSION}".jsonl

echo Extracting SD data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_SD_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/SD_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/SD_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/SD_input_data."${VERSION}".jsonl

echo Extracting TN data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_TN_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/TN_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/TN_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/TN_input_data."${VERSION}".jsonl

echo Extracting TX data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_TX_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/TX_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/TX_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/TX_input_data."${VERSION}".jsonl

echo Extracting UT data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_UT_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/UT_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/UT_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/UT_input_data."${VERSION}".jsonl

echo Extracting VT data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_VT_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/VT_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/VT_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/VT_input_data."${VERSION}".jsonl

echo Extracting VA data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_VA_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/VA_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/VA_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/VA_input_data."${VERSION}".jsonl

echo Extracting WA data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_WA_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/WA_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/WA_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/WA_input_data."${VERSION}".jsonl

echo Extracting WV data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_WV_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/WV_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/WV_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/WV_input_data."${VERSION}".jsonl

echo Extracting WI data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_WI_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/WI_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/WI_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/WI_input_data."${VERSION}".jsonl

echo Extracting WY data ...
scripts/data/extract_data.py \
--geojson "${GEOJSON_PATH}"/_WY_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/WY_data_map."${VERSION}".json \
--graph "${GRAPH_PATH}"/WY_"${CYCLE}"_graph.json \
--data "${DATA_MAP_PATH}"/WY_input_data."${VERSION}".jsonl

