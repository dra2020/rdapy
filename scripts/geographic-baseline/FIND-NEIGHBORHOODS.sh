#!/bin/bash

CYCLE=2020
DATA_PATH=~/local/temp-data # TODO
VERSION=v5
GRAPH_PATH=~/local/adjacency-graphs # TODO
NEIGHBORHOOD_PATH=temp
rm -rf "${NEIGHBORHOOD_PATH}/*_neighborhoods.jsonl"

echo Finding neighborhoods for AL/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state AL \
--plan-type congress \
--data "${DATA_PATH}"/AL_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/AL"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/AL_congress_neighborhoods.jsonl

echo Finding neighborhoods for AL/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state AL \
--plan-type upper \
--data "${DATA_PATH}"/AL_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/AL"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/AL_upper_neighborhoods.jsonl

echo Finding neighborhoods for AL/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state AL \
--plan-type lower \
--data "${DATA_PATH}"/AL_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/AL"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/AL_lower_neighborhoods.jsonl

echo Finding neighborhoods for AK/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state AK \
--plan-type upper \
--data "${DATA_PATH}"/AK_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/AK"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/AK_upper_neighborhoods.jsonl

echo Finding neighborhoods for AK/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state AK \
--plan-type lower \
--data "${DATA_PATH}"/AK_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/AK"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/AK_lower_neighborhoods.jsonl

echo Finding neighborhoods for AZ/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state AZ \
--plan-type congress \
--data "${DATA_PATH}"/AZ_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/AZ"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/AZ_congress_neighborhoods.jsonl

echo Finding neighborhoods for AZ/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state AZ \
--plan-type upper \
--data "${DATA_PATH}"/AZ_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/AZ"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/AZ_upper_neighborhoods.jsonl

echo Finding neighborhoods for AR/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state AR \
--plan-type congress \
--data "${DATA_PATH}"/AR_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/AR"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/AR_congress_neighborhoods.jsonl

echo Finding neighborhoods for AR/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state AR \
--plan-type upper \
--data "${DATA_PATH}"/AR_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/AR"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/AR_upper_neighborhoods.jsonl

echo Finding neighborhoods for AR/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state AR \
--plan-type lower \
--data "${DATA_PATH}"/AR_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/AR"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/AR_lower_neighborhoods.jsonl

echo Finding neighborhoods for CA/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state CA \
--plan-type congress \
--data "${DATA_PATH}"/CA_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/CA"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/CA_congress_neighborhoods.jsonl

echo Finding neighborhoods for CA/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state CA \
--plan-type upper \
--data "${DATA_PATH}"/CA_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/CA"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/CA_upper_neighborhoods.jsonl

echo Finding neighborhoods for CA/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state CA \
--plan-type lower \
--data "${DATA_PATH}"/CA_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/CA"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/CA_lower_neighborhoods.jsonl

echo Finding neighborhoods for CO/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state CO \
--plan-type congress \
--data "${DATA_PATH}"/CO_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/CO"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/CO_congress_neighborhoods.jsonl

echo Finding neighborhoods for CO/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state CO \
--plan-type upper \
--data "${DATA_PATH}"/CO_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/CO"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/CO_upper_neighborhoods.jsonl

echo Finding neighborhoods for CO/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state CO \
--plan-type lower \
--data "${DATA_PATH}"/CO_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/CO"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/CO_lower_neighborhoods.jsonl

echo Finding neighborhoods for CT/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state CT \
--plan-type congress \
--data "${DATA_PATH}"/CT_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/CT"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/CT_congress_neighborhoods.jsonl

echo Finding neighborhoods for CT/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state CT \
--plan-type upper \
--data "${DATA_PATH}"/CT_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/CT"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/CT_upper_neighborhoods.jsonl

echo Finding neighborhoods for CT/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state CT \
--plan-type lower \
--data "${DATA_PATH}"/CT_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/CT"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/CT_lower_neighborhoods.jsonl

echo Finding neighborhoods for DE/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state DE \
--plan-type upper \
--data "${DATA_PATH}"/DE_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/DE"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/DE_upper_neighborhoods.jsonl

echo Finding neighborhoods for DE/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state DE \
--plan-type lower \
--data "${DATA_PATH}"/DE_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/DE"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/DE_lower_neighborhoods.jsonl

echo Finding neighborhoods for FL/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state FL \
--plan-type congress \
--data "${DATA_PATH}"/FL_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/FL"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/FL_congress_neighborhoods.jsonl

echo Finding neighborhoods for FL/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state FL \
--plan-type upper \
--data "${DATA_PATH}"/FL_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/FL"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/FL_upper_neighborhoods.jsonl

echo Finding neighborhoods for FL/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state FL \
--plan-type lower \
--data "${DATA_PATH}"/FL_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/FL"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/FL_lower_neighborhoods.jsonl

echo Finding neighborhoods for GA/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state GA \
--plan-type congress \
--data "${DATA_PATH}"/GA_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/GA"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/GA_congress_neighborhoods.jsonl

echo Finding neighborhoods for GA/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state GA \
--plan-type upper \
--data "${DATA_PATH}"/GA_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/GA"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/GA_upper_neighborhoods.jsonl

echo Finding neighborhoods for GA/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state GA \
--plan-type lower \
--data "${DATA_PATH}"/GA_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/GA"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/GA_lower_neighborhoods.jsonl

echo Finding neighborhoods for HI/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state HI \
--plan-type congress \
--data "${DATA_PATH}"/HI_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/HI"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/HI_congress_neighborhoods.jsonl

echo Finding neighborhoods for HI/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state HI \
--plan-type upper \
--data "${DATA_PATH}"/HI_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/HI"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/HI_upper_neighborhoods.jsonl

echo Finding neighborhoods for HI/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state HI \
--plan-type lower \
--data "${DATA_PATH}"/HI_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/HI"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/HI_lower_neighborhoods.jsonl

echo Finding neighborhoods for ID/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state ID \
--plan-type congress \
--data "${DATA_PATH}"/ID_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/ID"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/ID_congress_neighborhoods.jsonl

echo Finding neighborhoods for ID/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state ID \
--plan-type upper \
--data "${DATA_PATH}"/ID_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/ID"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/ID_upper_neighborhoods.jsonl

echo Finding neighborhoods for IL/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state IL \
--plan-type congress \
--data "${DATA_PATH}"/IL_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/IL"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/IL_congress_neighborhoods.jsonl

echo Finding neighborhoods for IL/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state IL \
--plan-type upper \
--data "${DATA_PATH}"/IL_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/IL"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/IL_upper_neighborhoods.jsonl

echo Finding neighborhoods for IL/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state IL \
--plan-type lower \
--data "${DATA_PATH}"/IL_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/IL"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/IL_lower_neighborhoods.jsonl

echo Finding neighborhoods for IN/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state IN \
--plan-type congress \
--data "${DATA_PATH}"/IN_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/IN"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/IN_congress_neighborhoods.jsonl

echo Finding neighborhoods for IN/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state IN \
--plan-type upper \
--data "${DATA_PATH}"/IN_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/IN"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/IN_upper_neighborhoods.jsonl

echo Finding neighborhoods for IN/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state IN \
--plan-type lower \
--data "${DATA_PATH}"/IN_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/IN"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/IN_lower_neighborhoods.jsonl

echo Finding neighborhoods for IA/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state IA \
--plan-type congress \
--data "${DATA_PATH}"/IA_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/IA"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/IA_congress_neighborhoods.jsonl

echo Finding neighborhoods for IA/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state IA \
--plan-type upper \
--data "${DATA_PATH}"/IA_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/IA"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/IA_upper_neighborhoods.jsonl

echo Finding neighborhoods for IA/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state IA \
--plan-type lower \
--data "${DATA_PATH}"/IA_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/IA"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/IA_lower_neighborhoods.jsonl

echo Finding neighborhoods for KS/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state KS \
--plan-type congress \
--data "${DATA_PATH}"/KS_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/KS"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/KS_congress_neighborhoods.jsonl

echo Finding neighborhoods for KS/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state KS \
--plan-type upper \
--data "${DATA_PATH}"/KS_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/KS"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/KS_upper_neighborhoods.jsonl

echo Finding neighborhoods for KS/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state KS \
--plan-type lower \
--data "${DATA_PATH}"/KS_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/KS"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/KS_lower_neighborhoods.jsonl

echo Finding neighborhoods for KY/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state KY \
--plan-type congress \
--data "${DATA_PATH}"/KY_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/KY"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/KY_congress_neighborhoods.jsonl

echo Finding neighborhoods for KY/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state KY \
--plan-type upper \
--data "${DATA_PATH}"/KY_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/KY"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/KY_upper_neighborhoods.jsonl

echo Finding neighborhoods for KY/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state KY \
--plan-type lower \
--data "${DATA_PATH}"/KY_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/KY"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/KY_lower_neighborhoods.jsonl

echo Finding neighborhoods for LA/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state LA \
--plan-type congress \
--data "${DATA_PATH}"/LA_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/LA"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/LA_congress_neighborhoods.jsonl

echo Finding neighborhoods for LA/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state LA \
--plan-type upper \
--data "${DATA_PATH}"/LA_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/LA"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/LA_upper_neighborhoods.jsonl

echo Finding neighborhoods for LA/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state LA \
--plan-type lower \
--data "${DATA_PATH}"/LA_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/LA"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/LA_lower_neighborhoods.jsonl

echo Finding neighborhoods for ME/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state ME \
--plan-type congress \
--data "${DATA_PATH}"/ME_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/ME"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/ME_congress_neighborhoods.jsonl

echo Finding neighborhoods for ME/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state ME \
--plan-type upper \
--data "${DATA_PATH}"/ME_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/ME"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/ME_upper_neighborhoods.jsonl

echo Finding neighborhoods for ME/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state ME \
--plan-type lower \
--data "${DATA_PATH}"/ME_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/ME"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/ME_lower_neighborhoods.jsonl

echo Finding neighborhoods for MD/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MD \
--plan-type congress \
--data "${DATA_PATH}"/MD_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/MD"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/MD_congress_neighborhoods.jsonl

echo Finding neighborhoods for MD/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MD \
--plan-type upper \
--data "${DATA_PATH}"/MD_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/MD"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/MD_upper_neighborhoods.jsonl

echo Finding neighborhoods for MD/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MD \
--plan-type lower \
--data "${DATA_PATH}"/MD_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/MD"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/MD_lower_neighborhoods.jsonl

echo Finding neighborhoods for MA/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MA \
--plan-type congress \
--data "${DATA_PATH}"/MA_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/MA"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/MA_congress_neighborhoods.jsonl

echo Finding neighborhoods for MA/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MA \
--plan-type upper \
--data "${DATA_PATH}"/MA_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/MA"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/MA_upper_neighborhoods.jsonl

echo Finding neighborhoods for MA/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MA \
--plan-type lower \
--data "${DATA_PATH}"/MA_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/MA"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/MA_lower_neighborhoods.jsonl

echo Finding neighborhoods for MI/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MI \
--plan-type congress \
--data "${DATA_PATH}"/MI_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/MI"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/MI_congress_neighborhoods.jsonl

echo Finding neighborhoods for MI/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MI \
--plan-type upper \
--data "${DATA_PATH}"/MI_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/MI"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/MI_upper_neighborhoods.jsonl

echo Finding neighborhoods for MI/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MI \
--plan-type lower \
--data "${DATA_PATH}"/MI_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/MI"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/MI_lower_neighborhoods.jsonl

echo Finding neighborhoods for MN/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MN \
--plan-type congress \
--data "${DATA_PATH}"/MN_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/MN"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/MN_congress_neighborhoods.jsonl

echo Finding neighborhoods for MN/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MN \
--plan-type upper \
--data "${DATA_PATH}"/MN_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/MN"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/MN_upper_neighborhoods.jsonl

echo Finding neighborhoods for MN/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MN \
--plan-type lower \
--data "${DATA_PATH}"/MN_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/MN"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/MN_lower_neighborhoods.jsonl

echo Finding neighborhoods for MS/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MS \
--plan-type congress \
--data "${DATA_PATH}"/MS_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/MS"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/MS_congress_neighborhoods.jsonl

echo Finding neighborhoods for MS/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MS \
--plan-type upper \
--data "${DATA_PATH}"/MS_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/MS"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/MS_upper_neighborhoods.jsonl

echo Finding neighborhoods for MS/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MS \
--plan-type lower \
--data "${DATA_PATH}"/MS_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/MS"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/MS_lower_neighborhoods.jsonl

echo Finding neighborhoods for MO/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MO \
--plan-type congress \
--data "${DATA_PATH}"/MO_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/MO"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/MO_congress_neighborhoods.jsonl

echo Finding neighborhoods for MO/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MO \
--plan-type upper \
--data "${DATA_PATH}"/MO_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/MO"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/MO_upper_neighborhoods.jsonl

echo Finding neighborhoods for MO/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MO \
--plan-type lower \
--data "${DATA_PATH}"/MO_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/MO"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/MO_lower_neighborhoods.jsonl

echo Finding neighborhoods for MT/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MT \
--plan-type congress \
--data "${DATA_PATH}"/MT_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/MT"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/MT_congress_neighborhoods.jsonl

echo Finding neighborhoods for MT/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MT \
--plan-type upper \
--data "${DATA_PATH}"/MT_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/MT"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/MT_upper_neighborhoods.jsonl

echo Finding neighborhoods for MT/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MT \
--plan-type lower \
--data "${DATA_PATH}"/MT_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/MT"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/MT_lower_neighborhoods.jsonl

echo Finding neighborhoods for NE/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state NE \
--plan-type congress \
--data "${DATA_PATH}"/NE_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/NE"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/NE_congress_neighborhoods.jsonl

echo Finding neighborhoods for NE/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state NE \
--plan-type upper \
--data "${DATA_PATH}"/NE_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/NE"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/NE_upper_neighborhoods.jsonl

echo Finding neighborhoods for NV/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state NV \
--plan-type congress \
--data "${DATA_PATH}"/NV_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/NV"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/NV_congress_neighborhoods.jsonl

echo Finding neighborhoods for NV/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state NV \
--plan-type upper \
--data "${DATA_PATH}"/NV_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/NV"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/NV_upper_neighborhoods.jsonl

echo Finding neighborhoods for NV/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state NV \
--plan-type lower \
--data "${DATA_PATH}"/NV_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/NV"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/NV_lower_neighborhoods.jsonl

echo Finding neighborhoods for NH/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state NH \
--plan-type congress \
--data "${DATA_PATH}"/NH_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/NH"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/NH_congress_neighborhoods.jsonl

echo Finding neighborhoods for NH/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state NH \
--plan-type upper \
--data "${DATA_PATH}"/NH_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/NH"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/NH_upper_neighborhoods.jsonl

echo Finding neighborhoods for NH/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state NH \
--plan-type lower \
--data "${DATA_PATH}"/NH_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/NH"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/NH_lower_neighborhoods.jsonl

echo Finding neighborhoods for NJ/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state NJ \
--plan-type congress \
--data "${DATA_PATH}"/NJ_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/NJ"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/NJ_congress_neighborhoods.jsonl

echo Finding neighborhoods for NJ/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state NJ \
--plan-type upper \
--data "${DATA_PATH}"/NJ_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/NJ"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/NJ_upper_neighborhoods.jsonl

echo Finding neighborhoods for NM/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state NM \
--plan-type congress \
--data "${DATA_PATH}"/NM_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/NM"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/NM_congress_neighborhoods.jsonl

echo Finding neighborhoods for NM/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state NM \
--plan-type upper \
--data "${DATA_PATH}"/NM_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/NM"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/NM_upper_neighborhoods.jsonl

echo Finding neighborhoods for NM/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state NM \
--plan-type lower \
--data "${DATA_PATH}"/NM_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/NM"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/NM_lower_neighborhoods.jsonl

echo Finding neighborhoods for NY/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state NY \
--plan-type congress \
--data "${DATA_PATH}"/NY_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/NY"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/NY_congress_neighborhoods.jsonl

echo Finding neighborhoods for NY/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state NY \
--plan-type upper \
--data "${DATA_PATH}"/NY_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/NY"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/NY_upper_neighborhoods.jsonl

echo Finding neighborhoods for NY/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state NY \
--plan-type lower \
--data "${DATA_PATH}"/NY_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/NY"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/NY_lower_neighborhoods.jsonl

echo Finding neighborhoods for NC/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state NC \
--plan-type congress \
--data "${DATA_PATH}"/NC_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/NC"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/NC_congress_neighborhoods.jsonl

echo Finding neighborhoods for NC/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state NC \
--plan-type upper \
--data "${DATA_PATH}"/NC_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/NC"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/NC_upper_neighborhoods.jsonl

echo Finding neighborhoods for NC/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state NC \
--plan-type lower \
--data "${DATA_PATH}"/NC_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/NC"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/NC_lower_neighborhoods.jsonl

echo Finding neighborhoods for ND/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state ND \
--plan-type upper \
--data "${DATA_PATH}"/ND_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/ND"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/ND_upper_neighborhoods.jsonl

echo Finding neighborhoods for ND/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state ND \
--plan-type lower \
--data "${DATA_PATH}"/ND_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/ND"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/ND_lower_neighborhoods.jsonl

echo Finding neighborhoods for OH/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state OH \
--plan-type congress \
--data "${DATA_PATH}"/OH_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/OH"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/OH_congress_neighborhoods.jsonl

echo Finding neighborhoods for OH/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state OH \
--plan-type upper \
--data "${DATA_PATH}"/OH_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/OH"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/OH_upper_neighborhoods.jsonl

echo Finding neighborhoods for OH/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state OH \
--plan-type lower \
--data "${DATA_PATH}"/OH_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/OH"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/OH_lower_neighborhoods.jsonl

echo Finding neighborhoods for OK/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state OK \
--plan-type congress \
--data "${DATA_PATH}"/OK_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/OK"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/OK_congress_neighborhoods.jsonl

echo Finding neighborhoods for OK/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state OK \
--plan-type upper \
--data "${DATA_PATH}"/OK_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/OK"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/OK_upper_neighborhoods.jsonl

echo Finding neighborhoods for OK/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state OK \
--plan-type lower \
--data "${DATA_PATH}"/OK_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/OK"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/OK_lower_neighborhoods.jsonl

echo Finding neighborhoods for OR/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state OR \
--plan-type congress \
--data "${DATA_PATH}"/OR_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/OR"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/OR_congress_neighborhoods.jsonl

echo Finding neighborhoods for OR/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state OR \
--plan-type upper \
--data "${DATA_PATH}"/OR_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/OR"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/OR_upper_neighborhoods.jsonl

echo Finding neighborhoods for OR/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state OR \
--plan-type lower \
--data "${DATA_PATH}"/OR_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/OR"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/OR_lower_neighborhoods.jsonl

echo Finding neighborhoods for PA/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state PA \
--plan-type congress \
--data "${DATA_PATH}"/PA_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/PA"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/PA_congress_neighborhoods.jsonl

echo Finding neighborhoods for PA/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state PA \
--plan-type upper \
--data "${DATA_PATH}"/PA_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/PA"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/PA_upper_neighborhoods.jsonl

echo Finding neighborhoods for PA/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state PA \
--plan-type lower \
--data "${DATA_PATH}"/PA_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/PA"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/PA_lower_neighborhoods.jsonl

echo Finding neighborhoods for RI/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state RI \
--plan-type congress \
--data "${DATA_PATH}"/RI_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/RI"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/RI_congress_neighborhoods.jsonl

echo Finding neighborhoods for RI/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state RI \
--plan-type upper \
--data "${DATA_PATH}"/RI_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/RI"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/RI_upper_neighborhoods.jsonl

echo Finding neighborhoods for RI/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state RI \
--plan-type lower \
--data "${DATA_PATH}"/RI_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/RI"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/RI_lower_neighborhoods.jsonl

echo Finding neighborhoods for SC/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state SC \
--plan-type congress \
--data "${DATA_PATH}"/SC_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/SC"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/SC_congress_neighborhoods.jsonl

echo Finding neighborhoods for SC/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state SC \
--plan-type upper \
--data "${DATA_PATH}"/SC_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/SC"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/SC_upper_neighborhoods.jsonl

echo Finding neighborhoods for SC/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state SC \
--plan-type lower \
--data "${DATA_PATH}"/SC_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/SC"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/SC_lower_neighborhoods.jsonl

echo Finding neighborhoods for SD/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state SD \
--plan-type upper \
--data "${DATA_PATH}"/SD_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/SD"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/SD_upper_neighborhoods.jsonl

echo Finding neighborhoods for SD/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state SD \
--plan-type lower \
--data "${DATA_PATH}"/SD_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/SD"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/SD_lower_neighborhoods.jsonl

echo Finding neighborhoods for TN/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state TN \
--plan-type congress \
--data "${DATA_PATH}"/TN_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/TN"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/TN_congress_neighborhoods.jsonl

echo Finding neighborhoods for TN/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state TN \
--plan-type upper \
--data "${DATA_PATH}"/TN_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/TN"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/TN_upper_neighborhoods.jsonl

echo Finding neighborhoods for TN/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state TN \
--plan-type lower \
--data "${DATA_PATH}"/TN_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/TN"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/TN_lower_neighborhoods.jsonl

echo Finding neighborhoods for TX/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state TX \
--plan-type congress \
--data "${DATA_PATH}"/TX_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/TX"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/TX_congress_neighborhoods.jsonl

echo Finding neighborhoods for TX/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state TX \
--plan-type upper \
--data "${DATA_PATH}"/TX_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/TX"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/TX_upper_neighborhoods.jsonl

echo Finding neighborhoods for TX/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state TX \
--plan-type lower \
--data "${DATA_PATH}"/TX_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/TX"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/TX_lower_neighborhoods.jsonl

echo Finding neighborhoods for UT/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state UT \
--plan-type congress \
--data "${DATA_PATH}"/UT_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/UT"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/UT_congress_neighborhoods.jsonl

echo Finding neighborhoods for UT/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state UT \
--plan-type upper \
--data "${DATA_PATH}"/UT_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/UT"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/UT_upper_neighborhoods.jsonl

echo Finding neighborhoods for UT/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state UT \
--plan-type lower \
--data "${DATA_PATH}"/UT_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/UT"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/UT_lower_neighborhoods.jsonl

echo Finding neighborhoods for VT/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state VT \
--plan-type upper \
--data "${DATA_PATH}"/VT_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/VT"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/VT_upper_neighborhoods.jsonl

echo Finding neighborhoods for VT/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state VT \
--plan-type lower \
--data "${DATA_PATH}"/VT_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/VT"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/VT_lower_neighborhoods.jsonl

echo Finding neighborhoods for VA/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state VA \
--plan-type congress \
--data "${DATA_PATH}"/VA_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/VA"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/VA_congress_neighborhoods.jsonl

echo Finding neighborhoods for VA/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state VA \
--plan-type upper \
--data "${DATA_PATH}"/VA_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/VA"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/VA_upper_neighborhoods.jsonl

echo Finding neighborhoods for VA/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state VA \
--plan-type lower \
--data "${DATA_PATH}"/VA_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/VA"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/VA_lower_neighborhoods.jsonl

echo Finding neighborhoods for WA/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state WA \
--plan-type congress \
--data "${DATA_PATH}"/WA_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/WA"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/WA_congress_neighborhoods.jsonl

echo Finding neighborhoods for WA/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state WA \
--plan-type upper \
--data "${DATA_PATH}"/WA_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/WA"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/WA_upper_neighborhoods.jsonl

echo Finding neighborhoods for WV/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state WV \
--plan-type congress \
--data "${DATA_PATH}"/WV_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/WV"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/WV_congress_neighborhoods.jsonl

echo Finding neighborhoods for WV/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state WV \
--plan-type upper \
--data "${DATA_PATH}"/WV_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/WV"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/WV_upper_neighborhoods.jsonl

echo Finding neighborhoods for WV/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state WV \
--plan-type lower \
--data "${DATA_PATH}"/WV_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/WV"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/WV_lower_neighborhoods.jsonl

echo Finding neighborhoods for WI/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state WI \
--plan-type congress \
--data "${DATA_PATH}"/WI_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/WI"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/WI_congress_neighborhoods.jsonl

echo Finding neighborhoods for WI/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state WI \
--plan-type upper \
--data "${DATA_PATH}"/WI_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/WI"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/WI_upper_neighborhoods.jsonl

echo Finding neighborhoods for WI/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state WI \
--plan-type lower \
--data "${DATA_PATH}"/WI_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/WI"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/WI_lower_neighborhoods.jsonl

echo Finding neighborhoods for WY/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state WY \
--plan-type upper \
--data "${DATA_PATH}"/WY_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/WY"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/WY_upper_neighborhoods.jsonl

echo Finding neighborhoods for WY/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state WY \
--plan-type lower \
--data "${DATA_PATH}"/WY_input_data."${VERSION}"jsonl \
--graph "${GRAPH_PATH}"/WY"${CYCLE}"graph.json \
> "${NEIGHBORHOOD_PATH}"/WY_lower_neighborhoods.jsonl

