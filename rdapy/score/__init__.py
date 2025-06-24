# rdapy/score/__init__.py

from .analyze import score_plans, score_plan
from .categories import (
    calc_population_deviation,
    calc_general_category,
    calc_partisan_category,
    calc_minority_metrics,  # TODO
    calc_compactness_metrics,
    calc_splitting_metrics,
)

name: str = "score"
