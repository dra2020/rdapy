#!/bin/bash

echo Extracting AL data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_AL_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/AL_data_map.v4.json \
--graph ~/local/dra-to-publish/AL_2020_graph.json \
--data ~/local/temp-data/AL_input_data.v4.jsonl

echo Extracting AK data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_AK_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/AK_data_map.v4.json \
--graph ~/local/dra-to-publish/AK_2020_graph.json \
--data ~/local/temp-data/AK_input_data.v4.jsonl

echo Extracting AZ data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_AZ_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/AZ_data_map.v4.json \
--graph ~/local/dra-to-publish/AZ_2020_graph.json \
--data ~/local/temp-data/AZ_input_data.v4.jsonl

echo Extracting AR data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_AR_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/AR_data_map.v4.json \
--graph ~/local/dra-to-publish/AR_2020_graph.json \
--data ~/local/temp-data/AR_input_data.v4.jsonl

echo Extracting CA data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_CA_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/CA_data_map.v4.json \
--graph ~/local/dra-to-publish/CA_2020_graph.json \
--data ~/local/temp-data/CA_input_data.v4.jsonl

echo Extracting CO data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_CO_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/CO_data_map.v4.json \
--graph ~/local/dra-to-publish/CO_2020_graph.json \
--data ~/local/temp-data/CO_input_data.v4.jsonl

echo Extracting CT data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_CT_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/CT_data_map.v4.json \
--graph ~/local/dra-to-publish/CT_2020_graph.json \
--data ~/local/temp-data/CT_input_data.v4.jsonl

echo Extracting DE data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_DE_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/DE_data_map.v4.json \
--graph ~/local/dra-to-publish/DE_2020_graph.json \
--data ~/local/temp-data/DE_input_data.v4.jsonl

echo Extracting FL data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_FL_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/FL_data_map.v4.json \
--graph ~/local/dra-to-publish/FL_2020_graph.json \
--data ~/local/temp-data/FL_input_data.v4.jsonl

echo Extracting GA data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_GA_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/GA_data_map.v4.json \
--graph ~/local/dra-to-publish/GA_2020_graph.json \
--data ~/local/temp-data/GA_input_data.v4.jsonl

echo Extracting HI data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_HI_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/HI_data_map.v4.json \
--graph ~/local/dra-to-publish/HI_2020_graph.json \
--data ~/local/temp-data/HI_input_data.v4.jsonl

echo Extracting ID data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_ID_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/ID_data_map.v4.json \
--graph ~/local/dra-to-publish/ID_2020_graph.json \
--data ~/local/temp-data/ID_input_data.v4.jsonl

echo Extracting IL data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_IL_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/IL_data_map.v4.json \
--graph ~/local/dra-to-publish/IL_2020_graph.json \
--data ~/local/temp-data/IL_input_data.v4.jsonl

echo Extracting IN data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_IN_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/IN_data_map.v4.json \
--graph ~/local/dra-to-publish/IN_2020_graph.json \
--data ~/local/temp-data/IN_input_data.v4.jsonl

echo Extracting IA data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_IA_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/IA_data_map.v4.json \
--graph ~/local/dra-to-publish/IA_2020_graph.json \
--data ~/local/temp-data/IA_input_data.v4.jsonl

echo Extracting KS data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_KS_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/KS_data_map.v4.json \
--graph ~/local/dra-to-publish/KS_2020_graph.json \
--data ~/local/temp-data/KS_input_data.v4.jsonl

echo Extracting KY data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_KY_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/KY_data_map.v4.json \
--graph ~/local/dra-to-publish/KY_2020_graph.json \
--data ~/local/temp-data/KY_input_data.v4.jsonl

echo Extracting LA data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_LA_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/LA_data_map.v4.json \
--graph ~/local/dra-to-publish/LA_2020_graph.json \
--data ~/local/temp-data/LA_input_data.v4.jsonl

echo Extracting ME data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_ME_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/ME_data_map.v4.json \
--graph ~/local/dra-to-publish/ME_2020_graph.json \
--data ~/local/temp-data/ME_input_data.v4.jsonl

echo Extracting MD data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_MD_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/MD_data_map.v4.json \
--graph ~/local/dra-to-publish/MD_2020_graph.json \
--data ~/local/temp-data/MD_input_data.v4.jsonl

echo Extracting MA data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_MA_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/MA_data_map.v4.json \
--graph ~/local/dra-to-publish/MA_2020_graph.json \
--data ~/local/temp-data/MA_input_data.v4.jsonl

echo Extracting MI data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_MI_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/MI_data_map.v4.json \
--graph ~/local/dra-to-publish/MI_2020_graph.json \
--data ~/local/temp-data/MI_input_data.v4.jsonl

echo Extracting MN data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_MN_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/MN_data_map.v4.json \
--graph ~/local/dra-to-publish/MN_2020_graph.json \
--data ~/local/temp-data/MN_input_data.v4.jsonl

echo Extracting MS data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_MS_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/MS_data_map.v4.json \
--graph ~/local/dra-to-publish/MS_2020_graph.json \
--data ~/local/temp-data/MS_input_data.v4.jsonl

echo Extracting MO data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_MO_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/MO_data_map.v4.json \
--graph ~/local/dra-to-publish/MO_2020_graph.json \
--data ~/local/temp-data/MO_input_data.v4.jsonl

echo Extracting MT data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_MT_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/MT_data_map.v4.json \
--graph ~/local/dra-to-publish/MT_2020_graph.json \
--data ~/local/temp-data/MT_input_data.v4.jsonl

echo Extracting NE data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_NE_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/NE_data_map.v4.json \
--graph ~/local/dra-to-publish/NE_2020_graph.json \
--data ~/local/temp-data/NE_input_data.v4.jsonl

echo Extracting NV data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_NV_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/NV_data_map.v4.json \
--graph ~/local/dra-to-publish/NV_2020_graph.json \
--data ~/local/temp-data/NV_input_data.v4.jsonl

echo Extracting NH data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_NH_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/NH_data_map.v4.json \
--graph ~/local/dra-to-publish/NH_2020_graph.json \
--data ~/local/temp-data/NH_input_data.v4.jsonl

echo Extracting NJ data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_NJ_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/NJ_data_map.v4.json \
--graph ~/local/dra-to-publish/NJ_2020_graph.json \
--data ~/local/temp-data/NJ_input_data.v4.jsonl

echo Extracting NM data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_NM_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/NM_data_map.v4.json \
--graph ~/local/dra-to-publish/NM_2020_graph.json \
--data ~/local/temp-data/NM_input_data.v4.jsonl

echo Extracting NY data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_NY_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/NY_data_map.v4.json \
--graph ~/local/dra-to-publish/NY_2020_graph.json \
--data ~/local/temp-data/NY_input_data.v4.jsonl

echo Extracting NC data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_NC_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/NC_data_map.v4.json \
--graph ~/local/dra-to-publish/NC_2020_graph.json \
--data ~/local/temp-data/NC_input_data.v4.jsonl

echo Extracting ND data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_ND_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/ND_data_map.v4.json \
--graph ~/local/dra-to-publish/ND_2020_graph.json \
--data ~/local/temp-data/ND_input_data.v4.jsonl

echo Extracting OH data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_OH_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/OH_data_map.v4.json \
--graph ~/local/dra-to-publish/OH_2020_graph.json \
--data ~/local/temp-data/OH_input_data.v4.jsonl

echo Extracting OK data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_OK_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/OK_data_map.v4.json \
--graph ~/local/dra-to-publish/OK_2020_graph.json \
--data ~/local/temp-data/OK_input_data.v4.jsonl

echo Extracting OR data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_OR_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/OR_data_map.v4.json \
--graph ~/local/dra-to-publish/OR_2020_graph.json \
--data ~/local/temp-data/OR_input_data.v4.jsonl

echo Extracting PA data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_PA_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/PA_data_map.v4.json \
--graph ~/local/dra-to-publish/PA_2020_graph.json \
--data ~/local/temp-data/PA_input_data.v4.jsonl

echo Extracting RI data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_RI_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/RI_data_map.v4.json \
--graph ~/local/dra-to-publish/RI_2020_graph.json \
--data ~/local/temp-data/RI_input_data.v4.jsonl

echo Extracting SC data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_SC_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/SC_data_map.v4.json \
--graph ~/local/dra-to-publish/SC_2020_graph.json \
--data ~/local/temp-data/SC_input_data.v4.jsonl

echo Extracting SD data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_SD_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/SD_data_map.v4.json \
--graph ~/local/dra-to-publish/SD_2020_graph.json \
--data ~/local/temp-data/SD_input_data.v4.jsonl

echo Extracting TN data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_TN_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/TN_data_map.v4.json \
--graph ~/local/dra-to-publish/TN_2020_graph.json \
--data ~/local/temp-data/TN_input_data.v4.jsonl

echo Extracting TX data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_TX_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/TX_data_map.v4.json \
--graph ~/local/dra-to-publish/TX_2020_graph.json \
--data ~/local/temp-data/TX_input_data.v4.jsonl

echo Extracting UT data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_UT_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/UT_data_map.v4.json \
--graph ~/local/dra-to-publish/UT_2020_graph.json \
--data ~/local/temp-data/UT_input_data.v4.jsonl

echo Extracting VT data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_VT_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/VT_data_map.v4.json \
--graph ~/local/dra-to-publish/VT_2020_graph.json \
--data ~/local/temp-data/VT_input_data.v4.jsonl

echo Extracting VA data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_VA_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/VA_data_map.v4.json \
--graph ~/local/dra-to-publish/VA_2020_graph.json \
--data ~/local/temp-data/VA_input_data.v4.jsonl

echo Extracting WA data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_WA_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/WA_data_map.v4.json \
--graph ~/local/dra-to-publish/WA_2020_graph.json \
--data ~/local/temp-data/WA_input_data.v4.jsonl

echo Extracting WV data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_WV_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/WV_data_map.v4.json \
--graph ~/local/dra-to-publish/WV_2020_graph.json \
--data ~/local/temp-data/WV_input_data.v4.jsonl

echo Extracting WI data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_WI_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/WI_data_map.v4.json \
--graph ~/local/dra-to-publish/WI_2020_graph.json \
--data ~/local/temp-data/WI_input_data.v4.jsonl

echo Extracting WY data ...
scripts/extract_data.py \
--geojson ~/local/dra-to-publish/_WY_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/WY_data_map.v4.json \
--graph ~/local/dra-to-publish/WY_2020_graph.json \
--data ~/local/temp-data/WY_input_data.v4.jsonl

