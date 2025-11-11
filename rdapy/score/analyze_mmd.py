"""
SCAFFOLDING TO EXPLORE ANALYZING ("SCORING") MULTI-MEMBER DISTRICT (MMD) PLANS
"""

from statistics import mode
from typing import Any, List, Dict, Tuple, Optional, TextIO

import sys, json
from collections import defaultdict

from ..base import (
    get_dataset,
    get_datasets,
    get_fields,
    get_dataset_keys,
    DatasetKey,
    Aggregates,
    Precinct,
    District,
    NamedAggregates,
)

from ..partisan import calc_electability_index, calc_gallagher_index  # MMD HACK
from .analyze import (
    setup_scorecard,
    score_general_mode,
    score_partisan_mode,
    score_minority_mode,
    score_compactness_mode,
    score_splitting_mode,
    update_aggregates,
    trim_scores,
)  # MMD HACK

#####


def score_mmd_plans(
    input_stream: TextIO,
    output_stream: TextIO,
    input_data: List[Dict[str, Any]],
    data_map: Dict[str, Any],
    adjacency_graph: Dict[str, List[str]],
    metadata: Dict[str, Any],
    *,
    districts_override: int,  # MMD HACK
    district_magnitude: int,  # MMD HACK
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
                updated_aggs: Aggregates
                scores, updated_aggs = score_mmd_plan(
                    assignments,
                    aggs,
                    data=input_data,
                    graph=adjacency_graph,
                    metadata=metadata,
                    data_map=data_map,
                    districts_override=districts_override,  # MMD HACK
                    district_magnitude=district_magnitude,  # MMD HACK
                )

                tagged_scores: Dict[str, Any] = {
                    "_tag_": "scores",
                    "name": name,
                    "scores": scores,
                    "aggregates": updated_aggs,
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
    mode: str = "all",  # Or one of "general", "partisan", "minority", "compactness", "splitting"
    precomputed: Dict[str, Any] = dict(),
    #
    mmd_scoring: bool = True,  # If False, don't do MMD scoring for backwards compatibility w/ tests.
    reverse_weight_splitting: bool = False,
    #
    districts_override: Optional[int] = None,  # MMD HACK
    district_magnitude: int,  # MMD HACK
) -> Tuple[Dict[str, Any], Aggregates]:
    """
    This is a quick & dirty HACK for scoring a MMD plan, using homogenous-sized MMDs.
    A cut down clone of score_plan() in analyze.py with MMD-specific metrics added.
    """

    # Pulled 'extended' scoring out separately
    assert mode in [
        "all",
        "general",
        "partisan",
        "minority",
        "compactness",
        "splitting",
    ]

    n_districts: int = (
        metadata["D"] if districts_override is None else districts_override
    )  # MMD HACK
    n_counties: int = metadata["C"]

    # region - Get the dataset keys
    census_dataset: DatasetKey
    vap_dataset: DatasetKey
    cvap_dataset: DatasetKey
    election_datasets: List[DatasetKey]
    shapes_dataset: DatasetKey
    census_dataset, vap_dataset, cvap_dataset, election_datasets, shapes_dataset = (
        get_dataset_keys(data_map)
    )
    # endregion

    # region - Set up the scorecard & new by-district aggregates
    scorecard: Dict[str, Any] = setup_scorecard(
        census_dataset,
        vap_dataset,
        cvap_dataset,
        election_datasets,
        shapes_dataset,
        mode,
    )
    compactness_by_district: Dict[str, List[float]] = dict()
    splitting_by_district: Dict[str, List[float]] = dict()

    EI_by_district: List[Dict[str, float]] = list()  # MMD HACK
    # endregion

    if mode in ["all", "general"]:  # 'general' mode
        score_general_mode(
            aggs,
            census_dataset,
            n_districts,
            scorecard,
        )

    # region - MMD HACK
    # if mode in ["all", "partisan"]:  # 'partisan' mode
    #     for election_dataset in election_datasets:
    #         score_partisan_mode(
    #             aggs,
    #             election_dataset,
    #             n_districts,
    #             precomputed,
    #             scorecard,
    #         )

    # if mode in ["all", "minority"]:  # 'minority' mode
    #     score_minority_mode(
    #         aggs,
    #         vap_dataset,
    #         cvap_dataset,
    #         data_map,
    #         n_districts,
    #         scorecard,
    #         mmd_scoring=mmd_scoring,
    #     )
    # endregion

    score_mmd_mode(
        aggs,
        n_districts,
        district_magnitude,
        cvap_dataset,
        data_map,
        scorecard,
        EI_by_district,
    )  # 'mmd' mode - MMD HACK

    if mode in ["all", "compactness"]:  # 'compactness' mode
        score_compactness_mode(
            aggs,
            shapes_dataset,
            n_districts,
            assignments,
            graph,
            data,
            data_map,
            scorecard,
            compactness_by_district,
        )

    if mode in ["all", "splitting"]:  # 'splitting' mode
        score_splitting_mode(
            aggs,
            census_dataset,
            n_districts,
            n_counties,
            scorecard,
            splitting_by_district,
            reverse_weight_splitting=reverse_weight_splitting,
        )

    # Update the by-district aggregates
    new_aggs: Aggregates = update_aggregates(
        aggs,
        mode,
        shapes_dataset,
        census_dataset,
        compactness_by_district,
        splitting_by_district,
    )
    if mode in ["all"]:  # MMD HACK
        EI_aggs: List[Dict[str, List[float]]] = EI_to_aggregates(EI_by_district)
        for agg in EI_aggs:
            new_aggs["cvap"][cvap_dataset].update(agg)

    # Trim the floating point numbers
    trim_scores(scorecard)

    return scorecard, new_aggs


### HELPERS ###


def score_mmd_mode(
    aggs: Aggregates,
    n_districts: int,
    district_magnitude: int,
    cvap_dataset: DatasetKey,
    data_map: Dict[str, Any],
    scorecard: Dict[str, Any],  # NOTE - updated
    EI_by_district: List[Dict[str, float]],  # NOTE - updated
):
    """
    Calulate MMD-specific scoring metrics.
    - Electability index -- by district (fractions) and for the plan (integers)
    - Statewide CVAP percentages
    - Gallagher Index
    """

    cvap_keys: List[str] = list(get_fields(data_map, "cvap", cvap_dataset).keys())

    district_magnitudes: List[int] = [district_magnitude] * n_districts

    by_district: List[Dict[str, float]] = calc_electability_indexes(
        aggs["cvap"][cvap_dataset],
        cvap_keys,
        n_districts,
        district_magnitudes,
    )
    demos: List[str] = list(by_district[0].keys())
    EI_summaries: Dict[str, int] = defaultdict(int)
    for district in by_district:
        for demo in demos:
            field: str = f"{demo}_EI"
            EI_summaries[field] += int(district[demo])
        minority_EI: float = EI_summaries.pop("minority_EI")
        cumulative_EI: float = sum(EI_summaries.values())
        EI_summaries["cumulative_EI"] = int(cumulative_EI)
        EI_summaries["coalition_EI"] = int(minority_EI)

    Sf_array: List[float] = [s / n_districts for s in EI_summaries.values()][
        :-1
    ]  # Exclude all minorities together
    statewide_cvap: Dict[str, float] = statewide_demo_percentages(
        aggs["cvap"][cvap_dataset], cvap_keys
    )
    Vf_array: List[float] = list(
        statewide_demo_percentages(aggs["cvap"][cvap_dataset], cvap_keys).values()
    )
    GI: float = calc_gallagher_index(Vf_array, Sf_array)

    scorecard["cvap"][cvap_dataset]["GI"] = GI
    scorecard["cvap"][cvap_dataset].update(EI_summaries)
    scorecard["cvap"][cvap_dataset].update(statewide_cvap)

    EI_by_district.extend(by_district)


def calc_electability_indexes(
    data: NamedAggregates,
    cvap_keys: List[str],
    n_districts: int,
    district_magnitudes: List[int],
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

        for demo in cvap_keys[1:]:  # Skip total CVAP; include white CVAP
            simple_demo: str = demo.split("_")[0].lower()
            Vf: float = data[demo][i + 1] / total_cvap
            EI: float = calc_electability_index(Vf, district_magnitudes[i])
            district_EIs[simple_demo] = round(EI, precision)

        by_district.append(district_EIs)

    return by_district


def EI_to_aggregates(data: List[Dict[str, float]]) -> List[Dict[str, List[float]]]:
    """
    Convert the EI results by district to a list of aggregates.
    """

    if not data:
        return []

    # Get all unique keys
    keys = data[0].keys()

    # Create a list of dicts, one for each key
    result = []
    for key in keys:
        result.append({f"{key}_EI": [d[key] for d in data]})

    return result


def statewide_demo_percentages(
    data: NamedAggregates, demo_keys: List[str]
) -> Dict[str, float]:
    """
    Calculate statewide demographic percentages for CVAP or VAP.
    """

    demo_totals: Dict[str, float] = defaultdict(float)
    for k in demo_keys:
        for value in data[k]:
            demo_totals[k] += value

    total: float = demo_totals[demo_keys[0]]
    shares: Dict[str, float] = {k: v / total for k, v in demo_totals.items()}
    shares.pop(demo_keys[0])  # Remove total CVAP/VAP

    return shares


### END ###
