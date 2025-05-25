#!/bin/bash

echo Extracting AL data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_AL_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/AL_data_map.v5.json \
--graph ~/local/adjacency-graphs/AL_2020_graph.json \
--data ~/local/temp-data/AL_input_data.v5.jsonl

echo Extracting AK data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_AK_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/AK_data_map.v5.json \
--graph ~/local/adjacency-graphs/AK_2020_graph.json \
--data ~/local/temp-data/AK_input_data.v5.jsonl

echo Extracting AZ data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_AZ_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/AZ_data_map.v5.json \
--graph ~/local/adjacency-graphs/AZ_2020_graph.json \
--data ~/local/temp-data/AZ_input_data.v5.jsonl

echo Extracting AR data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_AR_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/AR_data_map.v5.json \
--graph ~/local/adjacency-graphs/AR_2020_graph.json \
--data ~/local/temp-data/AR_input_data.v5.jsonl

echo Extracting CA data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_CA_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/CA_data_map.v5.json \
--graph ~/local/adjacency-graphs/CA_2020_graph.json \
--data ~/local/temp-data/CA_input_data.v5.jsonl

echo Extracting CO data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_CO_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/CO_data_map.v5.json \
--graph ~/local/adjacency-graphs/CO_2020_graph.json \
--data ~/local/temp-data/CO_input_data.v5.jsonl

echo Extracting CT data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_CT_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/CT_data_map.v5.json \
--graph ~/local/adjacency-graphs/CT_2020_graph.json \
--data ~/local/temp-data/CT_input_data.v5.jsonl

echo Extracting DE data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_DE_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/DE_data_map.v5.json \
--graph ~/local/adjacency-graphs/DE_2020_graph.json \
--data ~/local/temp-data/DE_input_data.v5.jsonl

echo Extracting FL data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_FL_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/FL_data_map.v5.json \
--graph ~/local/adjacency-graphs/FL_2020_graph.json \
--data ~/local/temp-data/FL_input_data.v5.jsonl

echo Extracting GA data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_GA_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/GA_data_map.v5.json \
--graph ~/local/adjacency-graphs/GA_2020_graph.json \
--data ~/local/temp-data/GA_input_data.v5.jsonl

echo Extracting HI data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_HI_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/HI_data_map.v5.json \
--graph ~/local/adjacency-graphs/HI_2020_graph.json \
--data ~/local/temp-data/HI_input_data.v5.jsonl

echo Extracting ID data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_ID_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/ID_data_map.v5.json \
--graph ~/local/adjacency-graphs/ID_2020_graph.json \
--data ~/local/temp-data/ID_input_data.v5.jsonl

echo Extracting IL data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_IL_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/IL_data_map.v5.json \
--graph ~/local/adjacency-graphs/IL_2020_graph.json \
--data ~/local/temp-data/IL_input_data.v5.jsonl

echo Extracting IN data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_IN_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/IN_data_map.v5.json \
--graph ~/local/adjacency-graphs/IN_2020_graph.json \
--data ~/local/temp-data/IN_input_data.v5.jsonl

echo Extracting IA data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_IA_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/IA_data_map.v5.json \
--graph ~/local/adjacency-graphs/IA_2020_graph.json \
--data ~/local/temp-data/IA_input_data.v5.jsonl

echo Extracting KS data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_KS_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/KS_data_map.v5.json \
--graph ~/local/adjacency-graphs/KS_2020_graph.json \
--data ~/local/temp-data/KS_input_data.v5.jsonl

echo Extracting KY data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_KY_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/KY_data_map.v5.json \
--graph ~/local/adjacency-graphs/KY_2020_graph.json \
--data ~/local/temp-data/KY_input_data.v5.jsonl

echo Extracting LA data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_LA_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/LA_data_map.v5.json \
--graph ~/local/adjacency-graphs/LA_2020_graph.json \
--data ~/local/temp-data/LA_input_data.v5.jsonl

echo Extracting ME data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_ME_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/ME_data_map.v5.json \
--graph ~/local/adjacency-graphs/ME_2020_graph.json \
--data ~/local/temp-data/ME_input_data.v5.jsonl

echo Extracting MD data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_MD_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/MD_data_map.v5.json \
--graph ~/local/adjacency-graphs/MD_2020_graph.json \
--data ~/local/temp-data/MD_input_data.v5.jsonl

echo Extracting MA data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_MA_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/MA_data_map.v5.json \
--graph ~/local/adjacency-graphs/MA_2020_graph.json \
--data ~/local/temp-data/MA_input_data.v5.jsonl

echo Extracting MI data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_MI_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/MI_data_map.v5.json \
--graph ~/local/adjacency-graphs/MI_2020_graph.json \
--data ~/local/temp-data/MI_input_data.v5.jsonl

echo Extracting MN data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_MN_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/MN_data_map.v5.json \
--graph ~/local/adjacency-graphs/MN_2020_graph.json \
--data ~/local/temp-data/MN_input_data.v5.jsonl

echo Extracting MS data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_MS_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/MS_data_map.v5.json \
--graph ~/local/adjacency-graphs/MS_2020_graph.json \
--data ~/local/temp-data/MS_input_data.v5.jsonl

echo Extracting MO data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_MO_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/MO_data_map.v5.json \
--graph ~/local/adjacency-graphs/MO_2020_graph.json \
--data ~/local/temp-data/MO_input_data.v5.jsonl

echo Extracting MT data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_MT_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/MT_data_map.v5.json \
--graph ~/local/adjacency-graphs/MT_2020_graph.json \
--data ~/local/temp-data/MT_input_data.v5.jsonl

echo Extracting NE data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_NE_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/NE_data_map.v5.json \
--graph ~/local/adjacency-graphs/NE_2020_graph.json \
--data ~/local/temp-data/NE_input_data.v5.jsonl

echo Extracting NV data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_NV_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/NV_data_map.v5.json \
--graph ~/local/adjacency-graphs/NV_2020_graph.json \
--data ~/local/temp-data/NV_input_data.v5.jsonl

echo Extracting NH data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_NH_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/NH_data_map.v5.json \
--graph ~/local/adjacency-graphs/NH_2020_graph.json \
--data ~/local/temp-data/NH_input_data.v5.jsonl

echo Extracting NJ data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_NJ_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/NJ_data_map.v5.json \
--graph ~/local/adjacency-graphs/NJ_2020_graph.json \
--data ~/local/temp-data/NJ_input_data.v5.jsonl

echo Extracting NM data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_NM_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/NM_data_map.v5.json \
--graph ~/local/adjacency-graphs/NM_2020_graph.json \
--data ~/local/temp-data/NM_input_data.v5.jsonl

echo Extracting NY data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_NY_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/NY_data_map.v5.json \
--graph ~/local/adjacency-graphs/NY_2020_graph.json \
--data ~/local/temp-data/NY_input_data.v5.jsonl

echo Extracting NC data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_NC_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/NC_data_map.v5.json \
--graph ~/local/adjacency-graphs/NC_2020_graph.json \
--data ~/local/temp-data/NC_input_data.v5.jsonl

echo Extracting ND data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_ND_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/ND_data_map.v5.json \
--graph ~/local/adjacency-graphs/ND_2020_graph.json \
--data ~/local/temp-data/ND_input_data.v5.jsonl

echo Extracting OH data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_OH_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/OH_data_map.v5.json \
--graph ~/local/adjacency-graphs/OH_2020_graph.json \
--data ~/local/temp-data/OH_input_data.v5.jsonl

echo Extracting OK data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_OK_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/OK_data_map.v5.json \
--graph ~/local/adjacency-graphs/OK_2020_graph.json \
--data ~/local/temp-data/OK_input_data.v5.jsonl

echo Extracting OR data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_OR_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/OR_data_map.v5.json \
--graph ~/local/adjacency-graphs/OR_2020_graph.json \
--data ~/local/temp-data/OR_input_data.v5.jsonl

echo Extracting PA data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_PA_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/PA_data_map.v5.json \
--graph ~/local/adjacency-graphs/PA_2020_graph.json \
--data ~/local/temp-data/PA_input_data.v5.jsonl

echo Extracting RI data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_RI_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/RI_data_map.v5.json \
--graph ~/local/adjacency-graphs/RI_2020_graph.json \
--data ~/local/temp-data/RI_input_data.v5.jsonl

echo Extracting SC data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_SC_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/SC_data_map.v5.json \
--graph ~/local/adjacency-graphs/SC_2020_graph.json \
--data ~/local/temp-data/SC_input_data.v5.jsonl

echo Extracting SD data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_SD_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/SD_data_map.v5.json \
--graph ~/local/adjacency-graphs/SD_2020_graph.json \
--data ~/local/temp-data/SD_input_data.v5.jsonl

echo Extracting TN data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_TN_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/TN_data_map.v5.json \
--graph ~/local/adjacency-graphs/TN_2020_graph.json \
--data ~/local/temp-data/TN_input_data.v5.jsonl

echo Extracting TX data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_TX_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/TX_data_map.v5.json \
--graph ~/local/adjacency-graphs/TX_2020_graph.json \
--data ~/local/temp-data/TX_input_data.v5.jsonl

echo Extracting UT data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_UT_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/UT_data_map.v5.json \
--graph ~/local/adjacency-graphs/UT_2020_graph.json \
--data ~/local/temp-data/UT_input_data.v5.jsonl

echo Extracting VT data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_VT_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/VT_data_map.v5.json \
--graph ~/local/adjacency-graphs/VT_2020_graph.json \
--data ~/local/temp-data/VT_input_data.v5.jsonl

echo Extracting VA data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_VA_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/VA_data_map.v5.json \
--graph ~/local/adjacency-graphs/VA_2020_graph.json \
--data ~/local/temp-data/VA_input_data.v5.jsonl

echo Extracting WA data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_WA_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/WA_data_map.v5.json \
--graph ~/local/adjacency-graphs/WA_2020_graph.json \
--data ~/local/temp-data/WA_input_data.v5.jsonl

echo Extracting WV data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_WV_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/WV_data_map.v5.json \
--graph ~/local/adjacency-graphs/WV_2020_graph.json \
--data ~/local/temp-data/WV_input_data.v5.jsonl

echo Extracting WI data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_WI_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/WI_data_map.v5.json \
--graph ~/local/adjacency-graphs/WI_2020_graph.json \
--data ~/local/temp-data/WI_input_data.v5.jsonl

echo Extracting WY data ...
scripts/data/extract_data.py \
--geojson ~/local/dra-to-publish/_WY_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/WY_data_map.v5.json \
--graph ~/local/adjacency-graphs/WY_2020_graph.json \
--data ~/local/temp-data/WY_input_data.v5.jsonl

