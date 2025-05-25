#!/bin/bash

echo Generating adjacency graph for AL ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_AL_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/AL_2020_graph.json \
--locations /tmp/AL_precinct-locations.json

echo Generating adjacency graph for AK ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_AK_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/AK_2020_graph.json \
--locations /tmp/AK_precinct-locations.json

echo Generating adjacency graph for AZ ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_AZ_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/AZ_2020_graph.json \
--locations /tmp/AZ_precinct-locations.json

echo Generating adjacency graph for AR ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_AR_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/AR_2020_graph.json \
--locations /tmp/AR_precinct-locations.json

echo Generating adjacency graph for CA ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_CA_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/CA_2020_graph.json \
--locations /tmp/CA_precinct-locations.json

echo Generating adjacency graph for CO ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_CO_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/CO_2020_graph.json \
--locations /tmp/CO_precinct-locations.json

echo Generating adjacency graph for CT ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_CT_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/CT_2020_graph.json \
--locations /tmp/CT_precinct-locations.json

echo Generating adjacency graph for DE ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_DE_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/DE_2020_graph.json \
--locations /tmp/DE_precinct-locations.json

echo Generating adjacency graph for FL ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_FL_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/FL_2020_graph.json \
--locations /tmp/FL_precinct-locations.json

echo Generating adjacency graph for GA ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_GA_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/GA_2020_graph.json \
--locations /tmp/GA_precinct-locations.json

echo Generating adjacency graph for HI ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_HI_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/HI_2020_graph.json \
--locations /tmp/HI_precinct-locations.json

echo Generating adjacency graph for ID ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_ID_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/ID_2020_graph.json \
--locations /tmp/ID_precinct-locations.json

echo Generating adjacency graph for IL ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_IL_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/IL_2020_graph.json \
--locations /tmp/IL_precinct-locations.json

echo Generating adjacency graph for IN ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_IN_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/IN_2020_graph.json \
--locations /tmp/IN_precinct-locations.json

echo Generating adjacency graph for IA ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_IA_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/IA_2020_graph.json \
--locations /tmp/IA_precinct-locations.json

echo Generating adjacency graph for KS ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_KS_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/KS_2020_graph.json \
--locations /tmp/KS_precinct-locations.json

echo Generating adjacency graph for KY ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_KY_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/KY_2020_graph.json \
--locations /tmp/KY_precinct-locations.json

echo Generating adjacency graph for LA ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_LA_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/LA_2020_graph.json \
--locations /tmp/LA_precinct-locations.json

echo Generating adjacency graph for ME ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_ME_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/ME_2020_graph.json \
--locations /tmp/ME_precinct-locations.json

echo Generating adjacency graph for MD ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_MD_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/MD_2020_graph.json \
--locations /tmp/MD_precinct-locations.json

echo Generating adjacency graph for MA ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_MA_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/MA_2020_graph.json \
--locations /tmp/MA_precinct-locations.json

echo Generating adjacency graph for MI ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_MI_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/MI_2020_graph.json \
--locations /tmp/MI_precinct-locations.json

echo Generating adjacency graph for MN ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_MN_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/MN_2020_graph.json \
--locations /tmp/MN_precinct-locations.json

echo Generating adjacency graph for MS ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_MS_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/MS_2020_graph.json \
--locations /tmp/MS_precinct-locations.json

echo Generating adjacency graph for MO ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_MO_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/MO_2020_graph.json \
--locations /tmp/MO_precinct-locations.json

echo Generating adjacency graph for MT ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_MT_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/MT_2020_graph.json \
--locations /tmp/MT_precinct-locations.json

echo Generating adjacency graph for NE ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_NE_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/NE_2020_graph.json \
--locations /tmp/NE_precinct-locations.json

echo Generating adjacency graph for NV ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_NV_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/NV_2020_graph.json \
--locations /tmp/NV_precinct-locations.json

echo Generating adjacency graph for NH ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_NH_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/NH_2020_graph.json \
--locations /tmp/NH_precinct-locations.json

echo Generating adjacency graph for NJ ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_NJ_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/NJ_2020_graph.json \
--locations /tmp/NJ_precinct-locations.json

echo Generating adjacency graph for NM ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_NM_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/NM_2020_graph.json \
--locations /tmp/NM_precinct-locations.json

echo Generating adjacency graph for NY ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_NY_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/NY_2020_graph.json \
--locations /tmp/NY_precinct-locations.json

echo Generating adjacency graph for NC ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_NC_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/NC_2020_graph.json \
--locations /tmp/NC_precinct-locations.json

echo Generating adjacency graph for ND ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_ND_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/ND_2020_graph.json \
--locations /tmp/ND_precinct-locations.json

echo Generating adjacency graph for OH ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_OH_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/OH_2020_graph.json \
--locations /tmp/OH_precinct-locations.json

echo Generating adjacency graph for OK ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_OK_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/OK_2020_graph.json \
--locations /tmp/OK_precinct-locations.json

echo Generating adjacency graph for OR ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_OR_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/OR_2020_graph.json \
--locations /tmp/OR_precinct-locations.json

echo Generating adjacency graph for PA ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_PA_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/PA_2020_graph.json \
--locations /tmp/PA_precinct-locations.json

echo Generating adjacency graph for RI ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_RI_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/RI_2020_graph.json \
--locations /tmp/RI_precinct-locations.json

echo Generating adjacency graph for SC ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_SC_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/SC_2020_graph.json \
--locations /tmp/SC_precinct-locations.json

echo Generating adjacency graph for SD ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_SD_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/SD_2020_graph.json \
--locations /tmp/SD_precinct-locations.json

echo Generating adjacency graph for TN ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_TN_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/TN_2020_graph.json \
--locations /tmp/TN_precinct-locations.json

echo Generating adjacency graph for TX ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_TX_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/TX_2020_graph.json \
--locations /tmp/TX_precinct-locations.json

echo Generating adjacency graph for UT ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_UT_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/UT_2020_graph.json \
--locations /tmp/UT_precinct-locations.json

echo Generating adjacency graph for VT ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_VT_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/VT_2020_graph.json \
--locations /tmp/VT_precinct-locations.json

echo Generating adjacency graph for VA ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_VA_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/VA_2020_graph.json \
--locations /tmp/VA_precinct-locations.json

echo Generating adjacency graph for WA ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_WA_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/WA_2020_graph.json \
--locations /tmp/WA_precinct-locations.json

echo Generating adjacency graph for WV ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_WV_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/WV_2020_graph.json \
--locations /tmp/WV_precinct-locations.json

echo Generating adjacency graph for WI ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_WI_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/WI_2020_graph.json \
--locations /tmp/WI_precinct-locations.json

echo Generating adjacency graph for WY ...
scripts/graphs/extract_graph.py \
--geojson ~/local/dra-to-publish/_WY_2020_VD_tabblock.vtd.datasets.geojson \
--graph ~/local/adjacency-graphs/WY_2020_graph.json \
--locations /tmp/WY_precinct-locations.json