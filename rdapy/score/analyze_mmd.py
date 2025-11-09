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
    DatasetKey,
    Aggregates,
    Precinct,
    District,
    NamedAggregates,
)

from ..partisan import calc_electability_index, calc_gallagher_index
from ..compactness import (
    calc_cut_score,
    calc_energy,
)
from ..minority import DEMOGRAPHICS
from .categories import (
    calc_general_category,
    calc_partisan_category,
    calc_minority_category,
    calc_compactness_category,
    calc_splitting_category,
)
from .analyze import _rate_compactness, _rate_splitting  # MMD HACK

#####


def score_mmd_plans(
    input_stream: TextIO,
    output_stream: TextIO,
    input_data: List[Dict[str, Any]],
    data_map: Dict[str, Any],
    adjacency_graph: Dict[str, List[str]],
    metadata: Dict[str, Any],
    *,
    districts_override: int,
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
                updated_aggs: Aggregates
                scores, updated_aggs = score_mmd_plan(
                    assignments,
                    aggs,
                    data=input_data,
                    graph=adjacency_graph,
                    metadata=metadata,
                    data_map=data_map,
                    districts_override=districts_override,
                    district_magnitude=district_magnitude,
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

    # This assumes that the data map specifies datasets for each type ...

    census_dataset: DatasetKey = get_dataset(data_map, "census")
    vap_dataset: DatasetKey = get_dataset(data_map, "vap")
    cvap_dataset: DatasetKey = get_dataset(data_map, "cvap")
    election_datasets: List[DatasetKey] = get_datasets(data_map, "election")
    shapes_dataset: DatasetKey = get_dataset(data_map, "shapes")

    scorecard: Dict[str, Any] = {
        "census": {census_dataset: {}},
        "vap": {vap_dataset: {}},
        "cvap": {cvap_dataset: {}},
        "election": {e: {} for e in election_datasets},
        "shapes": {shapes_dataset: {}},
    }

    # ... but limit the scorecard to just the needed dataset types.

    if mode not in ["all", "general", "splitting"]:
        scorecard.pop("census", None)

    if mode not in ["all", "minority"]:
        scorecard.pop("vap", None)
        scorecard.pop("cvap", None)

    if mode not in ["all", "partisan"]:
        scorecard.pop("election", None)

    if mode not in ["all", "compactness"]:
        scorecard.pop("shapes", None)

    if mode in ["all", "general"]:
        general_metrics: Dict[str, Any] = calc_general_category(
            aggs["census"][census_dataset],
            n_districts,
        )
        deviation: float = general_metrics.pop("population_deviation")
        scorecard["census"][census_dataset]["population_deviation"] = deviation

    # if mode in ["all", "partisan"]: ...

    # if mode in ["all", "minority"]: ...

    ##### MMD ADDITIONS #####
    # - Electability index -- by district (fractions) and for the plan (integers)
    # - Statewide CVAP percentages
    # - Gallagher Index

    if mode in ["all"]:  # MMD HACK
        # vap_keys: List[str] = list(get_fields(data_map, "vap", vap_dataset).keys())
        cvap_keys: List[str] = list(get_fields(data_map, "cvap", cvap_dataset).keys())

        district_magnitudes: List[int] = [district_magnitude] * n_districts

        EI_by_district: List[Dict[str, float]] = calc_electability_indexes(
            aggs["cvap"][cvap_dataset],
            cvap_keys,
            n_districts,
            district_magnitudes,
        )
        demos: List[str] = list(EI_by_district[0].keys())
        EI_summaries: Dict[str, int] = defaultdict(int)
        for district in EI_by_district:
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

    ##### END MMD ADDITIONS #####

    if mode in ["all", "compactness"]:
        compactness_by_district: Dict[str, List[float]] = calc_compactness_category(
            aggs["shapes"][shapes_dataset], n_districts
        )
        compactness_metrics: Dict[str, float] = {
            "reock": compactness_by_district["reock"][0],
            "polsby_popper": compactness_by_district["polsby_popper"][0],
        }

        # Additional discrete compactness metrics
        cut_score: int = calc_cut_score(assignments, graph)
        compactness_metrics["cut_score"] = cut_score

        # Population compactness
        census_dataset: DatasetKey = get_dataset(data_map, "census")
        pop_field: str = get_fields(data_map, "census", census_dataset)["total_pop"]
        energy: float = calc_energy(assignments, data, pop_field)  # type: ignore
        compactness_metrics["population_compactness"] = energy

        scorecard["shapes"][shapes_dataset].update(compactness_metrics)

        scorecard["shapes"][shapes_dataset]["compactness"] = _rate_compactness(
            scorecard["shapes"][shapes_dataset]["reock"],
            scorecard["shapes"][shapes_dataset]["polsby_popper"],
        )

    if mode in ["all", "splitting"]:
        splitting_metrics: Dict[str, float]
        splitting_by_district: Dict[str, List[float]]
        splitting_metrics, splitting_by_district = calc_splitting_category(
            aggs["census"][census_dataset], n_districts
        )
        scorecard["census"][census_dataset].update(splitting_metrics)
        scorecard["census"][census_dataset]["splitting"] = _rate_splitting(
            scorecard["census"][census_dataset]["county_splitting"],
            scorecard["census"][census_dataset]["district_splitting"],
            n_counties,
            n_districts,
        )

    # Combine the by-district metrics
    new_aggs: Aggregates = aggs.copy()
    if mode in ["all"]:  # MMD HACK
        EI_aggs: List[Dict[str, List[float]]] = EI_to_aggregates(EI_by_district)
        for agg in EI_aggs:
            new_aggs["cvap"][cvap_dataset].update(agg)
    if mode in ["all", "compactness"]:
        new_aggs["shapes"][shapes_dataset].update(compactness_by_district)
    if mode in ["all", "splitting"]:
        new_aggs["census"][census_dataset].update(splitting_by_district)
        new_aggs["census"][census_dataset].pop("CxD")

    # Trim the floating point numbers
    precision: int = 4
    int_metrics: List[str] = [
        "pr_seats",
        "fptp_seats",
        "proportionality",
        "competitive_district_count",
        "competitiveness",
        "proportional_opportunities",
        "proportional_coalitions",
        "mmd_black",
        "mmd_hispanic",
        "mmd_coalition",
        "minority",
        "cut_score",
        "spanning_tree_score",
        "compactness",
        "counties_split",
        "county_splits",
        "splitting",
    ]
    for type_, datasets_ in scorecard.items():
        for dataset_, metrics in datasets_.items():
            for metric_, value_ in metrics.items():
                if value_ is None:  # Was: or metric == "by_district":
                    continue
                if metric_ not in int_metrics:
                    scorecard[type_][dataset_][metric_] = round(value_, precision)

    return scorecard, new_aggs


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
