#!/bin/bash

echo Finding neighborhoods for AL/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state AL \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/AL_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/AL_2020_graph.json \
> ~/local/geographic-baseline/AL_congress_neighborhoods.jsonl

echo Finding neighborhoods for AL/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state AL \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/AL_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/AL_2020_graph.json \
> ~/local/geographic-baseline/AL_upper_neighborhoods.jsonl

echo Finding neighborhoods for AL/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state AL \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/AL_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/AL_2020_graph.json \
> ~/local/geographic-baseline/AL_lower_neighborhoods.jsonl

echo Finding neighborhoods for AK/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state AK \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/AK_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/AK_2020_graph.json \
> ~/local/geographic-baseline/AK_upper_neighborhoods.jsonl

echo Finding neighborhoods for AK/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state AK \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/AK_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/AK_2020_graph.json \
> ~/local/geographic-baseline/AK_lower_neighborhoods.jsonl

echo Finding neighborhoods for AZ/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state AZ \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/AZ_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/AZ_2020_graph.json \
> ~/local/geographic-baseline/AZ_congress_neighborhoods.jsonl

echo Finding neighborhoods for AZ/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state AZ \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/AZ_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/AZ_2020_graph.json \
> ~/local/geographic-baseline/AZ_upper_neighborhoods.jsonl

echo Finding neighborhoods for AR/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state AR \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/AR_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/AR_2020_graph.json \
> ~/local/geographic-baseline/AR_congress_neighborhoods.jsonl

echo Finding neighborhoods for AR/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state AR \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/AR_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/AR_2020_graph.json \
> ~/local/geographic-baseline/AR_upper_neighborhoods.jsonl

echo Finding neighborhoods for AR/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state AR \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/AR_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/AR_2020_graph.json \
> ~/local/geographic-baseline/AR_lower_neighborhoods.jsonl

echo Finding neighborhoods for CA/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state CA \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/CA_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/CA_2020_graph.json \
> ~/local/geographic-baseline/CA_congress_neighborhoods.jsonl

echo Finding neighborhoods for CA/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state CA \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/CA_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/CA_2020_graph.json \
> ~/local/geographic-baseline/CA_upper_neighborhoods.jsonl

echo Finding neighborhoods for CA/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state CA \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/CA_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/CA_2020_graph.json \
> ~/local/geographic-baseline/CA_lower_neighborhoods.jsonl

echo Finding neighborhoods for CO/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state CO \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/CO_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/CO_2020_graph.json \
> ~/local/geographic-baseline/CO_congress_neighborhoods.jsonl

echo Finding neighborhoods for CO/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state CO \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/CO_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/CO_2020_graph.json \
> ~/local/geographic-baseline/CO_upper_neighborhoods.jsonl

echo Finding neighborhoods for CO/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state CO \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/CO_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/CO_2020_graph.json \
> ~/local/geographic-baseline/CO_lower_neighborhoods.jsonl

echo Finding neighborhoods for CT/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state CT \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/CT_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/CT_2020_graph.json \
> ~/local/geographic-baseline/CT_congress_neighborhoods.jsonl

echo Finding neighborhoods for CT/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state CT \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/CT_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/CT_2020_graph.json \
> ~/local/geographic-baseline/CT_upper_neighborhoods.jsonl

echo Finding neighborhoods for CT/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state CT \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/CT_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/CT_2020_graph.json \
> ~/local/geographic-baseline/CT_lower_neighborhoods.jsonl

echo Finding neighborhoods for DE/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state DE \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/DE_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/DE_2020_graph.json \
> ~/local/geographic-baseline/DE_upper_neighborhoods.jsonl

echo Finding neighborhoods for DE/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state DE \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/DE_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/DE_2020_graph.json \
> ~/local/geographic-baseline/DE_lower_neighborhoods.jsonl

echo Finding neighborhoods for FL/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state FL \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/FL_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/FL_2020_graph.json \
> ~/local/geographic-baseline/FL_congress_neighborhoods.jsonl

echo Finding neighborhoods for FL/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state FL \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/FL_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/FL_2020_graph.json \
> ~/local/geographic-baseline/FL_upper_neighborhoods.jsonl

echo Finding neighborhoods for FL/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state FL \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/FL_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/FL_2020_graph.json \
> ~/local/geographic-baseline/FL_lower_neighborhoods.jsonl

echo Finding neighborhoods for GA/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state GA \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/GA_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/GA_2020_graph.json \
> ~/local/geographic-baseline/GA_congress_neighborhoods.jsonl

echo Finding neighborhoods for GA/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state GA \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/GA_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/GA_2020_graph.json \
> ~/local/geographic-baseline/GA_upper_neighborhoods.jsonl

echo Finding neighborhoods for GA/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state GA \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/GA_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/GA_2020_graph.json \
> ~/local/geographic-baseline/GA_lower_neighborhoods.jsonl

echo Finding neighborhoods for HI/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state HI \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/HI_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/HI_2020_graph.json \
> ~/local/geographic-baseline/HI_congress_neighborhoods.jsonl

echo Finding neighborhoods for HI/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state HI \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/HI_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/HI_2020_graph.json \
> ~/local/geographic-baseline/HI_upper_neighborhoods.jsonl

echo Finding neighborhoods for HI/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state HI \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/HI_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/HI_2020_graph.json \
> ~/local/geographic-baseline/HI_lower_neighborhoods.jsonl

echo Finding neighborhoods for ID/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state ID \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/ID_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/ID_2020_graph.json \
> ~/local/geographic-baseline/ID_congress_neighborhoods.jsonl

echo Finding neighborhoods for ID/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state ID \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/ID_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/ID_2020_graph.json \
> ~/local/geographic-baseline/ID_upper_neighborhoods.jsonl

echo Finding neighborhoods for IL/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state IL \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/IL_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/IL_2020_graph.json \
> ~/local/geographic-baseline/IL_congress_neighborhoods.jsonl

echo Finding neighborhoods for IL/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state IL \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/IL_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/IL_2020_graph.json \
> ~/local/geographic-baseline/IL_upper_neighborhoods.jsonl

echo Finding neighborhoods for IL/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state IL \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/IL_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/IL_2020_graph.json \
> ~/local/geographic-baseline/IL_lower_neighborhoods.jsonl

echo Finding neighborhoods for IN/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state IN \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/IN_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/IN_2020_graph.json \
> ~/local/geographic-baseline/IN_congress_neighborhoods.jsonl

echo Finding neighborhoods for IN/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state IN \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/IN_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/IN_2020_graph.json \
> ~/local/geographic-baseline/IN_upper_neighborhoods.jsonl

echo Finding neighborhoods for IN/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state IN \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/IN_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/IN_2020_graph.json \
> ~/local/geographic-baseline/IN_lower_neighborhoods.jsonl

echo Finding neighborhoods for IA/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state IA \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/IA_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/IA_2020_graph.json \
> ~/local/geographic-baseline/IA_congress_neighborhoods.jsonl

echo Finding neighborhoods for IA/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state IA \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/IA_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/IA_2020_graph.json \
> ~/local/geographic-baseline/IA_upper_neighborhoods.jsonl

echo Finding neighborhoods for IA/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state IA \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/IA_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/IA_2020_graph.json \
> ~/local/geographic-baseline/IA_lower_neighborhoods.jsonl

echo Finding neighborhoods for KS/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state KS \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/KS_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/KS_2020_graph.json \
> ~/local/geographic-baseline/KS_congress_neighborhoods.jsonl

echo Finding neighborhoods for KS/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state KS \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/KS_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/KS_2020_graph.json \
> ~/local/geographic-baseline/KS_upper_neighborhoods.jsonl

echo Finding neighborhoods for KS/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state KS \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/KS_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/KS_2020_graph.json \
> ~/local/geographic-baseline/KS_lower_neighborhoods.jsonl

echo Finding neighborhoods for KY/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state KY \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/KY_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/KY_2020_graph.json \
> ~/local/geographic-baseline/KY_congress_neighborhoods.jsonl

echo Finding neighborhoods for KY/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state KY \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/KY_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/KY_2020_graph.json \
> ~/local/geographic-baseline/KY_upper_neighborhoods.jsonl

echo Finding neighborhoods for KY/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state KY \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/KY_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/KY_2020_graph.json \
> ~/local/geographic-baseline/KY_lower_neighborhoods.jsonl

echo Finding neighborhoods for LA/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state LA \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/LA_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/LA_2020_graph.json \
> ~/local/geographic-baseline/LA_congress_neighborhoods.jsonl

echo Finding neighborhoods for LA/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state LA \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/LA_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/LA_2020_graph.json \
> ~/local/geographic-baseline/LA_upper_neighborhoods.jsonl

echo Finding neighborhoods for LA/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state LA \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/LA_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/LA_2020_graph.json \
> ~/local/geographic-baseline/LA_lower_neighborhoods.jsonl

echo Finding neighborhoods for ME/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state ME \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/ME_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/ME_2020_graph.json \
> ~/local/geographic-baseline/ME_congress_neighborhoods.jsonl

echo Finding neighborhoods for ME/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state ME \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/ME_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/ME_2020_graph.json \
> ~/local/geographic-baseline/ME_upper_neighborhoods.jsonl

echo Finding neighborhoods for ME/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state ME \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/ME_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/ME_2020_graph.json \
> ~/local/geographic-baseline/ME_lower_neighborhoods.jsonl

echo Finding neighborhoods for MD/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MD \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/MD_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/MD_2020_graph.json \
> ~/local/geographic-baseline/MD_congress_neighborhoods.jsonl

echo Finding neighborhoods for MD/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MD \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/MD_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/MD_2020_graph.json \
> ~/local/geographic-baseline/MD_upper_neighborhoods.jsonl

echo Finding neighborhoods for MD/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MD \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/MD_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/MD_2020_graph.json \
> ~/local/geographic-baseline/MD_lower_neighborhoods.jsonl

echo Finding neighborhoods for MA/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MA \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/MA_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/MA_2020_graph.json \
> ~/local/geographic-baseline/MA_congress_neighborhoods.jsonl

echo Finding neighborhoods for MA/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MA \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/MA_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/MA_2020_graph.json \
> ~/local/geographic-baseline/MA_upper_neighborhoods.jsonl

echo Finding neighborhoods for MA/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MA \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/MA_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/MA_2020_graph.json \
> ~/local/geographic-baseline/MA_lower_neighborhoods.jsonl

echo Finding neighborhoods for MI/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MI \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/MI_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/MI_2020_graph.json \
> ~/local/geographic-baseline/MI_congress_neighborhoods.jsonl

echo Finding neighborhoods for MI/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MI \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/MI_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/MI_2020_graph.json \
> ~/local/geographic-baseline/MI_upper_neighborhoods.jsonl

echo Finding neighborhoods for MI/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MI \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/MI_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/MI_2020_graph.json \
> ~/local/geographic-baseline/MI_lower_neighborhoods.jsonl

echo Finding neighborhoods for MN/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MN \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/MN_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/MN_2020_graph.json \
> ~/local/geographic-baseline/MN_congress_neighborhoods.jsonl

echo Finding neighborhoods for MN/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MN \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/MN_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/MN_2020_graph.json \
> ~/local/geographic-baseline/MN_upper_neighborhoods.jsonl

echo Finding neighborhoods for MN/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MN \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/MN_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/MN_2020_graph.json \
> ~/local/geographic-baseline/MN_lower_neighborhoods.jsonl

echo Finding neighborhoods for MS/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MS \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/MS_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/MS_2020_graph.json \
> ~/local/geographic-baseline/MS_congress_neighborhoods.jsonl

echo Finding neighborhoods for MS/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MS \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/MS_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/MS_2020_graph.json \
> ~/local/geographic-baseline/MS_upper_neighborhoods.jsonl

echo Finding neighborhoods for MS/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MS \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/MS_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/MS_2020_graph.json \
> ~/local/geographic-baseline/MS_lower_neighborhoods.jsonl

echo Finding neighborhoods for MO/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MO \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/MO_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/MO_2020_graph.json \
> ~/local/geographic-baseline/MO_congress_neighborhoods.jsonl

echo Finding neighborhoods for MO/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MO \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/MO_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/MO_2020_graph.json \
> ~/local/geographic-baseline/MO_upper_neighborhoods.jsonl

echo Finding neighborhoods for MO/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MO \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/MO_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/MO_2020_graph.json \
> ~/local/geographic-baseline/MO_lower_neighborhoods.jsonl

echo Finding neighborhoods for MT/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MT \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/MT_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/MT_2020_graph.json \
> ~/local/geographic-baseline/MT_congress_neighborhoods.jsonl

echo Finding neighborhoods for MT/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MT \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/MT_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/MT_2020_graph.json \
> ~/local/geographic-baseline/MT_upper_neighborhoods.jsonl

echo Finding neighborhoods for MT/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state MT \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/MT_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/MT_2020_graph.json \
> ~/local/geographic-baseline/MT_lower_neighborhoods.jsonl

echo Finding neighborhoods for NE/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state NE \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/NE_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/NE_2020_graph.json \
> ~/local/geographic-baseline/NE_congress_neighborhoods.jsonl

echo Finding neighborhoods for NE/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state NE \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/NE_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/NE_2020_graph.json \
> ~/local/geographic-baseline/NE_upper_neighborhoods.jsonl

echo Finding neighborhoods for NV/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state NV \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/NV_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/NV_2020_graph.json \
> ~/local/geographic-baseline/NV_congress_neighborhoods.jsonl

echo Finding neighborhoods for NV/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state NV \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/NV_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/NV_2020_graph.json \
> ~/local/geographic-baseline/NV_upper_neighborhoods.jsonl

echo Finding neighborhoods for NV/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state NV \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/NV_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/NV_2020_graph.json \
> ~/local/geographic-baseline/NV_lower_neighborhoods.jsonl

echo Finding neighborhoods for NH/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state NH \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/NH_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/NH_2020_graph.json \
> ~/local/geographic-baseline/NH_congress_neighborhoods.jsonl

echo Finding neighborhoods for NH/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state NH \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/NH_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/NH_2020_graph.json \
> ~/local/geographic-baseline/NH_upper_neighborhoods.jsonl

echo Finding neighborhoods for NH/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state NH \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/NH_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/NH_2020_graph.json \
> ~/local/geographic-baseline/NH_lower_neighborhoods.jsonl

echo Finding neighborhoods for NJ/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state NJ \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/NJ_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/NJ_2020_graph.json \
> ~/local/geographic-baseline/NJ_congress_neighborhoods.jsonl

echo Finding neighborhoods for NJ/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state NJ \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/NJ_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/NJ_2020_graph.json \
> ~/local/geographic-baseline/NJ_upper_neighborhoods.jsonl

echo Finding neighborhoods for NM/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state NM \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/NM_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/NM_2020_graph.json \
> ~/local/geographic-baseline/NM_congress_neighborhoods.jsonl

echo Finding neighborhoods for NM/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state NM \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/NM_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/NM_2020_graph.json \
> ~/local/geographic-baseline/NM_upper_neighborhoods.jsonl

echo Finding neighborhoods for NM/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state NM \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/NM_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/NM_2020_graph.json \
> ~/local/geographic-baseline/NM_lower_neighborhoods.jsonl

echo Finding neighborhoods for NY/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state NY \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/NY_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/NY_2020_graph.json \
> ~/local/geographic-baseline/NY_congress_neighborhoods.jsonl

echo Finding neighborhoods for NY/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state NY \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/NY_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/NY_2020_graph.json \
> ~/local/geographic-baseline/NY_upper_neighborhoods.jsonl

echo Finding neighborhoods for NY/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state NY \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/NY_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/NY_2020_graph.json \
> ~/local/geographic-baseline/NY_lower_neighborhoods.jsonl

echo Finding neighborhoods for NC/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state NC \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/NC_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/NC_2020_graph.json \
> ~/local/geographic-baseline/NC_congress_neighborhoods.jsonl

echo Finding neighborhoods for NC/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state NC \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/NC_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/NC_2020_graph.json \
> ~/local/geographic-baseline/NC_upper_neighborhoods.jsonl

echo Finding neighborhoods for NC/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state NC \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/NC_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/NC_2020_graph.json \
> ~/local/geographic-baseline/NC_lower_neighborhoods.jsonl

echo Finding neighborhoods for ND/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state ND \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/ND_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/ND_2020_graph.json \
> ~/local/geographic-baseline/ND_upper_neighborhoods.jsonl

echo Finding neighborhoods for ND/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state ND \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/ND_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/ND_2020_graph.json \
> ~/local/geographic-baseline/ND_lower_neighborhoods.jsonl

echo Finding neighborhoods for OH/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state OH \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/OH_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/OH_2020_graph.json \
> ~/local/geographic-baseline/OH_congress_neighborhoods.jsonl

echo Finding neighborhoods for OH/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state OH \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/OH_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/OH_2020_graph.json \
> ~/local/geographic-baseline/OH_upper_neighborhoods.jsonl

echo Finding neighborhoods for OH/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state OH \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/OH_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/OH_2020_graph.json \
> ~/local/geographic-baseline/OH_lower_neighborhoods.jsonl

echo Finding neighborhoods for OK/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state OK \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/OK_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/OK_2020_graph.json \
> ~/local/geographic-baseline/OK_congress_neighborhoods.jsonl

echo Finding neighborhoods for OK/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state OK \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/OK_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/OK_2020_graph.json \
> ~/local/geographic-baseline/OK_upper_neighborhoods.jsonl

echo Finding neighborhoods for OK/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state OK \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/OK_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/OK_2020_graph.json \
> ~/local/geographic-baseline/OK_lower_neighborhoods.jsonl

echo Finding neighborhoods for OR/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state OR \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/OR_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/OR_2020_graph.json \
> ~/local/geographic-baseline/OR_congress_neighborhoods.jsonl

echo Finding neighborhoods for OR/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state OR \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/OR_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/OR_2020_graph.json \
> ~/local/geographic-baseline/OR_upper_neighborhoods.jsonl

echo Finding neighborhoods for OR/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state OR \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/OR_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/OR_2020_graph.json \
> ~/local/geographic-baseline/OR_lower_neighborhoods.jsonl

echo Finding neighborhoods for PA/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state PA \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/PA_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/PA_2020_graph.json \
> ~/local/geographic-baseline/PA_congress_neighborhoods.jsonl

echo Finding neighborhoods for PA/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state PA \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/PA_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/PA_2020_graph.json \
> ~/local/geographic-baseline/PA_upper_neighborhoods.jsonl

echo Finding neighborhoods for PA/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state PA \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/PA_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/PA_2020_graph.json \
> ~/local/geographic-baseline/PA_lower_neighborhoods.jsonl

echo Finding neighborhoods for RI/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state RI \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/RI_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/RI_2020_graph.json \
> ~/local/geographic-baseline/RI_congress_neighborhoods.jsonl

echo Finding neighborhoods for RI/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state RI \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/RI_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/RI_2020_graph.json \
> ~/local/geographic-baseline/RI_upper_neighborhoods.jsonl

echo Finding neighborhoods for RI/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state RI \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/RI_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/RI_2020_graph.json \
> ~/local/geographic-baseline/RI_lower_neighborhoods.jsonl

echo Finding neighborhoods for SC/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state SC \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/SC_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/SC_2020_graph.json \
> ~/local/geographic-baseline/SC_congress_neighborhoods.jsonl

echo Finding neighborhoods for SC/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state SC \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/SC_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/SC_2020_graph.json \
> ~/local/geographic-baseline/SC_upper_neighborhoods.jsonl

echo Finding neighborhoods for SC/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state SC \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/SC_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/SC_2020_graph.json \
> ~/local/geographic-baseline/SC_lower_neighborhoods.jsonl

echo Finding neighborhoods for SD/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state SD \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/SD_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/SD_2020_graph.json \
> ~/local/geographic-baseline/SD_upper_neighborhoods.jsonl

echo Finding neighborhoods for SD/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state SD \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/SD_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/SD_2020_graph.json \
> ~/local/geographic-baseline/SD_lower_neighborhoods.jsonl

echo Finding neighborhoods for TN/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state TN \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/TN_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/TN_2020_graph.json \
> ~/local/geographic-baseline/TN_congress_neighborhoods.jsonl

echo Finding neighborhoods for TN/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state TN \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/TN_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/TN_2020_graph.json \
> ~/local/geographic-baseline/TN_upper_neighborhoods.jsonl

echo Finding neighborhoods for TN/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state TN \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/TN_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/TN_2020_graph.json \
> ~/local/geographic-baseline/TN_lower_neighborhoods.jsonl

echo Finding neighborhoods for TX/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state TX \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/TX_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/TX_2020_graph.json \
> ~/local/geographic-baseline/TX_congress_neighborhoods.jsonl

echo Finding neighborhoods for TX/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state TX \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/TX_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/TX_2020_graph.json \
> ~/local/geographic-baseline/TX_upper_neighborhoods.jsonl

echo Finding neighborhoods for TX/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state TX \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/TX_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/TX_2020_graph.json \
> ~/local/geographic-baseline/TX_lower_neighborhoods.jsonl

echo Finding neighborhoods for UT/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state UT \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/UT_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/UT_2020_graph.json \
> ~/local/geographic-baseline/UT_congress_neighborhoods.jsonl

echo Finding neighborhoods for UT/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state UT \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/UT_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/UT_2020_graph.json \
> ~/local/geographic-baseline/UT_upper_neighborhoods.jsonl

echo Finding neighborhoods for UT/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state UT \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/UT_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/UT_2020_graph.json \
> ~/local/geographic-baseline/UT_lower_neighborhoods.jsonl

echo Finding neighborhoods for VT/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state VT \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/VT_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/VT_2020_graph.json \
> ~/local/geographic-baseline/VT_upper_neighborhoods.jsonl

echo Finding neighborhoods for VT/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state VT \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/VT_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/VT_2020_graph.json \
> ~/local/geographic-baseline/VT_lower_neighborhoods.jsonl

echo Finding neighborhoods for VA/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state VA \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/VA_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/VA_2020_graph.json \
> ~/local/geographic-baseline/VA_congress_neighborhoods.jsonl

echo Finding neighborhoods for VA/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state VA \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/VA_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/VA_2020_graph.json \
> ~/local/geographic-baseline/VA_upper_neighborhoods.jsonl

echo Finding neighborhoods for VA/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state VA \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/VA_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/VA_2020_graph.json \
> ~/local/geographic-baseline/VA_lower_neighborhoods.jsonl

echo Finding neighborhoods for WA/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state WA \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/WA_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/WA_2020_graph.json \
> ~/local/geographic-baseline/WA_congress_neighborhoods.jsonl

echo Finding neighborhoods for WA/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state WA \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/WA_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/WA_2020_graph.json \
> ~/local/geographic-baseline/WA_upper_neighborhoods.jsonl

echo Finding neighborhoods for WV/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state WV \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/WV_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/WV_2020_graph.json \
> ~/local/geographic-baseline/WV_congress_neighborhoods.jsonl

echo Finding neighborhoods for WV/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state WV \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/WV_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/WV_2020_graph.json \
> ~/local/geographic-baseline/WV_upper_neighborhoods.jsonl

echo Finding neighborhoods for WV/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state WV \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/WV_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/WV_2020_graph.json \
> ~/local/geographic-baseline/WV_lower_neighborhoods.jsonl

echo Finding neighborhoods for WI/congress ...
scripts/geographic-baseline/find_neighborhoods.py \
--state WI \
--plan-type congress \
--slack 0.0 \
--data ~/local/temp-data/WI_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/WI_2020_graph.json \
> ~/local/geographic-baseline/WI_congress_neighborhoods.jsonl

echo Finding neighborhoods for WI/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state WI \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/WI_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/WI_2020_graph.json \
> ~/local/geographic-baseline/WI_upper_neighborhoods.jsonl

echo Finding neighborhoods for WI/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state WI \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/WI_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/WI_2020_graph.json \
> ~/local/geographic-baseline/WI_lower_neighborhoods.jsonl

echo Finding neighborhoods for WY/upper ...
scripts/geographic-baseline/find_neighborhoods.py \
--state WY \
--plan-type upper \
--slack 0.0 \
--data ~/local/temp-data/WY_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/WY_2020_graph.json \
> ~/local/geographic-baseline/WY_upper_neighborhoods.jsonl

echo Finding neighborhoods for WY/lower ...
scripts/geographic-baseline/find_neighborhoods.py \
--state WY \
--plan-type lower \
--slack 0.0 \
--data ~/local/temp-data/WY_input_data.v4.jsonl \
--graph ~/local/dra-to-publish/WY_2020_graph.json \
> ~/local/geographic-baseline/WY_lower_neighborhoods.jsonl

