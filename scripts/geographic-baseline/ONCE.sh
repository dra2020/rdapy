#!/bin/bash

echo Computing the geographic baseline for AL/congress ...
scripts/once.py \
--state AL \
--plan-type congress \
--data ~/local/temp-data/AL_input_data.v4.jsonl \
< ~/local/geographic-baseline/AL_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/AL_congress_precomputed.json

echo Computing the geographic baseline for AL/upper ...
scripts/once.py \
--state AL \
--plan-type upper \
--data ~/local/temp-data/AL_input_data.v4.jsonl \
< ~/local/geographic-baseline/AL_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/AL_upper_precomputed.json

echo Computing the geographic baseline for AL/lower ...
scripts/once.py \
--state AL \
--plan-type lower \
--data ~/local/temp-data/AL_input_data.v4.jsonl \
< ~/local/geographic-baseline/AL_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/AL_lower_precomputed.json

echo Computing the geographic baseline for AK/upper ...
scripts/once.py \
--state AK \
--plan-type upper \
--data ~/local/temp-data/AK_input_data.v4.jsonl \
< ~/local/geographic-baseline/AK_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/AK_upper_precomputed.json

echo Computing the geographic baseline for AK/lower ...
scripts/once.py \
--state AK \
--plan-type lower \
--data ~/local/temp-data/AK_input_data.v4.jsonl \
< ~/local/geographic-baseline/AK_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/AK_lower_precomputed.json

echo Computing the geographic baseline for AZ/congress ...
scripts/once.py \
--state AZ \
--plan-type congress \
--data ~/local/temp-data/AZ_input_data.v4.jsonl \
< ~/local/geographic-baseline/AZ_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/AZ_congress_precomputed.json

echo Computing the geographic baseline for AZ/upper ...
scripts/once.py \
--state AZ \
--plan-type upper \
--data ~/local/temp-data/AZ_input_data.v4.jsonl \
< ~/local/geographic-baseline/AZ_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/AZ_upper_precomputed.json

echo Computing the geographic baseline for AR/congress ...
scripts/once.py \
--state AR \
--plan-type congress \
--data ~/local/temp-data/AR_input_data.v4.jsonl \
< ~/local/geographic-baseline/AR_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/AR_congress_precomputed.json

echo Computing the geographic baseline for AR/upper ...
scripts/once.py \
--state AR \
--plan-type upper \
--data ~/local/temp-data/AR_input_data.v4.jsonl \
< ~/local/geographic-baseline/AR_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/AR_upper_precomputed.json

echo Computing the geographic baseline for AR/lower ...
scripts/once.py \
--state AR \
--plan-type lower \
--data ~/local/temp-data/AR_input_data.v4.jsonl \
< ~/local/geographic-baseline/AR_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/AR_lower_precomputed.json

echo Computing the geographic baseline for CA/congress ...
scripts/once.py \
--state CA \
--plan-type congress \
--data ~/local/temp-data/CA_input_data.v4.jsonl \
< ~/local/geographic-baseline/CA_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/CA_congress_precomputed.json

echo Computing the geographic baseline for CA/upper ...
scripts/once.py \
--state CA \
--plan-type upper \
--data ~/local/temp-data/CA_input_data.v4.jsonl \
< ~/local/geographic-baseline/CA_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/CA_upper_precomputed.json

echo Computing the geographic baseline for CA/lower ...
scripts/once.py \
--state CA \
--plan-type lower \
--data ~/local/temp-data/CA_input_data.v4.jsonl \
< ~/local/geographic-baseline/CA_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/CA_lower_precomputed.json

echo Computing the geographic baseline for CO/congress ...
scripts/once.py \
--state CO \
--plan-type congress \
--data ~/local/temp-data/CO_input_data.v4.jsonl \
< ~/local/geographic-baseline/CO_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/CO_congress_precomputed.json

echo Computing the geographic baseline for CO/upper ...
scripts/once.py \
--state CO \
--plan-type upper \
--data ~/local/temp-data/CO_input_data.v4.jsonl \
< ~/local/geographic-baseline/CO_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/CO_upper_precomputed.json

echo Computing the geographic baseline for CO/lower ...
scripts/once.py \
--state CO \
--plan-type lower \
--data ~/local/temp-data/CO_input_data.v4.jsonl \
< ~/local/geographic-baseline/CO_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/CO_lower_precomputed.json

echo Computing the geographic baseline for CT/congress ...
scripts/once.py \
--state CT \
--plan-type congress \
--data ~/local/temp-data/CT_input_data.v4.jsonl \
< ~/local/geographic-baseline/CT_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/CT_congress_precomputed.json

echo Computing the geographic baseline for CT/upper ...
scripts/once.py \
--state CT \
--plan-type upper \
--data ~/local/temp-data/CT_input_data.v4.jsonl \
< ~/local/geographic-baseline/CT_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/CT_upper_precomputed.json

echo Computing the geographic baseline for CT/lower ...
scripts/once.py \
--state CT \
--plan-type lower \
--data ~/local/temp-data/CT_input_data.v4.jsonl \
< ~/local/geographic-baseline/CT_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/CT_lower_precomputed.json

echo Computing the geographic baseline for DE/upper ...
scripts/once.py \
--state DE \
--plan-type upper \
--data ~/local/temp-data/DE_input_data.v4.jsonl \
< ~/local/geographic-baseline/DE_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/DE_upper_precomputed.json

echo Computing the geographic baseline for DE/lower ...
scripts/once.py \
--state DE \
--plan-type lower \
--data ~/local/temp-data/DE_input_data.v4.jsonl \
< ~/local/geographic-baseline/DE_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/DE_lower_precomputed.json

echo Computing the geographic baseline for FL/congress ...
scripts/once.py \
--state FL \
--plan-type congress \
--data ~/local/temp-data/FL_input_data.v4.jsonl \
< ~/local/geographic-baseline/FL_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/FL_congress_precomputed.json

echo Computing the geographic baseline for FL/upper ...
scripts/once.py \
--state FL \
--plan-type upper \
--data ~/local/temp-data/FL_input_data.v4.jsonl \
< ~/local/geographic-baseline/FL_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/FL_upper_precomputed.json

echo Computing the geographic baseline for FL/lower ...
scripts/once.py \
--state FL \
--plan-type lower \
--data ~/local/temp-data/FL_input_data.v4.jsonl \
< ~/local/geographic-baseline/FL_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/FL_lower_precomputed.json

echo Computing the geographic baseline for GA/congress ...
scripts/once.py \
--state GA \
--plan-type congress \
--data ~/local/temp-data/GA_input_data.v4.jsonl \
< ~/local/geographic-baseline/GA_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/GA_congress_precomputed.json

echo Computing the geographic baseline for GA/upper ...
scripts/once.py \
--state GA \
--plan-type upper \
--data ~/local/temp-data/GA_input_data.v4.jsonl \
< ~/local/geographic-baseline/GA_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/GA_upper_precomputed.json

echo Computing the geographic baseline for GA/lower ...
scripts/once.py \
--state GA \
--plan-type lower \
--data ~/local/temp-data/GA_input_data.v4.jsonl \
< ~/local/geographic-baseline/GA_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/GA_lower_precomputed.json

echo Computing the geographic baseline for HI/congress ...
scripts/once.py \
--state HI \
--plan-type congress \
--data ~/local/temp-data/HI_input_data.v4.jsonl \
< ~/local/geographic-baseline/HI_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/HI_congress_precomputed.json

echo Computing the geographic baseline for HI/upper ...
scripts/once.py \
--state HI \
--plan-type upper \
--data ~/local/temp-data/HI_input_data.v4.jsonl \
< ~/local/geographic-baseline/HI_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/HI_upper_precomputed.json

echo Computing the geographic baseline for HI/lower ...
scripts/once.py \
--state HI \
--plan-type lower \
--data ~/local/temp-data/HI_input_data.v4.jsonl \
< ~/local/geographic-baseline/HI_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/HI_lower_precomputed.json

echo Computing the geographic baseline for ID/congress ...
scripts/once.py \
--state ID \
--plan-type congress \
--data ~/local/temp-data/ID_input_data.v4.jsonl \
< ~/local/geographic-baseline/ID_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/ID_congress_precomputed.json

echo Computing the geographic baseline for ID/upper ...
scripts/once.py \
--state ID \
--plan-type upper \
--data ~/local/temp-data/ID_input_data.v4.jsonl \
< ~/local/geographic-baseline/ID_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/ID_upper_precomputed.json

echo Computing the geographic baseline for IL/congress ...
scripts/once.py \
--state IL \
--plan-type congress \
--data ~/local/temp-data/IL_input_data.v4.jsonl \
< ~/local/geographic-baseline/IL_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/IL_congress_precomputed.json

echo Computing the geographic baseline for IL/upper ...
scripts/once.py \
--state IL \
--plan-type upper \
--data ~/local/temp-data/IL_input_data.v4.jsonl \
< ~/local/geographic-baseline/IL_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/IL_upper_precomputed.json

echo Computing the geographic baseline for IL/lower ...
scripts/once.py \
--state IL \
--plan-type lower \
--data ~/local/temp-data/IL_input_data.v4.jsonl \
< ~/local/geographic-baseline/IL_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/IL_lower_precomputed.json

echo Computing the geographic baseline for IN/congress ...
scripts/once.py \
--state IN \
--plan-type congress \
--data ~/local/temp-data/IN_input_data.v4.jsonl \
< ~/local/geographic-baseline/IN_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/IN_congress_precomputed.json

echo Computing the geographic baseline for IN/upper ...
scripts/once.py \
--state IN \
--plan-type upper \
--data ~/local/temp-data/IN_input_data.v4.jsonl \
< ~/local/geographic-baseline/IN_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/IN_upper_precomputed.json

echo Computing the geographic baseline for IN/lower ...
scripts/once.py \
--state IN \
--plan-type lower \
--data ~/local/temp-data/IN_input_data.v4.jsonl \
< ~/local/geographic-baseline/IN_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/IN_lower_precomputed.json

echo Computing the geographic baseline for IA/congress ...
scripts/once.py \
--state IA \
--plan-type congress \
--data ~/local/temp-data/IA_input_data.v4.jsonl \
< ~/local/geographic-baseline/IA_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/IA_congress_precomputed.json

echo Computing the geographic baseline for IA/upper ...
scripts/once.py \
--state IA \
--plan-type upper \
--data ~/local/temp-data/IA_input_data.v4.jsonl \
< ~/local/geographic-baseline/IA_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/IA_upper_precomputed.json

echo Computing the geographic baseline for IA/lower ...
scripts/once.py \
--state IA \
--plan-type lower \
--data ~/local/temp-data/IA_input_data.v4.jsonl \
< ~/local/geographic-baseline/IA_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/IA_lower_precomputed.json

echo Computing the geographic baseline for KS/congress ...
scripts/once.py \
--state KS \
--plan-type congress \
--data ~/local/temp-data/KS_input_data.v4.jsonl \
< ~/local/geographic-baseline/KS_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/KS_congress_precomputed.json

echo Computing the geographic baseline for KS/upper ...
scripts/once.py \
--state KS \
--plan-type upper \
--data ~/local/temp-data/KS_input_data.v4.jsonl \
< ~/local/geographic-baseline/KS_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/KS_upper_precomputed.json

echo Computing the geographic baseline for KS/lower ...
scripts/once.py \
--state KS \
--plan-type lower \
--data ~/local/temp-data/KS_input_data.v4.jsonl \
< ~/local/geographic-baseline/KS_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/KS_lower_precomputed.json

echo Computing the geographic baseline for KY/congress ...
scripts/once.py \
--state KY \
--plan-type congress \
--data ~/local/temp-data/KY_input_data.v4.jsonl \
< ~/local/geographic-baseline/KY_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/KY_congress_precomputed.json

echo Computing the geographic baseline for KY/upper ...
scripts/once.py \
--state KY \
--plan-type upper \
--data ~/local/temp-data/KY_input_data.v4.jsonl \
< ~/local/geographic-baseline/KY_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/KY_upper_precomputed.json

echo Computing the geographic baseline for KY/lower ...
scripts/once.py \
--state KY \
--plan-type lower \
--data ~/local/temp-data/KY_input_data.v4.jsonl \
< ~/local/geographic-baseline/KY_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/KY_lower_precomputed.json

echo Computing the geographic baseline for LA/congress ...
scripts/once.py \
--state LA \
--plan-type congress \
--data ~/local/temp-data/LA_input_data.v4.jsonl \
< ~/local/geographic-baseline/LA_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/LA_congress_precomputed.json

echo Computing the geographic baseline for LA/upper ...
scripts/once.py \
--state LA \
--plan-type upper \
--data ~/local/temp-data/LA_input_data.v4.jsonl \
< ~/local/geographic-baseline/LA_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/LA_upper_precomputed.json

echo Computing the geographic baseline for LA/lower ...
scripts/once.py \
--state LA \
--plan-type lower \
--data ~/local/temp-data/LA_input_data.v4.jsonl \
< ~/local/geographic-baseline/LA_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/LA_lower_precomputed.json

echo Computing the geographic baseline for ME/congress ...
scripts/once.py \
--state ME \
--plan-type congress \
--data ~/local/temp-data/ME_input_data.v4.jsonl \
< ~/local/geographic-baseline/ME_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/ME_congress_precomputed.json

echo Computing the geographic baseline for ME/upper ...
scripts/once.py \
--state ME \
--plan-type upper \
--data ~/local/temp-data/ME_input_data.v4.jsonl \
< ~/local/geographic-baseline/ME_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/ME_upper_precomputed.json

echo Computing the geographic baseline for ME/lower ...
scripts/once.py \
--state ME \
--plan-type lower \
--data ~/local/temp-data/ME_input_data.v4.jsonl \
< ~/local/geographic-baseline/ME_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/ME_lower_precomputed.json

echo Computing the geographic baseline for MD/congress ...
scripts/once.py \
--state MD \
--plan-type congress \
--data ~/local/temp-data/MD_input_data.v4.jsonl \
< ~/local/geographic-baseline/MD_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/MD_congress_precomputed.json

echo Computing the geographic baseline for MD/upper ...
scripts/once.py \
--state MD \
--plan-type upper \
--data ~/local/temp-data/MD_input_data.v4.jsonl \
< ~/local/geographic-baseline/MD_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/MD_upper_precomputed.json

echo Computing the geographic baseline for MD/lower ...
scripts/once.py \
--state MD \
--plan-type lower \
--data ~/local/temp-data/MD_input_data.v4.jsonl \
< ~/local/geographic-baseline/MD_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/MD_lower_precomputed.json

echo Computing the geographic baseline for MA/congress ...
scripts/once.py \
--state MA \
--plan-type congress \
--data ~/local/temp-data/MA_input_data.v4.jsonl \
< ~/local/geographic-baseline/MA_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/MA_congress_precomputed.json

echo Computing the geographic baseline for MA/upper ...
scripts/once.py \
--state MA \
--plan-type upper \
--data ~/local/temp-data/MA_input_data.v4.jsonl \
< ~/local/geographic-baseline/MA_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/MA_upper_precomputed.json

echo Computing the geographic baseline for MA/lower ...
scripts/once.py \
--state MA \
--plan-type lower \
--data ~/local/temp-data/MA_input_data.v4.jsonl \
< ~/local/geographic-baseline/MA_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/MA_lower_precomputed.json

echo Computing the geographic baseline for MI/congress ...
scripts/once.py \
--state MI \
--plan-type congress \
--data ~/local/temp-data/MI_input_data.v4.jsonl \
< ~/local/geographic-baseline/MI_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/MI_congress_precomputed.json

echo Computing the geographic baseline for MI/upper ...
scripts/once.py \
--state MI \
--plan-type upper \
--data ~/local/temp-data/MI_input_data.v4.jsonl \
< ~/local/geographic-baseline/MI_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/MI_upper_precomputed.json

echo Computing the geographic baseline for MI/lower ...
scripts/once.py \
--state MI \
--plan-type lower \
--data ~/local/temp-data/MI_input_data.v4.jsonl \
< ~/local/geographic-baseline/MI_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/MI_lower_precomputed.json

echo Computing the geographic baseline for MN/congress ...
scripts/once.py \
--state MN \
--plan-type congress \
--data ~/local/temp-data/MN_input_data.v4.jsonl \
< ~/local/geographic-baseline/MN_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/MN_congress_precomputed.json

echo Computing the geographic baseline for MN/upper ...
scripts/once.py \
--state MN \
--plan-type upper \
--data ~/local/temp-data/MN_input_data.v4.jsonl \
< ~/local/geographic-baseline/MN_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/MN_upper_precomputed.json

echo Computing the geographic baseline for MN/lower ...
scripts/once.py \
--state MN \
--plan-type lower \
--data ~/local/temp-data/MN_input_data.v4.jsonl \
< ~/local/geographic-baseline/MN_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/MN_lower_precomputed.json

echo Computing the geographic baseline for MS/congress ...
scripts/once.py \
--state MS \
--plan-type congress \
--data ~/local/temp-data/MS_input_data.v4.jsonl \
< ~/local/geographic-baseline/MS_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/MS_congress_precomputed.json

echo Computing the geographic baseline for MS/upper ...
scripts/once.py \
--state MS \
--plan-type upper \
--data ~/local/temp-data/MS_input_data.v4.jsonl \
< ~/local/geographic-baseline/MS_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/MS_upper_precomputed.json

echo Computing the geographic baseline for MS/lower ...
scripts/once.py \
--state MS \
--plan-type lower \
--data ~/local/temp-data/MS_input_data.v4.jsonl \
< ~/local/geographic-baseline/MS_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/MS_lower_precomputed.json

echo Computing the geographic baseline for MO/congress ...
scripts/once.py \
--state MO \
--plan-type congress \
--data ~/local/temp-data/MO_input_data.v4.jsonl \
< ~/local/geographic-baseline/MO_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/MO_congress_precomputed.json

echo Computing the geographic baseline for MO/upper ...
scripts/once.py \
--state MO \
--plan-type upper \
--data ~/local/temp-data/MO_input_data.v4.jsonl \
< ~/local/geographic-baseline/MO_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/MO_upper_precomputed.json

echo Computing the geographic baseline for MO/lower ...
scripts/once.py \
--state MO \
--plan-type lower \
--data ~/local/temp-data/MO_input_data.v4.jsonl \
< ~/local/geographic-baseline/MO_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/MO_lower_precomputed.json

echo Computing the geographic baseline for MT/congress ...
scripts/once.py \
--state MT \
--plan-type congress \
--data ~/local/temp-data/MT_input_data.v4.jsonl \
< ~/local/geographic-baseline/MT_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/MT_congress_precomputed.json

echo Computing the geographic baseline for MT/upper ...
scripts/once.py \
--state MT \
--plan-type upper \
--data ~/local/temp-data/MT_input_data.v4.jsonl \
< ~/local/geographic-baseline/MT_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/MT_upper_precomputed.json

echo Computing the geographic baseline for MT/lower ...
scripts/once.py \
--state MT \
--plan-type lower \
--data ~/local/temp-data/MT_input_data.v4.jsonl \
< ~/local/geographic-baseline/MT_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/MT_lower_precomputed.json

echo Computing the geographic baseline for NE/congress ...
scripts/once.py \
--state NE \
--plan-type congress \
--data ~/local/temp-data/NE_input_data.v4.jsonl \
< ~/local/geographic-baseline/NE_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/NE_congress_precomputed.json

echo Computing the geographic baseline for NE/upper ...
scripts/once.py \
--state NE \
--plan-type upper \
--data ~/local/temp-data/NE_input_data.v4.jsonl \
< ~/local/geographic-baseline/NE_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/NE_upper_precomputed.json

echo Computing the geographic baseline for NV/congress ...
scripts/once.py \
--state NV \
--plan-type congress \
--data ~/local/temp-data/NV_input_data.v4.jsonl \
< ~/local/geographic-baseline/NV_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/NV_congress_precomputed.json

echo Computing the geographic baseline for NV/upper ...
scripts/once.py \
--state NV \
--plan-type upper \
--data ~/local/temp-data/NV_input_data.v4.jsonl \
< ~/local/geographic-baseline/NV_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/NV_upper_precomputed.json

echo Computing the geographic baseline for NV/lower ...
scripts/once.py \
--state NV \
--plan-type lower \
--data ~/local/temp-data/NV_input_data.v4.jsonl \
< ~/local/geographic-baseline/NV_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/NV_lower_precomputed.json

echo Computing the geographic baseline for NH/congress ...
scripts/once.py \
--state NH \
--plan-type congress \
--data ~/local/temp-data/NH_input_data.v4.jsonl \
< ~/local/geographic-baseline/NH_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/NH_congress_precomputed.json

echo Computing the geographic baseline for NH/upper ...
scripts/once.py \
--state NH \
--plan-type upper \
--data ~/local/temp-data/NH_input_data.v4.jsonl \
< ~/local/geographic-baseline/NH_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/NH_upper_precomputed.json

echo Computing the geographic baseline for NH/lower ...
scripts/once.py \
--state NH \
--plan-type lower \
--data ~/local/temp-data/NH_input_data.v4.jsonl \
< ~/local/geographic-baseline/NH_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/NH_lower_precomputed.json

echo Computing the geographic baseline for NJ/congress ...
scripts/once.py \
--state NJ \
--plan-type congress \
--data ~/local/temp-data/NJ_input_data.v4.jsonl \
< ~/local/geographic-baseline/NJ_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/NJ_congress_precomputed.json

echo Computing the geographic baseline for NJ/upper ...
scripts/once.py \
--state NJ \
--plan-type upper \
--data ~/local/temp-data/NJ_input_data.v4.jsonl \
< ~/local/geographic-baseline/NJ_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/NJ_upper_precomputed.json

echo Computing the geographic baseline for NM/congress ...
scripts/once.py \
--state NM \
--plan-type congress \
--data ~/local/temp-data/NM_input_data.v4.jsonl \
< ~/local/geographic-baseline/NM_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/NM_congress_precomputed.json

echo Computing the geographic baseline for NM/upper ...
scripts/once.py \
--state NM \
--plan-type upper \
--data ~/local/temp-data/NM_input_data.v4.jsonl \
< ~/local/geographic-baseline/NM_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/NM_upper_precomputed.json

echo Computing the geographic baseline for NM/lower ...
scripts/once.py \
--state NM \
--plan-type lower \
--data ~/local/temp-data/NM_input_data.v4.jsonl \
< ~/local/geographic-baseline/NM_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/NM_lower_precomputed.json

echo Computing the geographic baseline for NY/congress ...
scripts/once.py \
--state NY \
--plan-type congress \
--data ~/local/temp-data/NY_input_data.v4.jsonl \
< ~/local/geographic-baseline/NY_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/NY_congress_precomputed.json

echo Computing the geographic baseline for NY/upper ...
scripts/once.py \
--state NY \
--plan-type upper \
--data ~/local/temp-data/NY_input_data.v4.jsonl \
< ~/local/geographic-baseline/NY_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/NY_upper_precomputed.json

echo Computing the geographic baseline for NY/lower ...
scripts/once.py \
--state NY \
--plan-type lower \
--data ~/local/temp-data/NY_input_data.v4.jsonl \
< ~/local/geographic-baseline/NY_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/NY_lower_precomputed.json

echo Computing the geographic baseline for NC/congress ...
scripts/once.py \
--state NC \
--plan-type congress \
--data ~/local/temp-data/NC_input_data.v4.jsonl \
< ~/local/geographic-baseline/NC_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/NC_congress_precomputed.json

echo Computing the geographic baseline for NC/upper ...
scripts/once.py \
--state NC \
--plan-type upper \
--data ~/local/temp-data/NC_input_data.v4.jsonl \
< ~/local/geographic-baseline/NC_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/NC_upper_precomputed.json

echo Computing the geographic baseline for NC/lower ...
scripts/once.py \
--state NC \
--plan-type lower \
--data ~/local/temp-data/NC_input_data.v4.jsonl \
< ~/local/geographic-baseline/NC_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/NC_lower_precomputed.json

echo Computing the geographic baseline for ND/upper ...
scripts/once.py \
--state ND \
--plan-type upper \
--data ~/local/temp-data/ND_input_data.v4.jsonl \
< ~/local/geographic-baseline/ND_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/ND_upper_precomputed.json

echo Computing the geographic baseline for ND/lower ...
scripts/once.py \
--state ND \
--plan-type lower \
--data ~/local/temp-data/ND_input_data.v4.jsonl \
< ~/local/geographic-baseline/ND_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/ND_lower_precomputed.json

echo Computing the geographic baseline for OH/congress ...
scripts/once.py \
--state OH \
--plan-type congress \
--data ~/local/temp-data/OH_input_data.v4.jsonl \
< ~/local/geographic-baseline/OH_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/OH_congress_precomputed.json

echo Computing the geographic baseline for OH/upper ...
scripts/once.py \
--state OH \
--plan-type upper \
--data ~/local/temp-data/OH_input_data.v4.jsonl \
< ~/local/geographic-baseline/OH_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/OH_upper_precomputed.json

echo Computing the geographic baseline for OH/lower ...
scripts/once.py \
--state OH \
--plan-type lower \
--data ~/local/temp-data/OH_input_data.v4.jsonl \
< ~/local/geographic-baseline/OH_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/OH_lower_precomputed.json

echo Computing the geographic baseline for OK/congress ...
scripts/once.py \
--state OK \
--plan-type congress \
--data ~/local/temp-data/OK_input_data.v4.jsonl \
< ~/local/geographic-baseline/OK_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/OK_congress_precomputed.json

echo Computing the geographic baseline for OK/upper ...
scripts/once.py \
--state OK \
--plan-type upper \
--data ~/local/temp-data/OK_input_data.v4.jsonl \
< ~/local/geographic-baseline/OK_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/OK_upper_precomputed.json

echo Computing the geographic baseline for OK/lower ...
scripts/once.py \
--state OK \
--plan-type lower \
--data ~/local/temp-data/OK_input_data.v4.jsonl \
< ~/local/geographic-baseline/OK_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/OK_lower_precomputed.json

echo Computing the geographic baseline for OR/congress ...
scripts/once.py \
--state OR \
--plan-type congress \
--data ~/local/temp-data/OR_input_data.v4.jsonl \
< ~/local/geographic-baseline/OR_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/OR_congress_precomputed.json

echo Computing the geographic baseline for OR/upper ...
scripts/once.py \
--state OR \
--plan-type upper \
--data ~/local/temp-data/OR_input_data.v4.jsonl \
< ~/local/geographic-baseline/OR_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/OR_upper_precomputed.json

echo Computing the geographic baseline for OR/lower ...
scripts/once.py \
--state OR \
--plan-type lower \
--data ~/local/temp-data/OR_input_data.v4.jsonl \
< ~/local/geographic-baseline/OR_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/OR_lower_precomputed.json

echo Computing the geographic baseline for PA/congress ...
scripts/once.py \
--state PA \
--plan-type congress \
--data ~/local/temp-data/PA_input_data.v4.jsonl \
< ~/local/geographic-baseline/PA_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/PA_congress_precomputed.json

echo Computing the geographic baseline for PA/upper ...
scripts/once.py \
--state PA \
--plan-type upper \
--data ~/local/temp-data/PA_input_data.v4.jsonl \
< ~/local/geographic-baseline/PA_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/PA_upper_precomputed.json

echo Computing the geographic baseline for PA/lower ...
scripts/once.py \
--state PA \
--plan-type lower \
--data ~/local/temp-data/PA_input_data.v4.jsonl \
< ~/local/geographic-baseline/PA_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/PA_lower_precomputed.json

echo Computing the geographic baseline for RI/congress ...
scripts/once.py \
--state RI \
--plan-type congress \
--data ~/local/temp-data/RI_input_data.v4.jsonl \
< ~/local/geographic-baseline/RI_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/RI_congress_precomputed.json

echo Computing the geographic baseline for RI/upper ...
scripts/once.py \
--state RI \
--plan-type upper \
--data ~/local/temp-data/RI_input_data.v4.jsonl \
< ~/local/geographic-baseline/RI_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/RI_upper_precomputed.json

echo Computing the geographic baseline for RI/lower ...
scripts/once.py \
--state RI \
--plan-type lower \
--data ~/local/temp-data/RI_input_data.v4.jsonl \
< ~/local/geographic-baseline/RI_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/RI_lower_precomputed.json

echo Computing the geographic baseline for SC/congress ...
scripts/once.py \
--state SC \
--plan-type congress \
--data ~/local/temp-data/SC_input_data.v4.jsonl \
< ~/local/geographic-baseline/SC_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/SC_congress_precomputed.json

echo Computing the geographic baseline for SC/upper ...
scripts/once.py \
--state SC \
--plan-type upper \
--data ~/local/temp-data/SC_input_data.v4.jsonl \
< ~/local/geographic-baseline/SC_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/SC_upper_precomputed.json

echo Computing the geographic baseline for SC/lower ...
scripts/once.py \
--state SC \
--plan-type lower \
--data ~/local/temp-data/SC_input_data.v4.jsonl \
< ~/local/geographic-baseline/SC_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/SC_lower_precomputed.json

echo Computing the geographic baseline for SD/upper ...
scripts/once.py \
--state SD \
--plan-type upper \
--data ~/local/temp-data/SD_input_data.v4.jsonl \
< ~/local/geographic-baseline/SD_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/SD_upper_precomputed.json

echo Computing the geographic baseline for SD/lower ...
scripts/once.py \
--state SD \
--plan-type lower \
--data ~/local/temp-data/SD_input_data.v4.jsonl \
< ~/local/geographic-baseline/SD_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/SD_lower_precomputed.json

echo Computing the geographic baseline for TN/congress ...
scripts/once.py \
--state TN \
--plan-type congress \
--data ~/local/temp-data/TN_input_data.v4.jsonl \
< ~/local/geographic-baseline/TN_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/TN_congress_precomputed.json

echo Computing the geographic baseline for TN/upper ...
scripts/once.py \
--state TN \
--plan-type upper \
--data ~/local/temp-data/TN_input_data.v4.jsonl \
< ~/local/geographic-baseline/TN_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/TN_upper_precomputed.json

echo Computing the geographic baseline for TN/lower ...
scripts/once.py \
--state TN \
--plan-type lower \
--data ~/local/temp-data/TN_input_data.v4.jsonl \
< ~/local/geographic-baseline/TN_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/TN_lower_precomputed.json

echo Computing the geographic baseline for TX/congress ...
scripts/once.py \
--state TX \
--plan-type congress \
--data ~/local/temp-data/TX_input_data.v4.jsonl \
< ~/local/geographic-baseline/TX_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/TX_congress_precomputed.json

echo Computing the geographic baseline for TX/upper ...
scripts/once.py \
--state TX \
--plan-type upper \
--data ~/local/temp-data/TX_input_data.v4.jsonl \
< ~/local/geographic-baseline/TX_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/TX_upper_precomputed.json

echo Computing the geographic baseline for TX/lower ...
scripts/once.py \
--state TX \
--plan-type lower \
--data ~/local/temp-data/TX_input_data.v4.jsonl \
< ~/local/geographic-baseline/TX_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/TX_lower_precomputed.json

echo Computing the geographic baseline for UT/congress ...
scripts/once.py \
--state UT \
--plan-type congress \
--data ~/local/temp-data/UT_input_data.v4.jsonl \
< ~/local/geographic-baseline/UT_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/UT_congress_precomputed.json

echo Computing the geographic baseline for UT/upper ...
scripts/once.py \
--state UT \
--plan-type upper \
--data ~/local/temp-data/UT_input_data.v4.jsonl \
< ~/local/geographic-baseline/UT_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/UT_upper_precomputed.json

echo Computing the geographic baseline for UT/lower ...
scripts/once.py \
--state UT \
--plan-type lower \
--data ~/local/temp-data/UT_input_data.v4.jsonl \
< ~/local/geographic-baseline/UT_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/UT_lower_precomputed.json

echo Computing the geographic baseline for VT/upper ...
scripts/once.py \
--state VT \
--plan-type upper \
--data ~/local/temp-data/VT_input_data.v4.jsonl \
< ~/local/geographic-baseline/VT_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/VT_upper_precomputed.json

echo Computing the geographic baseline for VT/lower ...
scripts/once.py \
--state VT \
--plan-type lower \
--data ~/local/temp-data/VT_input_data.v4.jsonl \
< ~/local/geographic-baseline/VT_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/VT_lower_precomputed.json

echo Computing the geographic baseline for VA/congress ...
scripts/once.py \
--state VA \
--plan-type congress \
--data ~/local/temp-data/VA_input_data.v4.jsonl \
< ~/local/geographic-baseline/VA_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/VA_congress_precomputed.json

echo Computing the geographic baseline for VA/upper ...
scripts/once.py \
--state VA \
--plan-type upper \
--data ~/local/temp-data/VA_input_data.v4.jsonl \
< ~/local/geographic-baseline/VA_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/VA_upper_precomputed.json

echo Computing the geographic baseline for VA/lower ...
scripts/once.py \
--state VA \
--plan-type lower \
--data ~/local/temp-data/VA_input_data.v4.jsonl \
< ~/local/geographic-baseline/VA_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/VA_lower_precomputed.json

echo Computing the geographic baseline for WA/congress ...
scripts/once.py \
--state WA \
--plan-type congress \
--data ~/local/temp-data/WA_input_data.v4.jsonl \
< ~/local/geographic-baseline/WA_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/WA_congress_precomputed.json

echo Computing the geographic baseline for WA/upper ...
scripts/once.py \
--state WA \
--plan-type upper \
--data ~/local/temp-data/WA_input_data.v4.jsonl \
< ~/local/geographic-baseline/WA_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/WA_upper_precomputed.json

echo Computing the geographic baseline for WV/congress ...
scripts/once.py \
--state WV \
--plan-type congress \
--data ~/local/temp-data/WV_input_data.v4.jsonl \
< ~/local/geographic-baseline/WV_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/WV_congress_precomputed.json

echo Computing the geographic baseline for WV/upper ...
scripts/once.py \
--state WV \
--plan-type upper \
--data ~/local/temp-data/WV_input_data.v4.jsonl \
< ~/local/geographic-baseline/WV_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/WV_upper_precomputed.json

echo Computing the geographic baseline for WV/lower ...
scripts/once.py \
--state WV \
--plan-type lower \
--data ~/local/temp-data/WV_input_data.v4.jsonl \
< ~/local/geographic-baseline/WV_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/WV_lower_precomputed.json

echo Computing the geographic baseline for WI/congress ...
scripts/once.py \
--state WI \
--plan-type congress \
--data ~/local/temp-data/WI_input_data.v4.jsonl \
< ~/local/geographic-baseline/WI_congress_neighborhoods.jsonl \
> ~/local/geographic-baseline/WI_congress_precomputed.json

echo Computing the geographic baseline for WI/upper ...
scripts/once.py \
--state WI \
--plan-type upper \
--data ~/local/temp-data/WI_input_data.v4.jsonl \
< ~/local/geographic-baseline/WI_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/WI_upper_precomputed.json

echo Computing the geographic baseline for WI/lower ...
scripts/once.py \
--state WI \
--plan-type lower \
--data ~/local/temp-data/WI_input_data.v4.jsonl \
< ~/local/geographic-baseline/WI_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/WI_lower_precomputed.json

echo Computing the geographic baseline for WY/upper ...
scripts/once.py \
--state WY \
--plan-type upper \
--data ~/local/temp-data/WY_input_data.v4.jsonl \
< ~/local/geographic-baseline/WY_upper_neighborhoods.jsonl \
> ~/local/geographic-baseline/WY_upper_precomputed.json

echo Computing the geographic baseline for WY/lower ...
scripts/once.py \
--state WY \
--plan-type lower \
--data ~/local/temp-data/WY_input_data.v4.jsonl \
< ~/local/geographic-baseline/WY_lower_neighborhoods.jsonl \
> ~/local/geographic-baseline/WY_lower_precomputed.json

