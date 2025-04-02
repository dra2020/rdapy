"""
SCORE ENSEMBLE WRAPPER
"""

from typing import Any, List, Dict, Tuple, OrderedDict, TextIO

import time, warnings
from collections import OrderedDict

from .utils import ensemble_plans
from .aggregate import Aggregates
from .analyze import analyze_plan


def score_ensemble(
    ensemble_stream: TextIO,
    data: List[Dict[str, Any]],
    graph: Dict[str, List[str]],
    metadata: Dict[str, Any],
    *,
    which: str = "all",
    data_metadata: Dict[str, Any],
    verbose: bool = False,
) -> Tuple[List[OrderedDict[str, Any]], List[Dict[str, Any]]]:
    """Score an ensemble of plans."""

    tic: float = time.perf_counter()
    warnings.warn("Starting scoring plans ...")

    # Read & score each plan

    scores_records: List[OrderedDict[str, Any]] = list()
    by_district_records: List[Dict[str, Any]] = list()

    for name, plan in ensemble_plans(ensemble_stream):

        score_record: OrderedDict[str, Any] = OrderedDict()
        score_record["map"] = name

        scorecard: Dict[str, Any] = analyze_plan(
            plan,
            data,
            graph,
            metadata,
            which=which,
            data_metadata=data_metadata,
        )

        by_district: Aggregates = scorecard.pop("by_district")
        score_record.update(scorecard)
        by_district_records.append({"map": name, "by-district": by_district})

        scores_records.append(score_record)

    toc: float = time.perf_counter()
    warnings.warn(f"Done. Elapsed time = {toc - tic: 0.1f} seconds.")

    return scores_records, by_district_records


### END ###
