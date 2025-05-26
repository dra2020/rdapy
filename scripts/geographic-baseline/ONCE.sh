#!/bin/bash

# CYCLE=2020
DATA_PATH=~/local/temp-data
VERSION=v5
NEIGHBORHOOD_PATH=~/local/geographic-baseline
PRECOMPUTED_PATH=~/local/geographic-baseline

echo Computing the geographic baseline for AL/congress ...
scripts/geographic-baseline/once.py \
--state AL \
--plan-type congress \
--data "${DATA_PATH}"/AL_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/AL_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/AL_congress_precomputed.json

echo Computing the geographic baseline for AL/upper ...
scripts/geographic-baseline/once.py \
--state AL \
--plan-type upper \
--data "${DATA_PATH}"/AL_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/AL_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/AL_upper_precomputed.json

echo Computing the geographic baseline for AL/lower ...
scripts/geographic-baseline/once.py \
--state AL \
--plan-type lower \
--data "${DATA_PATH}"/AL_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/AL_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/AL_lower_precomputed.json

echo Computing the geographic baseline for AK/upper ...
scripts/geographic-baseline/once.py \
--state AK \
--plan-type upper \
--data "${DATA_PATH}"/AK_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/AK_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/AK_upper_precomputed.json

echo Computing the geographic baseline for AK/lower ...
scripts/geographic-baseline/once.py \
--state AK \
--plan-type lower \
--data "${DATA_PATH}"/AK_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/AK_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/AK_lower_precomputed.json

echo Computing the geographic baseline for AZ/congress ...
scripts/geographic-baseline/once.py \
--state AZ \
--plan-type congress \
--data "${DATA_PATH}"/AZ_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/AZ_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/AZ_congress_precomputed.json

echo Computing the geographic baseline for AZ/upper ...
scripts/geographic-baseline/once.py \
--state AZ \
--plan-type upper \
--data "${DATA_PATH}"/AZ_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/AZ_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/AZ_upper_precomputed.json

echo Computing the geographic baseline for AR/congress ...
scripts/geographic-baseline/once.py \
--state AR \
--plan-type congress \
--data "${DATA_PATH}"/AR_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/AR_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/AR_congress_precomputed.json

echo Computing the geographic baseline for AR/upper ...
scripts/geographic-baseline/once.py \
--state AR \
--plan-type upper \
--data "${DATA_PATH}"/AR_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/AR_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/AR_upper_precomputed.json

echo Computing the geographic baseline for AR/lower ...
scripts/geographic-baseline/once.py \
--state AR \
--plan-type lower \
--data "${DATA_PATH}"/AR_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/AR_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/AR_lower_precomputed.json

echo Computing the geographic baseline for CA/congress ...
scripts/geographic-baseline/once.py \
--state CA \
--plan-type congress \
--data "${DATA_PATH}"/CA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/CA_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/CA_congress_precomputed.json

echo Computing the geographic baseline for CA/upper ...
scripts/geographic-baseline/once.py \
--state CA \
--plan-type upper \
--data "${DATA_PATH}"/CA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/CA_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/CA_upper_precomputed.json

echo Computing the geographic baseline for CA/lower ...
scripts/geographic-baseline/once.py \
--state CA \
--plan-type lower \
--data "${DATA_PATH}"/CA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/CA_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/CA_lower_precomputed.json

echo Computing the geographic baseline for CO/congress ...
scripts/geographic-baseline/once.py \
--state CO \
--plan-type congress \
--data "${DATA_PATH}"/CO_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/CO_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/CO_congress_precomputed.json

echo Computing the geographic baseline for CO/upper ...
scripts/geographic-baseline/once.py \
--state CO \
--plan-type upper \
--data "${DATA_PATH}"/CO_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/CO_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/CO_upper_precomputed.json

echo Computing the geographic baseline for CO/lower ...
scripts/geographic-baseline/once.py \
--state CO \
--plan-type lower \
--data "${DATA_PATH}"/CO_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/CO_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/CO_lower_precomputed.json

echo Computing the geographic baseline for CT/congress ...
scripts/geographic-baseline/once.py \
--state CT \
--plan-type congress \
--data "${DATA_PATH}"/CT_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/CT_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/CT_congress_precomputed.json

echo Computing the geographic baseline for CT/upper ...
scripts/geographic-baseline/once.py \
--state CT \
--plan-type upper \
--data "${DATA_PATH}"/CT_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/CT_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/CT_upper_precomputed.json

echo Computing the geographic baseline for CT/lower ...
scripts/geographic-baseline/once.py \
--state CT \
--plan-type lower \
--data "${DATA_PATH}"/CT_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/CT_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/CT_lower_precomputed.json

echo Computing the geographic baseline for DE/upper ...
scripts/geographic-baseline/once.py \
--state DE \
--plan-type upper \
--data "${DATA_PATH}"/DE_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/DE_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/DE_upper_precomputed.json

echo Computing the geographic baseline for DE/lower ...
scripts/geographic-baseline/once.py \
--state DE \
--plan-type lower \
--data "${DATA_PATH}"/DE_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/DE_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/DE_lower_precomputed.json

echo Computing the geographic baseline for FL/congress ...
scripts/geographic-baseline/once.py \
--state FL \
--plan-type congress \
--data "${DATA_PATH}"/FL_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/FL_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/FL_congress_precomputed.json

echo Computing the geographic baseline for FL/upper ...
scripts/geographic-baseline/once.py \
--state FL \
--plan-type upper \
--data "${DATA_PATH}"/FL_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/FL_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/FL_upper_precomputed.json

echo Computing the geographic baseline for FL/lower ...
scripts/geographic-baseline/once.py \
--state FL \
--plan-type lower \
--data "${DATA_PATH}"/FL_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/FL_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/FL_lower_precomputed.json

echo Computing the geographic baseline for GA/congress ...
scripts/geographic-baseline/once.py \
--state GA \
--plan-type congress \
--data "${DATA_PATH}"/GA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/GA_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/GA_congress_precomputed.json

echo Computing the geographic baseline for GA/upper ...
scripts/geographic-baseline/once.py \
--state GA \
--plan-type upper \
--data "${DATA_PATH}"/GA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/GA_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/GA_upper_precomputed.json

echo Computing the geographic baseline for GA/lower ...
scripts/geographic-baseline/once.py \
--state GA \
--plan-type lower \
--data "${DATA_PATH}"/GA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/GA_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/GA_lower_precomputed.json

echo Computing the geographic baseline for HI/congress ...
scripts/geographic-baseline/once.py \
--state HI \
--plan-type congress \
--data "${DATA_PATH}"/HI_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/HI_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/HI_congress_precomputed.json

echo Computing the geographic baseline for HI/upper ...
scripts/geographic-baseline/once.py \
--state HI \
--plan-type upper \
--data "${DATA_PATH}"/HI_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/HI_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/HI_upper_precomputed.json

echo Computing the geographic baseline for HI/lower ...
scripts/geographic-baseline/once.py \
--state HI \
--plan-type lower \
--data "${DATA_PATH}"/HI_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/HI_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/HI_lower_precomputed.json

echo Computing the geographic baseline for ID/congress ...
scripts/geographic-baseline/once.py \
--state ID \
--plan-type congress \
--data "${DATA_PATH}"/ID_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/ID_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/ID_congress_precomputed.json

echo Computing the geographic baseline for ID/upper ...
scripts/geographic-baseline/once.py \
--state ID \
--plan-type upper \
--data "${DATA_PATH}"/ID_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/ID_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/ID_upper_precomputed.json

echo Computing the geographic baseline for IL/congress ...
scripts/geographic-baseline/once.py \
--state IL \
--plan-type congress \
--data "${DATA_PATH}"/IL_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/IL_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/IL_congress_precomputed.json

echo Computing the geographic baseline for IL/upper ...
scripts/geographic-baseline/once.py \
--state IL \
--plan-type upper \
--data "${DATA_PATH}"/IL_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/IL_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/IL_upper_precomputed.json

echo Computing the geographic baseline for IL/lower ...
scripts/geographic-baseline/once.py \
--state IL \
--plan-type lower \
--data "${DATA_PATH}"/IL_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/IL_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/IL_lower_precomputed.json

echo Computing the geographic baseline for IN/congress ...
scripts/geographic-baseline/once.py \
--state IN \
--plan-type congress \
--data "${DATA_PATH}"/IN_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/IN_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/IN_congress_precomputed.json

echo Computing the geographic baseline for IN/upper ...
scripts/geographic-baseline/once.py \
--state IN \
--plan-type upper \
--data "${DATA_PATH}"/IN_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/IN_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/IN_upper_precomputed.json

echo Computing the geographic baseline for IN/lower ...
scripts/geographic-baseline/once.py \
--state IN \
--plan-type lower \
--data "${DATA_PATH}"/IN_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/IN_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/IN_lower_precomputed.json

echo Computing the geographic baseline for IA/congress ...
scripts/geographic-baseline/once.py \
--state IA \
--plan-type congress \
--data "${DATA_PATH}"/IA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/IA_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/IA_congress_precomputed.json

echo Computing the geographic baseline for IA/upper ...
scripts/geographic-baseline/once.py \
--state IA \
--plan-type upper \
--data "${DATA_PATH}"/IA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/IA_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/IA_upper_precomputed.json

echo Computing the geographic baseline for IA/lower ...
scripts/geographic-baseline/once.py \
--state IA \
--plan-type lower \
--data "${DATA_PATH}"/IA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/IA_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/IA_lower_precomputed.json

echo Computing the geographic baseline for KS/congress ...
scripts/geographic-baseline/once.py \
--state KS \
--plan-type congress \
--data "${DATA_PATH}"/KS_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/KS_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/KS_congress_precomputed.json

echo Computing the geographic baseline for KS/upper ...
scripts/geographic-baseline/once.py \
--state KS \
--plan-type upper \
--data "${DATA_PATH}"/KS_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/KS_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/KS_upper_precomputed.json

echo Computing the geographic baseline for KS/lower ...
scripts/geographic-baseline/once.py \
--state KS \
--plan-type lower \
--data "${DATA_PATH}"/KS_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/KS_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/KS_lower_precomputed.json

echo Computing the geographic baseline for KY/congress ...
scripts/geographic-baseline/once.py \
--state KY \
--plan-type congress \
--data "${DATA_PATH}"/KY_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/KY_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/KY_congress_precomputed.json

echo Computing the geographic baseline for KY/upper ...
scripts/geographic-baseline/once.py \
--state KY \
--plan-type upper \
--data "${DATA_PATH}"/KY_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/KY_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/KY_upper_precomputed.json

echo Computing the geographic baseline for KY/lower ...
scripts/geographic-baseline/once.py \
--state KY \
--plan-type lower \
--data "${DATA_PATH}"/KY_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/KY_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/KY_lower_precomputed.json

echo Computing the geographic baseline for LA/congress ...
scripts/geographic-baseline/once.py \
--state LA \
--plan-type congress \
--data "${DATA_PATH}"/LA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/LA_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/LA_congress_precomputed.json

echo Computing the geographic baseline for LA/upper ...
scripts/geographic-baseline/once.py \
--state LA \
--plan-type upper \
--data "${DATA_PATH}"/LA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/LA_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/LA_upper_precomputed.json

echo Computing the geographic baseline for LA/lower ...
scripts/geographic-baseline/once.py \
--state LA \
--plan-type lower \
--data "${DATA_PATH}"/LA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/LA_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/LA_lower_precomputed.json

echo Computing the geographic baseline for ME/congress ...
scripts/geographic-baseline/once.py \
--state ME \
--plan-type congress \
--data "${DATA_PATH}"/ME_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/ME_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/ME_congress_precomputed.json

echo Computing the geographic baseline for ME/upper ...
scripts/geographic-baseline/once.py \
--state ME \
--plan-type upper \
--data "${DATA_PATH}"/ME_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/ME_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/ME_upper_precomputed.json

echo Computing the geographic baseline for ME/lower ...
scripts/geographic-baseline/once.py \
--state ME \
--plan-type lower \
--data "${DATA_PATH}"/ME_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/ME_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/ME_lower_precomputed.json

echo Computing the geographic baseline for MD/congress ...
scripts/geographic-baseline/once.py \
--state MD \
--plan-type congress \
--data "${DATA_PATH}"/MD_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MD_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/MD_congress_precomputed.json

echo Computing the geographic baseline for MD/upper ...
scripts/geographic-baseline/once.py \
--state MD \
--plan-type upper \
--data "${DATA_PATH}"/MD_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MD_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/MD_upper_precomputed.json

echo Computing the geographic baseline for MD/lower ...
scripts/geographic-baseline/once.py \
--state MD \
--plan-type lower \
--data "${DATA_PATH}"/MD_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MD_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/MD_lower_precomputed.json

echo Computing the geographic baseline for MA/congress ...
scripts/geographic-baseline/once.py \
--state MA \
--plan-type congress \
--data "${DATA_PATH}"/MA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MA_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/MA_congress_precomputed.json

echo Computing the geographic baseline for MA/upper ...
scripts/geographic-baseline/once.py \
--state MA \
--plan-type upper \
--data "${DATA_PATH}"/MA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MA_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/MA_upper_precomputed.json

echo Computing the geographic baseline for MA/lower ...
scripts/geographic-baseline/once.py \
--state MA \
--plan-type lower \
--data "${DATA_PATH}"/MA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MA_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/MA_lower_precomputed.json

echo Computing the geographic baseline for MI/congress ...
scripts/geographic-baseline/once.py \
--state MI \
--plan-type congress \
--data "${DATA_PATH}"/MI_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MI_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/MI_congress_precomputed.json

echo Computing the geographic baseline for MI/upper ...
scripts/geographic-baseline/once.py \
--state MI \
--plan-type upper \
--data "${DATA_PATH}"/MI_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MI_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/MI_upper_precomputed.json

echo Computing the geographic baseline for MI/lower ...
scripts/geographic-baseline/once.py \
--state MI \
--plan-type lower \
--data "${DATA_PATH}"/MI_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MI_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/MI_lower_precomputed.json

echo Computing the geographic baseline for MN/congress ...
scripts/geographic-baseline/once.py \
--state MN \
--plan-type congress \
--data "${DATA_PATH}"/MN_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MN_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/MN_congress_precomputed.json

echo Computing the geographic baseline for MN/upper ...
scripts/geographic-baseline/once.py \
--state MN \
--plan-type upper \
--data "${DATA_PATH}"/MN_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MN_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/MN_upper_precomputed.json

echo Computing the geographic baseline for MN/lower ...
scripts/geographic-baseline/once.py \
--state MN \
--plan-type lower \
--data "${DATA_PATH}"/MN_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MN_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/MN_lower_precomputed.json

echo Computing the geographic baseline for MS/congress ...
scripts/geographic-baseline/once.py \
--state MS \
--plan-type congress \
--data "${DATA_PATH}"/MS_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MS_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/MS_congress_precomputed.json

echo Computing the geographic baseline for MS/upper ...
scripts/geographic-baseline/once.py \
--state MS \
--plan-type upper \
--data "${DATA_PATH}"/MS_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MS_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/MS_upper_precomputed.json

echo Computing the geographic baseline for MS/lower ...
scripts/geographic-baseline/once.py \
--state MS \
--plan-type lower \
--data "${DATA_PATH}"/MS_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MS_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/MS_lower_precomputed.json

echo Computing the geographic baseline for MO/congress ...
scripts/geographic-baseline/once.py \
--state MO \
--plan-type congress \
--data "${DATA_PATH}"/MO_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MO_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/MO_congress_precomputed.json

echo Computing the geographic baseline for MO/upper ...
scripts/geographic-baseline/once.py \
--state MO \
--plan-type upper \
--data "${DATA_PATH}"/MO_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MO_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/MO_upper_precomputed.json

echo Computing the geographic baseline for MO/lower ...
scripts/geographic-baseline/once.py \
--state MO \
--plan-type lower \
--data "${DATA_PATH}"/MO_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MO_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/MO_lower_precomputed.json

echo Computing the geographic baseline for MT/congress ...
scripts/geographic-baseline/once.py \
--state MT \
--plan-type congress \
--data "${DATA_PATH}"/MT_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MT_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/MT_congress_precomputed.json

echo Computing the geographic baseline for MT/upper ...
scripts/geographic-baseline/once.py \
--state MT \
--plan-type upper \
--data "${DATA_PATH}"/MT_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MT_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/MT_upper_precomputed.json

echo Computing the geographic baseline for MT/lower ...
scripts/geographic-baseline/once.py \
--state MT \
--plan-type lower \
--data "${DATA_PATH}"/MT_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/MT_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/MT_lower_precomputed.json

echo Computing the geographic baseline for NE/congress ...
scripts/geographic-baseline/once.py \
--state NE \
--plan-type congress \
--data "${DATA_PATH}"/NE_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/NE_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/NE_congress_precomputed.json

echo Computing the geographic baseline for NE/upper ...
scripts/geographic-baseline/once.py \
--state NE \
--plan-type upper \
--data "${DATA_PATH}"/NE_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/NE_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/NE_upper_precomputed.json

echo Computing the geographic baseline for NV/congress ...
scripts/geographic-baseline/once.py \
--state NV \
--plan-type congress \
--data "${DATA_PATH}"/NV_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/NV_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/NV_congress_precomputed.json

echo Computing the geographic baseline for NV/upper ...
scripts/geographic-baseline/once.py \
--state NV \
--plan-type upper \
--data "${DATA_PATH}"/NV_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/NV_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/NV_upper_precomputed.json

echo Computing the geographic baseline for NV/lower ...
scripts/geographic-baseline/once.py \
--state NV \
--plan-type lower \
--data "${DATA_PATH}"/NV_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/NV_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/NV_lower_precomputed.json

echo Computing the geographic baseline for NH/congress ...
scripts/geographic-baseline/once.py \
--state NH \
--plan-type congress \
--data "${DATA_PATH}"/NH_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/NH_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/NH_congress_precomputed.json

echo Computing the geographic baseline for NH/upper ...
scripts/geographic-baseline/once.py \
--state NH \
--plan-type upper \
--data "${DATA_PATH}"/NH_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/NH_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/NH_upper_precomputed.json

echo Computing the geographic baseline for NH/lower ...
scripts/geographic-baseline/once.py \
--state NH \
--plan-type lower \
--data "${DATA_PATH}"/NH_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/NH_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/NH_lower_precomputed.json

echo Computing the geographic baseline for NJ/congress ...
scripts/geographic-baseline/once.py \
--state NJ \
--plan-type congress \
--data "${DATA_PATH}"/NJ_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/NJ_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/NJ_congress_precomputed.json

echo Computing the geographic baseline for NJ/upper ...
scripts/geographic-baseline/once.py \
--state NJ \
--plan-type upper \
--data "${DATA_PATH}"/NJ_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/NJ_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/NJ_upper_precomputed.json

echo Computing the geographic baseline for NM/congress ...
scripts/geographic-baseline/once.py \
--state NM \
--plan-type congress \
--data "${DATA_PATH}"/NM_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/NM_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/NM_congress_precomputed.json

echo Computing the geographic baseline for NM/upper ...
scripts/geographic-baseline/once.py \
--state NM \
--plan-type upper \
--data "${DATA_PATH}"/NM_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/NM_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/NM_upper_precomputed.json

echo Computing the geographic baseline for NM/lower ...
scripts/geographic-baseline/once.py \
--state NM \
--plan-type lower \
--data "${DATA_PATH}"/NM_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/NM_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/NM_lower_precomputed.json

echo Computing the geographic baseline for NY/congress ...
scripts/geographic-baseline/once.py \
--state NY \
--plan-type congress \
--data "${DATA_PATH}"/NY_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/NY_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/NY_congress_precomputed.json

echo Computing the geographic baseline for NY/upper ...
scripts/geographic-baseline/once.py \
--state NY \
--plan-type upper \
--data "${DATA_PATH}"/NY_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/NY_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/NY_upper_precomputed.json

echo Computing the geographic baseline for NY/lower ...
scripts/geographic-baseline/once.py \
--state NY \
--plan-type lower \
--data "${DATA_PATH}"/NY_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/NY_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/NY_lower_precomputed.json

echo Computing the geographic baseline for NC/congress ...
scripts/geographic-baseline/once.py \
--state NC \
--plan-type congress \
--data "${DATA_PATH}"/NC_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/NC_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/NC_congress_precomputed.json

echo Computing the geographic baseline for NC/upper ...
scripts/geographic-baseline/once.py \
--state NC \
--plan-type upper \
--data "${DATA_PATH}"/NC_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/NC_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/NC_upper_precomputed.json

echo Computing the geographic baseline for NC/lower ...
scripts/geographic-baseline/once.py \
--state NC \
--plan-type lower \
--data "${DATA_PATH}"/NC_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/NC_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/NC_lower_precomputed.json

echo Computing the geographic baseline for ND/upper ...
scripts/geographic-baseline/once.py \
--state ND \
--plan-type upper \
--data "${DATA_PATH}"/ND_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/ND_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/ND_upper_precomputed.json

echo Computing the geographic baseline for ND/lower ...
scripts/geographic-baseline/once.py \
--state ND \
--plan-type lower \
--data "${DATA_PATH}"/ND_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/ND_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/ND_lower_precomputed.json

echo Computing the geographic baseline for OH/congress ...
scripts/geographic-baseline/once.py \
--state OH \
--plan-type congress \
--data "${DATA_PATH}"/OH_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/OH_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/OH_congress_precomputed.json

echo Computing the geographic baseline for OH/upper ...
scripts/geographic-baseline/once.py \
--state OH \
--plan-type upper \
--data "${DATA_PATH}"/OH_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/OH_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/OH_upper_precomputed.json

echo Computing the geographic baseline for OH/lower ...
scripts/geographic-baseline/once.py \
--state OH \
--plan-type lower \
--data "${DATA_PATH}"/OH_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/OH_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/OH_lower_precomputed.json

echo Computing the geographic baseline for OK/congress ...
scripts/geographic-baseline/once.py \
--state OK \
--plan-type congress \
--data "${DATA_PATH}"/OK_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/OK_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/OK_congress_precomputed.json

echo Computing the geographic baseline for OK/upper ...
scripts/geographic-baseline/once.py \
--state OK \
--plan-type upper \
--data "${DATA_PATH}"/OK_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/OK_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/OK_upper_precomputed.json

echo Computing the geographic baseline for OK/lower ...
scripts/geographic-baseline/once.py \
--state OK \
--plan-type lower \
--data "${DATA_PATH}"/OK_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/OK_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/OK_lower_precomputed.json

echo Computing the geographic baseline for OR/congress ...
scripts/geographic-baseline/once.py \
--state OR \
--plan-type congress \
--data "${DATA_PATH}"/OR_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/OR_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/OR_congress_precomputed.json

echo Computing the geographic baseline for OR/upper ...
scripts/geographic-baseline/once.py \
--state OR \
--plan-type upper \
--data "${DATA_PATH}"/OR_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/OR_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/OR_upper_precomputed.json

echo Computing the geographic baseline for OR/lower ...
scripts/geographic-baseline/once.py \
--state OR \
--plan-type lower \
--data "${DATA_PATH}"/OR_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/OR_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/OR_lower_precomputed.json

echo Computing the geographic baseline for PA/congress ...
scripts/geographic-baseline/once.py \
--state PA \
--plan-type congress \
--data "${DATA_PATH}"/PA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/PA_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/PA_congress_precomputed.json

echo Computing the geographic baseline for PA/upper ...
scripts/geographic-baseline/once.py \
--state PA \
--plan-type upper \
--data "${DATA_PATH}"/PA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/PA_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/PA_upper_precomputed.json

echo Computing the geographic baseline for PA/lower ...
scripts/geographic-baseline/once.py \
--state PA \
--plan-type lower \
--data "${DATA_PATH}"/PA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/PA_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/PA_lower_precomputed.json

echo Computing the geographic baseline for RI/congress ...
scripts/geographic-baseline/once.py \
--state RI \
--plan-type congress \
--data "${DATA_PATH}"/RI_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/RI_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/RI_congress_precomputed.json

echo Computing the geographic baseline for RI/upper ...
scripts/geographic-baseline/once.py \
--state RI \
--plan-type upper \
--data "${DATA_PATH}"/RI_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/RI_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/RI_upper_precomputed.json

echo Computing the geographic baseline for RI/lower ...
scripts/geographic-baseline/once.py \
--state RI \
--plan-type lower \
--data "${DATA_PATH}"/RI_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/RI_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/RI_lower_precomputed.json

echo Computing the geographic baseline for SC/congress ...
scripts/geographic-baseline/once.py \
--state SC \
--plan-type congress \
--data "${DATA_PATH}"/SC_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/SC_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/SC_congress_precomputed.json

echo Computing the geographic baseline for SC/upper ...
scripts/geographic-baseline/once.py \
--state SC \
--plan-type upper \
--data "${DATA_PATH}"/SC_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/SC_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/SC_upper_precomputed.json

echo Computing the geographic baseline for SC/lower ...
scripts/geographic-baseline/once.py \
--state SC \
--plan-type lower \
--data "${DATA_PATH}"/SC_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/SC_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/SC_lower_precomputed.json

echo Computing the geographic baseline for SD/upper ...
scripts/geographic-baseline/once.py \
--state SD \
--plan-type upper \
--data "${DATA_PATH}"/SD_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/SD_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/SD_upper_precomputed.json

echo Computing the geographic baseline for SD/lower ...
scripts/geographic-baseline/once.py \
--state SD \
--plan-type lower \
--data "${DATA_PATH}"/SD_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/SD_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/SD_lower_precomputed.json

echo Computing the geographic baseline for TN/congress ...
scripts/geographic-baseline/once.py \
--state TN \
--plan-type congress \
--data "${DATA_PATH}"/TN_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/TN_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/TN_congress_precomputed.json

echo Computing the geographic baseline for TN/upper ...
scripts/geographic-baseline/once.py \
--state TN \
--plan-type upper \
--data "${DATA_PATH}"/TN_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/TN_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/TN_upper_precomputed.json

echo Computing the geographic baseline for TN/lower ...
scripts/geographic-baseline/once.py \
--state TN \
--plan-type lower \
--data "${DATA_PATH}"/TN_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/TN_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/TN_lower_precomputed.json

echo Computing the geographic baseline for TX/congress ...
scripts/geographic-baseline/once.py \
--state TX \
--plan-type congress \
--data "${DATA_PATH}"/TX_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/TX_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/TX_congress_precomputed.json

echo Computing the geographic baseline for TX/upper ...
scripts/geographic-baseline/once.py \
--state TX \
--plan-type upper \
--data "${DATA_PATH}"/TX_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/TX_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/TX_upper_precomputed.json

echo Computing the geographic baseline for TX/lower ...
scripts/geographic-baseline/once.py \
--state TX \
--plan-type lower \
--data "${DATA_PATH}"/TX_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/TX_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/TX_lower_precomputed.json

echo Computing the geographic baseline for UT/congress ...
scripts/geographic-baseline/once.py \
--state UT \
--plan-type congress \
--data "${DATA_PATH}"/UT_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/UT_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/UT_congress_precomputed.json

echo Computing the geographic baseline for UT/upper ...
scripts/geographic-baseline/once.py \
--state UT \
--plan-type upper \
--data "${DATA_PATH}"/UT_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/UT_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/UT_upper_precomputed.json

echo Computing the geographic baseline for UT/lower ...
scripts/geographic-baseline/once.py \
--state UT \
--plan-type lower \
--data "${DATA_PATH}"/UT_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/UT_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/UT_lower_precomputed.json

echo Computing the geographic baseline for VT/upper ...
scripts/geographic-baseline/once.py \
--state VT \
--plan-type upper \
--data "${DATA_PATH}"/VT_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/VT_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/VT_upper_precomputed.json

echo Computing the geographic baseline for VT/lower ...
scripts/geographic-baseline/once.py \
--state VT \
--plan-type lower \
--data "${DATA_PATH}"/VT_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/VT_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/VT_lower_precomputed.json

echo Computing the geographic baseline for VA/congress ...
scripts/geographic-baseline/once.py \
--state VA \
--plan-type congress \
--data "${DATA_PATH}"/VA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/VA_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/VA_congress_precomputed.json

echo Computing the geographic baseline for VA/upper ...
scripts/geographic-baseline/once.py \
--state VA \
--plan-type upper \
--data "${DATA_PATH}"/VA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/VA_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/VA_upper_precomputed.json

echo Computing the geographic baseline for VA/lower ...
scripts/geographic-baseline/once.py \
--state VA \
--plan-type lower \
--data "${DATA_PATH}"/VA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/VA_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/VA_lower_precomputed.json

echo Computing the geographic baseline for WA/congress ...
scripts/geographic-baseline/once.py \
--state WA \
--plan-type congress \
--data "${DATA_PATH}"/WA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/WA_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/WA_congress_precomputed.json

echo Computing the geographic baseline for WA/upper ...
scripts/geographic-baseline/once.py \
--state WA \
--plan-type upper \
--data "${DATA_PATH}"/WA_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/WA_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/WA_upper_precomputed.json

echo Computing the geographic baseline for WV/congress ...
scripts/geographic-baseline/once.py \
--state WV \
--plan-type congress \
--data "${DATA_PATH}"/WV_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/WV_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/WV_congress_precomputed.json

echo Computing the geographic baseline for WV/upper ...
scripts/geographic-baseline/once.py \
--state WV \
--plan-type upper \
--data "${DATA_PATH}"/WV_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/WV_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/WV_upper_precomputed.json

echo Computing the geographic baseline for WV/lower ...
scripts/geographic-baseline/once.py \
--state WV \
--plan-type lower \
--data "${DATA_PATH}"/WV_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/WV_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/WV_lower_precomputed.json

echo Computing the geographic baseline for WI/congress ...
scripts/geographic-baseline/once.py \
--state WI \
--plan-type congress \
--data "${DATA_PATH}"/WI_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/WI_congress_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/WI_congress_precomputed.json

echo Computing the geographic baseline for WI/upper ...
scripts/geographic-baseline/once.py \
--state WI \
--plan-type upper \
--data "${DATA_PATH}"/WI_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/WI_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/WI_upper_precomputed.json

echo Computing the geographic baseline for WI/lower ...
scripts/geographic-baseline/once.py \
--state WI \
--plan-type lower \
--data "${DATA_PATH}"/WI_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/WI_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/WI_lower_precomputed.json

echo Computing the geographic baseline for WY/upper ...
scripts/geographic-baseline/once.py \
--state WY \
--plan-type upper \
--data "${DATA_PATH}"/WY_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/WY_upper_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/WY_upper_precomputed.json

echo Computing the geographic baseline for WY/lower ...
scripts/geographic-baseline/once.py \
--state WY \
--plan-type lower \
--data "${DATA_PATH}"/WY_input_data."${VERSION}".jsonl \
< "${NEIGHBORHOOD_PATH}"/WY_lower_neighborhoods.jsonl \
> "${PRECOMPUTED_PATH}"/WY_lower_precomputed.json

