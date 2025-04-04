# rdapy/score/__init__.py

from .utils import *

from .aggregate import (
    aggregate_plans,
    aggregate_districts,
    Aggregates,
    DatasetKey,
    get_dataset,
    get_fields,
)
from .analyze import score_plans, score_plan

name: str = "score"
