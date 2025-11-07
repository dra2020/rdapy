"""
SCAFFOLDING TO EXPLORE ANALYZING ("SCORING") MULTI-MEMBER DISTRICT (MMD) PLANS
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
    NamedAggregates,
)
from .categories import calc_general_category
from ..minority import DEMOGRAPHICS
from ..partisan import calc_electability_index, calc_gallagher_index

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
                # print(json.dumps(parsed_line), file=output_stream)
                continue

            # Case 2: Has "_tag_" key with value "plan"

            if "_tag_" in parsed_line and parsed_line["_tag_"] == "plan":
                name = parsed_line["name"]
                assignments = {str(k): int(v) for k, v in parsed_line["plan"].items()}
                aggs: Aggregates = parsed_line["aggregates"]

                scores: Dict[str, Any]
                # updated_aggs: Aggregates
                scores, _ = score_mmd_plan(
                    assignments,
                    aggs,
                    data=input_data,
                    graph=adjacency_graph,
                    metadata=metadata,
                    data_map=data_map,
                    n_districts=n_districts,
                    district_magnitude=district_magnitude,
                )

                tagged_scores: Dict[str, Any] = {
                    "_tag_": "scores",
                    "name": name,
                    "scores": scores,
                    # "aggregates": updated_aggs,
                }

                print(json.dumps(tagged_scores), file=output_stream)
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

    precision: int = 4

    census_dataset: DatasetKey = get_dataset(data_map, "census")
    # vap_dataset: DatasetKey = get_dataset(data_map, "vap")
    cvap_dataset: DatasetKey = get_dataset(data_map, "cvap")

    # vap_keys: List[str] = list(get_fields(data_map, "vap", vap_dataset).keys())
    cvap_keys: List[str] = list(get_fields(data_map, "cvap", cvap_dataset).keys())

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
    scorecard["census"][census_dataset]["population_deviation"] = round(
        deviation, precision
    )

    # Electability index

    EI_by_district: List[Dict[str, float]] = calc_electability_indexes(
        aggs["cvap"][cvap_dataset], cvap_keys, n_districts, district_magnitude
    )
    scorecard["cvap"][cvap_dataset]["EI"] = EI_by_district

    dummy_aggs: Aggregates = dict()

    return scorecard, dummy_aggs


def calc_electability_indexes(
    data: NamedAggregates,
    cvap_keys: List[str],
    n_districts: int,
    district_magnitude: int,
) -> List[Dict[str, float]]:
    """
    Calculate electability indexes for a MMD plan.

    The result is a list of dictionaries, one per district, where the keys of the dictionaries are
    the electability indexes for each demographic group.
    """

    precision: int = 4

    by_district: List[Dict[str, float]] = list()
    for i in range(n_districts):
        district_EIs: Dict[str, float] = dict()
        total_cvap: float = data[cvap_keys[0]][0]

        for demo in cvap_keys[2:]:  # Skip total and white CVAP
            simple_demo: str = demo.split("_")[0].lower()
            Vf: float = data[demo][i + 1] / total_cvap
            EI: float = calc_electability_index(Vf, district_magnitude)
            district_EIs[simple_demo] = round(EI, precision)

        by_district.append(district_EIs)

    return by_district


### END ###
