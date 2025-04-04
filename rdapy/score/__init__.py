# rdapy/score/__init__.py

from .utils import *

# TODO - Rationalize imports
from .aggregate import (
    aggregate_plans,
    aggregate_districts,
    Aggregates,
    Datasets,
    get_dataset,
    DatasetKey,
    get_fields,
)
from .analyze import score_plans, score_plan, default_datasets

name: str = "score"
