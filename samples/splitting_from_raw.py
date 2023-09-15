#!/usr/bin/env python3

"""
Sample county-districting splitting starting from raw data
"""

from rdapy import *
from testutils import *

# Parameters

data_path: str = "~/local/sample-data"

# Helpers


def read_census(rel_path: str) -> defaultdict[str, int]:
    """Read the DRA census block data JSON for a state."""

    abs_path: str = FileSpec(rel_path).abs_path
    with open(abs_path, "r", encoding="utf-8-sig") as f:
        data: Any = json.load(f)

    dataset_key: str = "D20F"
    field: str = "Tot"
    pop_by_geoid: defaultdict[str, int] = defaultdict(int)
    for feature in data["features"]:
        geoid: str = feature["properties"]["GEOID"]
        pop: int = feature["properties"]["datasets"][dataset_key][field]

        pop_by_geoid[geoid] = pop

    return pop_by_geoid


# Block assignments

# This is a standard block-assignment file
plan_path: str = os.path.expanduser(f"{data_path}/NC_2022_Congress_Official.csv")
plan = read_csv(plan_path, [str, int])

# TODO
# # Invert it & index it by geoid, for later use
# inverted_plan: defaultdict[int | str, set[str]] = defaultdict(set)
# for row in plan:
#     geoid: str = row["GEOID20"]
#     district: int = row["District"]
#     inverted_plan[district].add(geoid)

# assignments_by_block: dict[str, int | str] = {
#     row["GEOID20"]: row["District"] for row in plan
# }

# Census data

# NOTE - This is a proprietary DRA file, derived from the Census PL file
census_path: str = os.path.expanduser(f"{data_path}/2020vt_Census_block_37_data2.json")
# But the starting point for analyzing population deviations is simply
# the total census population by geoid.
population: dict[str, int] = read_census(census_path)

# Aggregate population by county & district

# TODO: More

pass


### END ###
