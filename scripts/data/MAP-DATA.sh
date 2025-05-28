#!/bin/bash

CYCLE=2020
GEOJSON_PATH=~/local/dra-to-publish # TODO
DATA_MAP_PATH=temp
VERSION=v5
CENSUS=T_20_CENS
VAP=V_20_VAP
CVAP=V_20_CVAP
ELECTIONS=__all__

echo Mapping AL data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_AL_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/AL_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping AK data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_AK_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/AK_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping AZ data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_AZ_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/AZ_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping AR data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_AR_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/AR_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping CA data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_CA_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/CA_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping CO data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_CO_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/CO_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping CT data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_CT_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/CT_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping DE data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_DE_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/DE_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping FL data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_FL_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/FL_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping GA data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_GA_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/GA_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping HI data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_HI_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/HI_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping ID data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_ID_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/ID_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping IL data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_IL_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/IL_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping IN data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_IN_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/IN_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping IA data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_IA_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/IA_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping KS data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_KS_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/KS_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping KY data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_KY_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/KY_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping LA data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_LA_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/LA_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping ME data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_ME_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/ME_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping MD data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_MD_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/MD_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping MA data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_MA_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/MA_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping MI data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_MI_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/MI_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping MN data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_MN_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/MN_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping MS data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_MS_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/MS_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping MO data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_MO_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/MO_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping MT data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_MT_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/MT_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping NE data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_NE_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/NE_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping NV data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_NV_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/NV_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping NH data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_NH_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/NH_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping NJ data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_NJ_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/NJ_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping NM data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_NM_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/NM_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping NY data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_NY_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/NY_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping NC data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_NC_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/NC_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping ND data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_ND_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/ND_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping OH data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_OH_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/OH_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping OK data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_OK_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/OK_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping OR data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_OR_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/OR_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping PA data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_PA_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/PA_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping RI data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_RI_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/RI_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping SC data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_SC_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/SC_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping SD data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_SD_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/SD_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping TN data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_TN_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/TN_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping TX data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_TX_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/TX_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping UT data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_UT_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/UT_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping VT data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_VT_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/VT_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping VA data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_VA_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/VA_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping WA data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_WA_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/WA_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping WV data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_WV_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/WV_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping WI data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_WI_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/WI_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

echo Mapping WY data ...
scripts/data/map_scoring_data.py \
--geojson "${GEOJSON_PATH}"/_WY_"${CYCLE}"_VD_tabblock.vtd.datasets.geojson \
--data-map "${DATA_MAP_PATH}"/WY_data_map."${VERSION}".json \
--census $CENSUS \
--vap $VAP \
--cvap $CVAP \
--elections $ELECTIONS

