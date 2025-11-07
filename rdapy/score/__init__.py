# rdapy/score/__init__.py

from .analyze import score_plans, score_plan
from .analyze_mmd import score_mmd_plans, score_mmd_plan
from .categories import (
    calc_general_category,
    calc_partisan_category,
    calc_minority_category,
    calc_compactness_category,
    calc_splitting_category,
)

name: str = "score"
