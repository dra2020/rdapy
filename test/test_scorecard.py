"""
TEST SAMPLE SCORECARDS
"""

from typing import Any, Dict, List, Generator, List, Tuple, TextIO

from collections import OrderedDict
import pandas as pd

from rdapy import (
    aggregate_districts,
    approx_equal,
    read_csv,
    read_json,
    smart_read,
    score_plan,
    Precinct,
    District,
    GeoIDIndex,
    DatasetKey,
    PlanCSV,
    sorted_geoids,
    collect_metadata,
    read_record,
    Aggregates,
    OUT_OF_STATE,
)

# TODO - Simplify these imports, when functions have moved.
from rdapy.score.aggregate import arcs_are_symmetric
from rdapy.score.analyze import calc_compactness_metrics


cycle: str = "2020"
testdata_dir: str = "testdata/score"


def flatten_scorecard(dataset_keyed_scorecard):
    """For legacy tests, flatten the scorecard dictionary by removing the dataset keys."""

    flattened: Dict[str, Any] = dict()

    for T in ["census", "vap", "cvap", "election", "shapes"]:
        dataset: DatasetKey = list(dataset_keyed_scorecard[T].keys())[0]
        flattened.update(dataset_keyed_scorecard[T][dataset])

    return flattened


class TestScorecard:
    def test_scorecard(self) -> None:
        for xx in ["NC", "NJ"]:
            plan_path: str = f"testdata/score/{xx}20C_baseline_100.csv"
            plan: PlanCSV = read_plan(plan_path)
            geoid_index: Dict[str, int] = index_plan(plan)

            data_path: str = f"testdata/score/{xx}_input_data.v1.jsonl"

            ### BOILERPLATE - DON'T CHANGE THIS ###

            input_metadata: Dict[str, Any]
            precinct_data: List[Dict[str, Any]]
            adjacency_graph: Dict[str, List[str]]
            input_metadata, precinct_data, adjacency_graph = unpack_input_data(
                data_path
            )
            geoids: List[str] = sorted_geoids(precinct_data)
            metadata: Dict[str, Any] = collect_metadata(xx, "congress", geoids)

            data_by_geoid: Dict[str, Any] = {
                precinct["geoid"]: precinct for precinct in precinct_data
            }
            assert arcs_are_symmetric(data_by_geoid)

            aggs: Aggregates = aggregate_districts(
                geoid_index,
                precinct_data,
                adjacency_graph,
                metadata,
                data_metadata=input_metadata,
                which="all",
            )

            scorecard: Dict[str, Any]
            updated_aggs: Aggregates
            scorecard, updated_aggs = score_plan(
                geoid_index,
                aggs,
                data=precinct_data,
                graph=adjacency_graph,
                metadata=metadata,
                data_map=input_metadata,
                mode="all",
                mmd_scoring=False,
                precomputed={},
            )

            scorecard = flatten_scorecard(scorecard)

            #

            expected_path: str = f"{testdata_dir}/{xx}_DRA_scorecard.json"
            expected: Dict[str, Any] = read_json(expected_path)

            decimals_path: str = f"{testdata_dir}/expected_decimal_places.json"
            # Skipping these removed redundant or legacy metrics
            skip: List[str] = [
                "gamma",
                "global_symmetry",
                "competitive_district_pct",
                "avg_dem_win_pct",
                "avg_rep_win_pct",
            ]
            approx_floats: Dict[str, int] = read_json(decimals_path)
            exact_ints: List[str] = [
                # "pr_seats",
                "proportional_opportunities",
                "proportional_coalitions",
            ]
            approx_ints: List[str] = [
                # "kiwysi", # Disabled due to large runtime cost
                "proportionality",
                "competitiveness",
                # "minority", # Removed 2025-03-25, because the rating is now continuous.
                "compactness",
                "splitting",
            ]

            for metric in exact_ints:
                assert scorecard[metric] == expected[metric]

            for metric in approx_ints:
                assert abs(scorecard[metric] - expected[metric]) <= 1

            for metric in approx_floats:
                if metric in skip:
                    continue
                assert approx_equal(
                    scorecard[metric], expected[metric], places=approx_floats[metric]
                )

    def test_compactness(self) -> None:
        for xx in ["NC", "NJ"]:
            profile_path = f"{testdata_dir}/{xx}_root_profile.json"
            profile: Dict[str, Any] = read_json(profile_path)
            n_districts: int = int(profile["nDistricts"])
            implicit_district_props: List[Dict[str, float]] = profile["shapes"]

            # Convert old profile format to new aggregates format
            # Initialize the aggregates with a dummy statewide value
            aggregates: Dict[str, Any] = {
                "area": [0.0],
                "perimeter": [0.0],
                "diameter": [0.0],
            }
            [aggregates["area"].append(d["area"]) for d in implicit_district_props]
            [
                aggregates["perimeter"].append(d["perimeter"])
                for d in implicit_district_props
            ]
            [
                aggregates["diameter"].append(d["diameter"])
                for d in implicit_district_props
            ]

            scorecard_path: str = f"{testdata_dir}/{xx}_DRA_scorecard.json"
            expected: Dict[str, Any] = read_json(scorecard_path)

            #

            actual: Dict[str, List[float]] = calc_compactness_metrics(
                aggregates, n_districts
            )

            # decimals_path: str = f"{testdata_dir}/expected_decimal_places.json"
            # approx_floats: Dict[str, int] = read_json(decimals_path)

            for metric in ["reock", "polsby_popper"]:
                assert approx_equal(actual[metric][0], expected[metric], places=4)

    def test_scoring_updates(self) -> None:
        xx: str = "NC"

        # Get one plan from the test ensemble
        test_plans: str = "testdata/plans/NC_congress_plans.tagged.jsonl"
        with smart_read(test_plans) as ensemble_stream:
            for i, line in enumerate(ensemble_stream):
                # Skip the metadata and ReCom graph records
                in_record: Dict[str, Any] = read_record(line)
                if "_tag_" not in in_record:
                    continue
                if in_record["_tag_"] == "metadata":
                    continue

                # Score each plan record
                assert in_record["_tag_"] == "plan"

                plan: Dict[Precinct, District] = in_record["plan"]
                break

        data_path: str = f"testdata/score/{xx}_input_data.v1.jsonl"

        input_metadata: Dict[str, Any]
        precinct_data: List[Dict[str, Any]]
        adjacency_graph: Dict[str, List[str]]
        input_metadata, precinct_data, adjacency_graph = unpack_input_data(data_path)
        geoids: List[str] = sorted_geoids(precinct_data)
        metadata: Dict[str, Any] = collect_metadata(xx, "congress", geoids)

        data_by_geoid: Dict[str, Any] = {
            precinct["geoid"]: precinct for precinct in precinct_data
        }
        assert arcs_are_symmetric(data_by_geoid)

        # assert arcs_are_symmetric(shapes)

        aggs: Aggregates = aggregate_districts(
            plan,
            precinct_data,
            adjacency_graph,
            metadata,
            data_metadata=input_metadata,
            which="all",
        )

        scorecard: Dict[str, Any]
        updated_aggs: Aggregates
        scorecard, updated_aggs = score_plan(
            plan,
            aggs,
            data=precinct_data,
            graph=adjacency_graph,
            metadata=metadata,
            data_map=input_metadata,
            mode="all",
            mmd_scoring=False,
            precomputed={},
        )

        scorecard = flatten_scorecard(scorecard)

        # The actual scores

        actuals: OrderedDict[str, Any] = OrderedDict()
        actuals.update(scorecard)

        # The expected scores

        test_scores: str = "testdata/score/baseline/NC20C_scores_all.csv"
        df = pd.read_csv(test_scores)
        expected: Dict[str, Any] = df.iloc[0].to_dict()

        # Compare the actual and expected scores

        decimals_path: str = f"{testdata_dir}/expected_decimal_places.json"
        approx_floats: Dict[str, int] = read_json(decimals_path)
        # Skipping these removed redundant or legacy metrics
        skip: List[str] = [
            "gamma",
            "global_symmetry",
            "competitive_district_pct",
            "avg_dem_win_pct",
            "avg_rep_win_pct",
        ]
        exact_ints: List[str] = [
            # "pr_seats",
            "proportional_opportunities",
            "proportional_coalitions",
        ]
        approx_ints: List[str] = [
            # "kiwysi", # Disabled due to large runtime cost
            "proportionality",
            "competitiveness",
            # "minority", # Removed 2025-03-25, because the rating is now continuous
            "compactness",
            "splitting",
        ]

        for metric in exact_ints:
            assert scorecard[metric] == expected[metric]

        for metric in approx_ints:
            assert abs(scorecard[metric] - expected[metric]) <= 1

        for metric in approx_floats:
            if metric in skip:
                continue
            assert approx_equal(
                scorecard[metric], expected[metric], places=approx_floats[metric]
            )


### LEGACY HELPERS FOR TEST CASES ###


def unpack_input_data(
    input_data_path: str,
) -> Tuple[Dict[str, Any], List[Dict[str, Any]], Dict[str, List[str]]]:
    """Read an input data file and return the metadata, the precinct data, and the adjacency graph."""

    input_metadata: Dict[str, Any] = dict()
    input_data: List[Dict[str, Any]] = list()
    adjacency_graph: Dict[str, List[str]] = dict()

    with smart_read(input_data_path) as data_stream:
        for tag, data in input_data_precincts(data_stream):
            if tag == "metadata":
                input_metadata = data
            else:
                if data["geoid"] != OUT_OF_STATE:
                    input_data.append(data)
                adjacency_graph[data["geoid"]] = data["neighbors"]

    return input_metadata, input_data, adjacency_graph


def input_data_precincts(
    data_stream: TextIO,
) -> Generator[Tuple[str, Dict[str, Any]], None, None]:
    """Return precinct data one record at a time (including a metadata record) from an input data JSONL file."""

    for i, line in enumerate(data_stream):
        try:
            in_record: Dict[str, Any] = read_record(line)
            if "_tag_" not in in_record:
                continue

            assert in_record["_tag_"] == "metadata" or in_record["_tag_"] == "precinct"

            tag: str = in_record["_tag_"]
            data: Dict[str, Any] = dict()
            if tag == "metadata":
                data = in_record["properties"]
            else:
                data = in_record["data"]

            yield (tag, data)

        except Exception as e:
            raise Exception(f"Reading input data {i}: {e}")


def read_plan(plan_path: str) -> PlanCSV:
    """Read a precinct-assignment file."""

    return read_csv(plan_path, [str, int])


def index_plan(plan_csv: PlanCSV) -> GeoIDIndex:
    """Index a plan by geoid."""

    geoid_fields: List[str] = ["GEOID", "GEOID20", "GEOID30"]
    district_fields: List[str] = ["District", "DISTRICT"]

    keys: List[str] = list(plan_csv[0].keys())

    geoid_field: str = list(set(geoid_fields) & set(keys))[0]
    district_field: str = list(set(district_fields) & set(keys))[0]

    return {str(row[geoid_field]): int(row[district_field]) for row in plan_csv}


### END ###
