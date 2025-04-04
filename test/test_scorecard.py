"""
TEST SAMPLE SCORECARDS
"""

from typing import Any, Dict, List

from collections import OrderedDict
import pandas as pd

from rdapy.score.utils import *
from rdapy.score.aggregate import arcs_are_symmetric
from rdapy.score.analyze import (
    Aggregates,
    aggregate_districts,
    score_plan,
    calc_compactness_metrics,
)

cycle: str = "2020"
testdata_dir: str = "testdata/score"


class TestScorecard:
    def test_scorecard(self) -> None:
        for xx in ["NC", "NJ"]:
            plan_path: str = f"testdata/score/{xx}20C_baseline_100.csv"
            plan: PlanCSV = read_plan(plan_path)
            geoid_index: Dict[str, int] = index_plan(plan)

            data_path: str = f"../vtd_data/2020_VTD/{xx}/{xx}_input_data.v1.jsonl"

            ### BOILERPLATE - DON'T CHANGE THIS ###

            input_metadata: Dict[str, Any]
            precinct_data: List[Dict[str, Any]]
            adjacency_graph: Dict[str, List[str]]
            input_metadata, precinct_data, adjacency_graph = unpack_input_data(
                data_path
            )
            geoids: List[str] = geoids_from_precinct_data(precinct_data)
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
            )

            #

            expected_path: str = f"{testdata_dir}/{xx}_DRA_scorecard.json"
            expected: Dict[str, Any] = read_json(expected_path)

            decimals_path: str = f"{testdata_dir}/expected_decimal_places.json"
            # 2025-03-21: Skipping these removed redundant or legacy metrics
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
                # 2025-03-21: Removed "minority",
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
        test_plans: str = "testdata/ensemble/NC_congress_plans.100.jsonl"
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

        data_path: str = f"../vtd_data/2020_VTD/{xx}/{xx}_input_data.v1.jsonl"

        input_metadata: Dict[str, Any]
        precinct_data: List[Dict[str, Any]]
        adjacency_graph: Dict[str, List[str]]
        input_metadata, precinct_data, adjacency_graph = unpack_input_data(data_path)
        geoids: List[str] = geoids_from_precinct_data(precinct_data)
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
        )

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
        # 2025-03-21: Skipping these removed redundant or legacy metrics
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
            # 2025-03-21: Removed "minority",
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


### END ###
