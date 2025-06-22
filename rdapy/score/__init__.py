# rdapy/score/__init__.py

from .aggregate import (
    aggregate_plans,
    aggregate_districts,
    Aggregates,
    DatasetKey,
    get_dataset,
    get_datasets,
    get_fields,
)
from .analyze import score_plans, score_plan

from .geographic import (
    Neighbor,
    nearest_connected_neighbor,
    make_neighborhood,
    unpack_neighborhood,
    eval_partisan_lean,
    calc_geographic_baseline,
)

name: str = "score"
