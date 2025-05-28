#!/bin/bash

# CYCLE=2020
DATA_PATH=~/local/temp-data # TODO
VERSION=v5
NEIGHBORHOOD_PATH=temp

echo Checking the neighborhoods for AL/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/AL_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/AL_congress_neighborhoods.jsonl

echo Checking the neighborhoods for AL/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/AL_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/AL_upper_neighborhoods.jsonl

echo Checking the neighborhoods for AL/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/AL_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/AL_lower_neighborhoods.jsonl

echo Checking the neighborhoods for AK/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/AK_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/AK_upper_neighborhoods.jsonl

echo Checking the neighborhoods for AK/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/AK_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/AK_lower_neighborhoods.jsonl

echo Checking the neighborhoods for AZ/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/AZ_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/AZ_congress_neighborhoods.jsonl

echo Checking the neighborhoods for AZ/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/AZ_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/AZ_upper_neighborhoods.jsonl

echo Checking the neighborhoods for AR/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/AR_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/AR_congress_neighborhoods.jsonl

echo Checking the neighborhoods for AR/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/AR_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/AR_upper_neighborhoods.jsonl

echo Checking the neighborhoods for AR/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/AR_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/AR_lower_neighborhoods.jsonl

echo Checking the neighborhoods for CA/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/CA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/CA_congress_neighborhoods.jsonl

echo Checking the neighborhoods for CA/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/CA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/CA_upper_neighborhoods.jsonl

echo Checking the neighborhoods for CA/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/CA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/CA_lower_neighborhoods.jsonl

echo Checking the neighborhoods for CO/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/CO_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/CO_congress_neighborhoods.jsonl

echo Checking the neighborhoods for CO/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/CO_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/CO_upper_neighborhoods.jsonl

echo Checking the neighborhoods for CO/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/CO_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/CO_lower_neighborhoods.jsonl

echo Checking the neighborhoods for CT/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/CT_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/CT_congress_neighborhoods.jsonl

echo Checking the neighborhoods for CT/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/CT_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/CT_upper_neighborhoods.jsonl

echo Checking the neighborhoods for CT/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/CT_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/CT_lower_neighborhoods.jsonl

echo Checking the neighborhoods for DE/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/DE_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/DE_upper_neighborhoods.jsonl

echo Checking the neighborhoods for DE/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/DE_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/DE_lower_neighborhoods.jsonl

echo Checking the neighborhoods for FL/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/FL_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/FL_congress_neighborhoods.jsonl

echo Checking the neighborhoods for FL/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/FL_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/FL_upper_neighborhoods.jsonl

echo Checking the neighborhoods for FL/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/FL_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/FL_lower_neighborhoods.jsonl

echo Checking the neighborhoods for GA/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/GA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/GA_congress_neighborhoods.jsonl

echo Checking the neighborhoods for GA/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/GA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/GA_upper_neighborhoods.jsonl

echo Checking the neighborhoods for GA/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/GA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/GA_lower_neighborhoods.jsonl

echo Checking the neighborhoods for HI/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/HI_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/HI_congress_neighborhoods.jsonl

echo Checking the neighborhoods for HI/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/HI_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/HI_upper_neighborhoods.jsonl

echo Checking the neighborhoods for HI/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/HI_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/HI_lower_neighborhoods.jsonl

echo Checking the neighborhoods for ID/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/ID_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/ID_congress_neighborhoods.jsonl

echo Checking the neighborhoods for ID/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/ID_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/ID_upper_neighborhoods.jsonl

echo Checking the neighborhoods for IL/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/IL_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/IL_congress_neighborhoods.jsonl

echo Checking the neighborhoods for IL/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/IL_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/IL_upper_neighborhoods.jsonl

echo Checking the neighborhoods for IL/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/IL_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/IL_lower_neighborhoods.jsonl

echo Checking the neighborhoods for IN/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/IN_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/IN_congress_neighborhoods.jsonl

echo Checking the neighborhoods for IN/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/IN_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/IN_upper_neighborhoods.jsonl

echo Checking the neighborhoods for IN/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/IN_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/IN_lower_neighborhoods.jsonl

echo Checking the neighborhoods for IA/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/IA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/IA_congress_neighborhoods.jsonl

echo Checking the neighborhoods for IA/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/IA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/IA_upper_neighborhoods.jsonl

echo Checking the neighborhoods for IA/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/IA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/IA_lower_neighborhoods.jsonl

echo Checking the neighborhoods for KS/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/KS_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/KS_congress_neighborhoods.jsonl

echo Checking the neighborhoods for KS/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/KS_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/KS_upper_neighborhoods.jsonl

echo Checking the neighborhoods for KS/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/KS_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/KS_lower_neighborhoods.jsonl

echo Checking the neighborhoods for KY/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/KY_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/KY_congress_neighborhoods.jsonl

echo Checking the neighborhoods for KY/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/KY_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/KY_upper_neighborhoods.jsonl

echo Checking the neighborhoods for KY/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/KY_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/KY_lower_neighborhoods.jsonl

echo Checking the neighborhoods for LA/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/LA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/LA_congress_neighborhoods.jsonl

echo Checking the neighborhoods for LA/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/LA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/LA_upper_neighborhoods.jsonl

echo Checking the neighborhoods for LA/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/LA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/LA_lower_neighborhoods.jsonl

echo Checking the neighborhoods for ME/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/ME_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/ME_congress_neighborhoods.jsonl

echo Checking the neighborhoods for ME/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/ME_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/ME_upper_neighborhoods.jsonl

echo Checking the neighborhoods for ME/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/ME_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/ME_lower_neighborhoods.jsonl

echo Checking the neighborhoods for MD/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/MD_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MD_congress_neighborhoods.jsonl

echo Checking the neighborhoods for MD/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/MD_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MD_upper_neighborhoods.jsonl

echo Checking the neighborhoods for MD/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/MD_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MD_lower_neighborhoods.jsonl

echo Checking the neighborhoods for MA/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/MA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MA_congress_neighborhoods.jsonl

echo Checking the neighborhoods for MA/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/MA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MA_upper_neighborhoods.jsonl

echo Checking the neighborhoods for MA/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/MA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MA_lower_neighborhoods.jsonl

echo Checking the neighborhoods for MI/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/MI_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MI_congress_neighborhoods.jsonl

echo Checking the neighborhoods for MI/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/MI_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MI_upper_neighborhoods.jsonl

echo Checking the neighborhoods for MI/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/MI_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MI_lower_neighborhoods.jsonl

echo Checking the neighborhoods for MN/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/MN_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MN_congress_neighborhoods.jsonl

echo Checking the neighborhoods for MN/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/MN_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MN_upper_neighborhoods.jsonl

echo Checking the neighborhoods for MN/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/MN_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MN_lower_neighborhoods.jsonl

echo Checking the neighborhoods for MS/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/MS_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MS_congress_neighborhoods.jsonl

echo Checking the neighborhoods for MS/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/MS_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MS_upper_neighborhoods.jsonl

echo Checking the neighborhoods for MS/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/MS_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MS_lower_neighborhoods.jsonl

echo Checking the neighborhoods for MO/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/MO_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MO_congress_neighborhoods.jsonl

echo Checking the neighborhoods for MO/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/MO_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MO_upper_neighborhoods.jsonl

echo Checking the neighborhoods for MO/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/MO_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MO_lower_neighborhoods.jsonl

echo Checking the neighborhoods for MT/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/MT_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MT_congress_neighborhoods.jsonl

echo Checking the neighborhoods for MT/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/MT_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MT_upper_neighborhoods.jsonl

echo Checking the neighborhoods for MT/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/MT_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MT_lower_neighborhoods.jsonl

echo Checking the neighborhoods for NE/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/NE_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/NE_congress_neighborhoods.jsonl

echo Checking the neighborhoods for NE/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/NE_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/NE_upper_neighborhoods.jsonl

echo Checking the neighborhoods for NV/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/NV_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/NV_congress_neighborhoods.jsonl

echo Checking the neighborhoods for NV/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/NV_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/NV_upper_neighborhoods.jsonl

echo Checking the neighborhoods for NV/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/NV_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/NV_lower_neighborhoods.jsonl

echo Checking the neighborhoods for NH/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/NH_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/NH_congress_neighborhoods.jsonl

echo Checking the neighborhoods for NH/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/NH_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/NH_upper_neighborhoods.jsonl

echo Checking the neighborhoods for NH/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/NH_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/NH_lower_neighborhoods.jsonl

echo Checking the neighborhoods for NJ/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/NJ_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/NJ_congress_neighborhoods.jsonl

echo Checking the neighborhoods for NJ/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/NJ_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/NJ_upper_neighborhoods.jsonl

echo Checking the neighborhoods for NM/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/NM_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/NM_congress_neighborhoods.jsonl

echo Checking the neighborhoods for NM/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/NM_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/NM_upper_neighborhoods.jsonl

echo Checking the neighborhoods for NM/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/NM_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/NM_lower_neighborhoods.jsonl

echo Checking the neighborhoods for NY/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/NY_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/NY_congress_neighborhoods.jsonl

echo Checking the neighborhoods for NY/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/NY_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/NY_upper_neighborhoods.jsonl

echo Checking the neighborhoods for NY/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/NY_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/NY_lower_neighborhoods.jsonl

echo Checking the neighborhoods for NC/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/NC_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/NC_congress_neighborhoods.jsonl

echo Checking the neighborhoods for NC/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/NC_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/NC_upper_neighborhoods.jsonl

echo Checking the neighborhoods for NC/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/NC_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/NC_lower_neighborhoods.jsonl

echo Checking the neighborhoods for ND/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/ND_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/ND_upper_neighborhoods.jsonl

echo Checking the neighborhoods for ND/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/ND_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/ND_lower_neighborhoods.jsonl

echo Checking the neighborhoods for OH/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/OH_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/OH_congress_neighborhoods.jsonl

echo Checking the neighborhoods for OH/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/OH_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/OH_upper_neighborhoods.jsonl

echo Checking the neighborhoods for OH/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/OH_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/OH_lower_neighborhoods.jsonl

echo Checking the neighborhoods for OK/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/OK_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/OK_congress_neighborhoods.jsonl

echo Checking the neighborhoods for OK/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/OK_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/OK_upper_neighborhoods.jsonl

echo Checking the neighborhoods for OK/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/OK_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/OK_lower_neighborhoods.jsonl

echo Checking the neighborhoods for OR/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/OR_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/OR_congress_neighborhoods.jsonl

echo Checking the neighborhoods for OR/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/OR_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/OR_upper_neighborhoods.jsonl

echo Checking the neighborhoods for OR/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/OR_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/OR_lower_neighborhoods.jsonl

echo Checking the neighborhoods for PA/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/PA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/PA_congress_neighborhoods.jsonl

echo Checking the neighborhoods for PA/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/PA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/PA_upper_neighborhoods.jsonl

echo Checking the neighborhoods for PA/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/PA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/PA_lower_neighborhoods.jsonl

echo Checking the neighborhoods for RI/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/RI_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/RI_congress_neighborhoods.jsonl

echo Checking the neighborhoods for RI/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/RI_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/RI_upper_neighborhoods.jsonl

echo Checking the neighborhoods for RI/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/RI_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/RI_lower_neighborhoods.jsonl

echo Checking the neighborhoods for SC/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/SC_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/SC_congress_neighborhoods.jsonl

echo Checking the neighborhoods for SC/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/SC_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/SC_upper_neighborhoods.jsonl

echo Checking the neighborhoods for SC/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/SC_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/SC_lower_neighborhoods.jsonl

echo Checking the neighborhoods for SD/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/SD_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/SD_upper_neighborhoods.jsonl

echo Checking the neighborhoods for SD/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/SD_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/SD_lower_neighborhoods.jsonl

echo Checking the neighborhoods for TN/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/TN_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/TN_congress_neighborhoods.jsonl

echo Checking the neighborhoods for TN/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/TN_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/TN_upper_neighborhoods.jsonl

echo Checking the neighborhoods for TN/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/TN_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/TN_lower_neighborhoods.jsonl

echo Checking the neighborhoods for TX/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/TX_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/TX_congress_neighborhoods.jsonl

echo Checking the neighborhoods for TX/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/TX_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/TX_upper_neighborhoods.jsonl

echo Checking the neighborhoods for TX/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/TX_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/TX_lower_neighborhoods.jsonl

echo Checking the neighborhoods for UT/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/UT_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/UT_congress_neighborhoods.jsonl

echo Checking the neighborhoods for UT/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/UT_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/UT_upper_neighborhoods.jsonl

echo Checking the neighborhoods for UT/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/UT_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/UT_lower_neighborhoods.jsonl

echo Checking the neighborhoods for VT/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/VT_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/VT_upper_neighborhoods.jsonl

echo Checking the neighborhoods for VT/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/VT_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/VT_lower_neighborhoods.jsonl

echo Checking the neighborhoods for VA/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/VA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/VA_congress_neighborhoods.jsonl

echo Checking the neighborhoods for VA/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/VA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/VA_upper_neighborhoods.jsonl

echo Checking the neighborhoods for VA/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/VA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/VA_lower_neighborhoods.jsonl

echo Checking the neighborhoods for WA/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/WA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/WA_congress_neighborhoods.jsonl

echo Checking the neighborhoods for WA/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/WA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/WA_upper_neighborhoods.jsonl

echo Checking the neighborhoods for WV/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/WV_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/WV_congress_neighborhoods.jsonl

echo Checking the neighborhoods for WV/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/WV_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/WV_upper_neighborhoods.jsonl

echo Checking the neighborhoods for WV/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/WV_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/WV_lower_neighborhoods.jsonl

echo Checking the neighborhoods for WI/congress ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/WI_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/WI_congress_neighborhoods.jsonl

echo Checking the neighborhoods for WI/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/WI_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/WI_upper_neighborhoods.jsonl

echo Checking the neighborhoods for WI/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/WI_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/WI_lower_neighborhoods.jsonl

echo Checking the neighborhoods for WY/upper ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/WY_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/WY_upper_neighborhoods.jsonl

echo Checking the neighborhoods for WY/lower ...
scripts/geographic-baseline/check_neighborhoods.py \
--data "${DATA_PATH}"/WY_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/WY_lower_neighborhoods.jsonl

