#!/bin/bash

CYCLE=2020
GEOJSON_PATH=~/local/dra-to-publish # TODO
GRAPH_PATH=~/local/adjacency-graphs # TODO

echo Generating adjacency graph for AL ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_AL_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/AL_"${CYCLE}"_graph.json \
--locations /tmp/AL_precinct-locations.json

echo Generating adjacency graph for AK ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_AK_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/AK_"${CYCLE}"_graph.json \
--locations /tmp/AK_precinct-locations.json

echo Generating adjacency graph for AZ ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_AZ_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/AZ_"${CYCLE}"_graph.json \
--locations /tmp/AZ_precinct-locations.json

echo Generating adjacency graph for AR ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_AR_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/AR_"${CYCLE}"_graph.json \
--locations /tmp/AR_precinct-locations.json

echo Generating adjacency graph for CA ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_CA_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/CA_"${CYCLE}"_graph.json \
--locations /tmp/CA_precinct-locations.json

echo Generating adjacency graph for CO ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_CO_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/CO_"${CYCLE}"_graph.json \
--locations /tmp/CO_precinct-locations.json

echo Generating adjacency graph for CT ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_CT_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/CT_"${CYCLE}"_graph.json \
--locations /tmp/CT_precinct-locations.json

echo Generating adjacency graph for DE ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_DE_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/DE_"${CYCLE}"_graph.json \
--locations /tmp/DE_precinct-locations.json

echo Generating adjacency graph for FL ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_FL_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/FL_"${CYCLE}"_graph.json \
--locations /tmp/FL_precinct-locations.json

echo Generating adjacency graph for GA ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_GA_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/GA_"${CYCLE}"_graph.json \
--locations /tmp/GA_precinct-locations.json

echo Generating adjacency graph for HI ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_HI_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/HI_"${CYCLE}"_graph.json \
--locations /tmp/HI_precinct-locations.json

echo Generating adjacency graph for ID ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_ID_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/ID_"${CYCLE}"_graph.json \
--locations /tmp/ID_precinct-locations.json

echo Generating adjacency graph for IL ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_IL_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/IL_"${CYCLE}"_graph.json \
--locations /tmp/IL_precinct-locations.json

echo Generating adjacency graph for IN ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_IN_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/IN_"${CYCLE}"_graph.json \
--locations /tmp/IN_precinct-locations.json

echo Generating adjacency graph for IA ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_IA_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/IA_"${CYCLE}"_graph.json \
--locations /tmp/IA_precinct-locations.json

echo Generating adjacency graph for KS ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_KS_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/KS_"${CYCLE}"_graph.json \
--locations /tmp/KS_precinct-locations.json

echo Generating adjacency graph for KY ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_KY_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/KY_"${CYCLE}"_graph.json \
--locations /tmp/KY_precinct-locations.json

echo Generating adjacency graph for LA ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_LA_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/LA_"${CYCLE}"_graph.json \
--locations /tmp/LA_precinct-locations.json

echo Generating adjacency graph for ME ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_ME_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/ME_"${CYCLE}"_graph.json \
--locations /tmp/ME_precinct-locations.json

echo Generating adjacency graph for MD ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_MD_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/MD_"${CYCLE}"_graph.json \
--locations /tmp/MD_precinct-locations.json

echo Generating adjacency graph for MA ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_MA_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/MA_"${CYCLE}"_graph.json \
--locations /tmp/MA_precinct-locations.json

echo Generating adjacency graph for MI ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_MI_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/MI_"${CYCLE}"_graph.json \
--locations /tmp/MI_precinct-locations.json

echo Generating adjacency graph for MN ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_MN_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/MN_"${CYCLE}"_graph.json \
--locations /tmp/MN_precinct-locations.json

echo Generating adjacency graph for MS ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_MS_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/MS_"${CYCLE}"_graph.json \
--locations /tmp/MS_precinct-locations.json

echo Generating adjacency graph for MO ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_MO_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/MO_"${CYCLE}"_graph.json \
--locations /tmp/MO_precinct-locations.json

echo Generating adjacency graph for MT ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_MT_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/MT_"${CYCLE}"_graph.json \
--locations /tmp/MT_precinct-locations.json

echo Generating adjacency graph for NE ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_NE_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/NE_"${CYCLE}"_graph.json \
--locations /tmp/NE_precinct-locations.json

echo Generating adjacency graph for NV ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_NV_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/NV_"${CYCLE}"_graph.json \
--locations /tmp/NV_precinct-locations.json

echo Generating adjacency graph for NH ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_NH_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/NH_"${CYCLE}"_graph.json \
--locations /tmp/NH_precinct-locations.json

echo Generating adjacency graph for NJ ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_NJ_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/NJ_"${CYCLE}"_graph.json \
--locations /tmp/NJ_precinct-locations.json

echo Generating adjacency graph for NM ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_NM_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/NM_"${CYCLE}"_graph.json \
--locations /tmp/NM_precinct-locations.json

echo Generating adjacency graph for NY ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_NY_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/NY_"${CYCLE}"_graph.json \
--locations /tmp/NY_precinct-locations.json

echo Generating adjacency graph for NC ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_NC_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/NC_"${CYCLE}"_graph.json \
--locations /tmp/NC_precinct-locations.json

echo Generating adjacency graph for ND ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_ND_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/ND_"${CYCLE}"_graph.json \
--locations /tmp/ND_precinct-locations.json

echo Generating adjacency graph for OH ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_OH_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/OH_"${CYCLE}"_graph.json \
--locations /tmp/OH_precinct-locations.json

echo Generating adjacency graph for OK ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_OK_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/OK_"${CYCLE}"_graph.json \
--locations /tmp/OK_precinct-locations.json

echo Generating adjacency graph for OR ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_OR_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/OR_"${CYCLE}"_graph.json \
--locations /tmp/OR_precinct-locations.json

echo Generating adjacency graph for PA ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_PA_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/PA_"${CYCLE}"_graph.json \
--locations /tmp/PA_precinct-locations.json

echo Generating adjacency graph for RI ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_RI_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/RI_"${CYCLE}"_graph.json \
--locations /tmp/RI_precinct-locations.json

echo Generating adjacency graph for SC ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_SC_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/SC_"${CYCLE}"_graph.json \
--locations /tmp/SC_precinct-locations.json

echo Generating adjacency graph for SD ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_SD_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/SD_"${CYCLE}"_graph.json \
--locations /tmp/SD_precinct-locations.json

echo Generating adjacency graph for TN ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_TN_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/TN_"${CYCLE}"_graph.json \
--locations /tmp/TN_precinct-locations.json

echo Generating adjacency graph for TX ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_TX_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/TX_"${CYCLE}"_graph.json \
--locations /tmp/TX_precinct-locations.json

echo Generating adjacency graph for UT ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_UT_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/UT_"${CYCLE}"_graph.json \
--locations /tmp/UT_precinct-locations.json

echo Generating adjacency graph for VT ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_VT_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/VT_"${CYCLE}"_graph.json \
--locations /tmp/VT_precinct-locations.json

echo Generating adjacency graph for VA ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_VA_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/VA_"${CYCLE}"_graph.json \
--locations /tmp/VA_precinct-locations.json

echo Generating adjacency graph for WA ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_WA_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/WA_"${CYCLE}"_graph.json \
--locations /tmp/WA_precinct-locations.json

echo Generating adjacency graph for WV ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_WV_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/WV_"${CYCLE}"_graph.json \
--locations /tmp/WV_precinct-locations.json

echo Generating adjacency graph for WI ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_WI_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/WI_"${CYCLE}"_graph.json \
--locations /tmp/WI_precinct-locations.json

echo Generating adjacency graph for WY ...
scripts/graphs/extract_graph.py \
--geojson "${GEOJSON_PATH}"/_WY_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--graph "${GRAPH_PATH}"/WY_"${CYCLE}"_graph.json \
--locations /tmp/WY_precinct-locations.json