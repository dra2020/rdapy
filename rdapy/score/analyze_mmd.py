"""
SCAFFOLDING TO ANALYZE ("SCORE") A MULTI-MEMBER DISTRICT (MMD) PLAN
"""

from typing import Any, List, Dict, Tuple, Optional, TextIO

import sys, json

from ..base import (
    get_dataset,
    get_datasets,
    get_fields,
    DatasetKey,
    Aggregates,
    Precinct,
    District,
)
from .categories import calc_general_category

#####


def score_mmd_plans(
    input_stream: TextIO,
    output_stream: TextIO,
    input_data: List[Dict[str, Any]],
    data_map: Dict[str, Any],
    adjacency_graph: Dict[str, List[str]],
    metadata: Dict[str, Any],
    *,
    n_districts: int,
    district_magnitude: int,
) -> None:
    """
    Read plans & district aggregates as JSONL from the input stream.
    Score each plan.
    Write the scores along with the aggregates to the output stream.
    Pass through metadata records.
    Skip any other records.
    """

    i: int = 0
    for line in input_stream:
        try:
            parsed_line: Dict[str, Any] = json.loads(line)

            # Case 1: Has "_tag_" key with value "metadata" - pass it along

            if "_tag_" in parsed_line and parsed_line["_tag_"] == "metadata":
                print(json.dumps(parsed_line), file=output_stream)
                continue

            # Case 2: Has "_tag_" key with value "plan"

            if "_tag_" in parsed_line and parsed_line["_tag_"] == "plan":
                name = parsed_line["name"]
                assignments = {str(k): int(v) for k, v in parsed_line["plan"].items()}
                aggs: Aggregates = parsed_line["aggregates"]

                scores: Dict[str, Any]
                updated_aggs: Aggregates
                scores, updated_aggs = score_mmd_plan(
                    assignments,
                    aggs,
                    data=input_data,
                    graph=adjacency_graph,
                    metadata=metadata,
                    data_map=data_map,
                    n_districts=n_districts,
                    district_magnitude=district_magnitude,
                )

                scores_with_aggs: Dict[str, Any] = {
                    "_tag_": "scores",
                    "name": name,
                    "scores": scores,
                    "aggregates": updated_aggs,
                }

                print(json.dumps(scores_with_aggs), file=output_stream)
                continue

            # Case 3: Something else - skip the line, e.g., adjacency graph, etc.

            continue

        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON: {e}", file=sys.stderr)
        except Exception as e:
            print(f"Error processing record: {e}", file=sys.stderr)


### SCORE ONE MMDPLAN ###


def score_mmd_plan(
    assignments: Dict[Precinct, District],
    aggs: Aggregates,
    *,
    data: List[Dict[str, Any]],
    graph: Dict[str, List[str]],
    metadata: Dict[str, Any],
    data_map: Dict[str, Any],
    #
    n_districts: int,
    district_magnitude: int,
) -> Tuple[Dict[str, Any], Aggregates]:
    """
    This is a quick & dirty routine for scoring a MMD plan, using homogenous-sized MMDs.
    """

    census_dataset: DatasetKey = get_dataset(data_map, "census")
    # vap_dataset: DatasetKey = get_dataset(data_map, "vap")
    cvap_dataset: DatasetKey = get_dataset(data_map, "cvap")

    scorecard: Dict[str, Any] = {
        "census": {census_dataset: {}},
        # "vap": {vap_dataset: {}},
        "cvap": {cvap_dataset: {}},
    }

    # Population deviation

    general_metrics: Dict[str, Any] = calc_general_category(
        aggs["census"][census_dataset],
        n_districts,
    )
    deviation: float = general_metrics.pop("population_deviation")
    scorecard["census"][census_dataset]["population_deviation"] = deviation

    # TODO - Electability index

    # Trim the floating point numbers
    precision: int = 4
    int_metrics: List[str] = []

    for type_, datasets_ in scorecard.items():
        for dataset_, metrics in datasets_.items():
            for metric_, value_ in metrics.items():
                if value_ is None:
                    continue
                if metric_ not in int_metrics:
                    scorecard[type_][dataset_][metric_] = round(value_, precision)

    new_aggs: Aggregates = aggs.copy()

    return scorecard, new_aggs


### END ###
