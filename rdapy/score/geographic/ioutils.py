"""
I/O UTILITIES
"""

from typing import List, Dict, Tuple, Any

import json, csv
from collections import defaultdict

from rdapy.score import (
    smart_read,
    # smart_write,
    OUT_OF_STATE,
    get_dataset,
    DatasetKey,
    get_fields,
)  # TODO - Include these in the base package


def load_neighborhoods(nh_path: str) -> Dict[str, Dict[str, Any]]:
    """Load neighborhoods from a JSONL file."""

    neighborhoods: Dict[str, Dict[str, Any]] = dict()
    with smart_read(nh_path) as nh_stream:
        for i, line in enumerate(nh_stream):
            parsed_line = json.loads(line)

            geoid: str = parsed_line["geoid"]
            neighborhoods[geoid] = parsed_line.copy()

    return neighborhoods


# TODO - DELETE
# def load_evaluations(evals_path: str) -> List[Dict[str, Any]]:
#     """Load evaluations from a JSONL file."""

#     evaluations: List[Dict[str, Any]] = list()
#     with smart_read(evals_path) as precincts_stream:
#         for i, line in enumerate(precincts_stream):
#             parsed_line = json.loads(line)
#             evaluations.append(parsed_line)

#     return evaluations


def index_data(
    data_map: Dict[str, Any], input_data: List[Dict[str, Any]], *, debug: bool = False
) -> Tuple[Dict[str, Dict[str, Any]], List[str], Dict[str, int]]:
    """Index precinct data by geoid."""

    census_dataset: DatasetKey = get_dataset(data_map, "census")
    total_pop_field: str = get_fields(data_map, "census", census_dataset)["total_pop"]
    election_dataset: DatasetKey = get_dataset(data_map, "election")
    dem_votes_field: str = get_fields(data_map, "election", election_dataset)[
        "dem_votes"
    ]
    rep_votes_field: str = get_fields(data_map, "election", election_dataset)[
        "rep_votes"
    ]

    data: Dict[str, Dict[str, Any]] = dict()
    geoids: List[str] = list()
    aggs: Dict[str, int] = defaultdict(int)

    j: int = 0
    for i, precinct in enumerate(input_data):
        geoid: str = precinct["geoid"]
        if geoid == OUT_OF_STATE:
            if debug:
                print("Skipping OUT_OF_STATE ...")
            continue
        j += 1

        geoids.append(geoid)
        data[geoid] = dict()

        pop: int = precinct[total_pop_field]

        data[geoid]["pop"] = pop
        data[geoid]["center"] = precinct["center"]
        data[geoid]["dem_votes"] = precinct[dem_votes_field]
        data[geoid]["tot_votes"] = precinct[dem_votes_field] + precinct[rep_votes_field]

        aggs["state_pop"] += data[geoid]["pop"]
        aggs["state_dem_votes"] += data[geoid]["dem_votes"]
        aggs["state_tot_votes"] += data[geoid]["tot_votes"]

    geoids.sort()

    assert len(geoids) == j, f"Expected {j} geoids, got {len(geoids)}"

    return data, geoids, aggs


# TODO - DELETE
# def districts_to_plan(
#     districts: Dict[int, Dict[str, Any]],
#     *,
#     geoid_field: str = "GEOID",
#     district_field: str = "DISTRICT",
# ) -> List[Dict[str, Any]]:
#     """Convert a dict of geoids by district to a plan."""

#     plan: List[Dict[str, Any]] = list()
#     for id, district_info in districts.items():
#         for geoid in district_info["geoids"]:
#             plan.append({geoid_field: geoid, district_field: str(id)})

#     return plan

# TODO - DELETE
# def write_plan(plan: List[Dict[str, Any]], plan_path: str) -> None:
#     """Write a plan in List[{"GEOID": str, "DISTRICT": int}] format to a CSV file."""

#     with smart_write(plan_path) as assignment_stream:
#         for i, row in enumerate(plan):
#             if i == 0:
#                 cols: List[str] = list(row.keys())
#                 writer: csv.DictWriter = csv.DictWriter(
#                     assignment_stream, fieldnames=cols
#                 )
#                 writer.writeheader()

#             writer.writerow(row)


### END ###
