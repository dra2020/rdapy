#!/bin/bash

echo "Extracting precinct locations for AL..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_AL_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/AL_data_map.v5.json \
> ~/local/temp-data/AL_precinct_locations.json

echo "Extracting precinct locations for AK..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_AK_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/AK_data_map.v5.json \
> ~/local/temp-data/AK_precinct_locations.json

echo "Extracting precinct locations for AZ..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_AZ_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/AZ_data_map.v5.json \
> ~/local/temp-data/AZ_precinct_locations.json

echo "Extracting precinct locations for AR..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_AR_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/AR_data_map.v5.json \
> ~/local/temp-data/AR_precinct_locations.json

echo "Extracting precinct locations for CA..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_CA_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/CA_data_map.v5.json \
> ~/local/temp-data/CA_precinct_locations.json

echo "Extracting precinct locations for CO..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_CO_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/CO_data_map.v5.json \
> ~/local/temp-data/CO_precinct_locations.json

echo "Extracting precinct locations for CT..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_CT_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/CT_data_map.v5.json \
> ~/local/temp-data/CT_precinct_locations.json

echo "Extracting precinct locations for DE..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_DE_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/DE_data_map.v5.json \
> ~/local/temp-data/DE_precinct_locations.json

echo "Extracting precinct locations for FL..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_FL_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/FL_data_map.v5.json \
> ~/local/temp-data/FL_precinct_locations.json

echo "Extracting precinct locations for GA..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_GA_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/GA_data_map.v5.json \
> ~/local/temp-data/GA_precinct_locations.json

echo "Extracting precinct locations for HI..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_HI_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/HI_data_map.v5.json \
> ~/local/temp-data/HI_precinct_locations.json

echo "Extracting precinct locations for ID..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_ID_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/ID_data_map.v5.json \
> ~/local/temp-data/ID_precinct_locations.json

echo "Extracting precinct locations for IL..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_IL_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/IL_data_map.v5.json \
> ~/local/temp-data/IL_precinct_locations.json

echo "Extracting precinct locations for IN..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_IN_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/IN_data_map.v5.json \
> ~/local/temp-data/IN_precinct_locations.json

echo "Extracting precinct locations for IA..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_IA_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/IA_data_map.v5.json \
> ~/local/temp-data/IA_precinct_locations.json

echo "Extracting precinct locations for KS..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_KS_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/KS_data_map.v5.json \
> ~/local/temp-data/KS_precinct_locations.json

echo "Extracting precinct locations for KY..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_KY_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/KY_data_map.v5.json \
> ~/local/temp-data/KY_precinct_locations.json

echo "Extracting precinct locations for LA..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_LA_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/LA_data_map.v5.json \
> ~/local/temp-data/LA_precinct_locations.json

echo "Extracting precinct locations for ME..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_ME_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/ME_data_map.v5.json \
> ~/local/temp-data/ME_precinct_locations.json

echo "Extracting precinct locations for MD..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_MD_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/MD_data_map.v5.json \
> ~/local/temp-data/MD_precinct_locations.json

echo "Extracting precinct locations for MA..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_MA_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/MA_data_map.v5.json \
> ~/local/temp-data/MA_precinct_locations.json

echo "Extracting precinct locations for MI..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_MI_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/MI_data_map.v5.json \
> ~/local/temp-data/MI_precinct_locations.json

echo "Extracting precinct locations for MN..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_MN_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/MN_data_map.v5.json \
> ~/local/temp-data/MN_precinct_locations.json

echo "Extracting precinct locations for MS..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_MS_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/MS_data_map.v5.json \
> ~/local/temp-data/MS_precinct_locations.json

echo "Extracting precinct locations for MO..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_MO_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/MO_data_map.v5.json \
> ~/local/temp-data/MO_precinct_locations.json

echo "Extracting precinct locations for MT..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_MT_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/MT_data_map.v5.json \
> ~/local/temp-data/MT_precinct_locations.json

echo "Extracting precinct locations for NE..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_NE_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/NE_data_map.v5.json \
> ~/local/temp-data/NE_precinct_locations.json

echo "Extracting precinct locations for NV..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_NV_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/NV_data_map.v5.json \
> ~/local/temp-data/NV_precinct_locations.json

echo "Extracting precinct locations for NH..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_NH_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/NH_data_map.v5.json \
> ~/local/temp-data/NH_precinct_locations.json

echo "Extracting precinct locations for NJ..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_NJ_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/NJ_data_map.v5.json \
> ~/local/temp-data/NJ_precinct_locations.json

echo "Extracting precinct locations for NM..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_NM_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/NM_data_map.v5.json \
> ~/local/temp-data/NM_precinct_locations.json

echo "Extracting precinct locations for NY..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_NY_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/NY_data_map.v5.json \
> ~/local/temp-data/NY_precinct_locations.json

echo "Extracting precinct locations for NC..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_NC_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/NC_data_map.v5.json \
> ~/local/temp-data/NC_precinct_locations.json

echo "Extracting precinct locations for ND..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_ND_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/ND_data_map.v5.json \
> ~/local/temp-data/ND_precinct_locations.json

echo "Extracting precinct locations for OH..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_OH_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/OH_data_map.v5.json \
> ~/local/temp-data/OH_precinct_locations.json

echo "Extracting precinct locations for OK..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_OK_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/OK_data_map.v5.json \
> ~/local/temp-data/OK_precinct_locations.json

echo "Extracting precinct locations for OR..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_OR_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/OR_data_map.v5.json \
> ~/local/temp-data/OR_precinct_locations.json

echo "Extracting precinct locations for PA..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_PA_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/PA_data_map.v5.json \
> ~/local/temp-data/PA_precinct_locations.json

echo "Extracting precinct locations for RI..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_RI_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/RI_data_map.v5.json \
> ~/local/temp-data/RI_precinct_locations.json

echo "Extracting precinct locations for SC..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_SC_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/SC_data_map.v5.json \
> ~/local/temp-data/SC_precinct_locations.json

echo "Extracting precinct locations for SD..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_SD_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/SD_data_map.v5.json \
> ~/local/temp-data/SD_precinct_locations.json

echo "Extracting precinct locations for TN..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_TN_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/TN_data_map.v5.json \
> ~/local/temp-data/TN_precinct_locations.json

echo "Extracting precinct locations for TX..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_TX_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/TX_data_map.v5.json \
> ~/local/temp-data/TX_precinct_locations.json

echo "Extracting precinct locations for UT..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_UT_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/UT_data_map.v5.json \
> ~/local/temp-data/UT_precinct_locations.json

echo "Extracting precinct locations for VT..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_VT_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/VT_data_map.v5.json \
> ~/local/temp-data/VT_precinct_locations.json

echo "Extracting precinct locations for VA..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_VA_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/VA_data_map.v5.json \
> ~/local/temp-data/VA_precinct_locations.json

echo "Extracting precinct locations for WA..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_WA_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/WA_data_map.v5.json \
> ~/local/temp-data/WA_precinct_locations.json

echo "Extracting precinct locations for WV..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_WV_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/WV_data_map.v5.json \
> ~/local/temp-data/WV_precinct_locations.json

echo "Extracting precinct locations for WI..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_WI_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/WI_data_map.v5.json \
> ~/local/temp-data/WI_precinct_locations.json

echo "Extracting precinct locations for WY..."
scripts/graphs/extract_locations.py \
--geojson ~/local/dra-to-publish/_WY_2020_VD_tabblock.vtd.datasets.geojson \
--data-map ~/local/temp-data/WY_data_map.v5.json \
> ~/local/temp-data/WY_precinct_locations.json

