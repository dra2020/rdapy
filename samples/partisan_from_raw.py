#!/usr/bin/env python3

"""
Sample partisan analytics starting from raw data
"""

from rdapy import *
from testutils import *

# Parameters

data_path: str = "~/local/sample-data"

# Helpers


def read_election(rel_path: str) -> dict[str, dict[str, int]]:
    """Read the DRA composite elections JSON for a state."""

    abs_path: str = FileSpec(rel_path).abs_path
    with open(abs_path, "r", encoding="utf-8-sig") as f:
        data: Any = json.load(f)

    dataset_key: str = "C16GCO"
    by_geoid: defaultdict[str, dict[str, int]] = defaultdict(dict)
    for feature in data["features"]:
        geoid: str = feature["properties"]["GEOID"]
        tot: int = feature["properties"]["datasets"][dataset_key]["Tot"]
        d: int = feature["properties"]["datasets"][dataset_key]["D"]
        r: int = feature["properties"]["datasets"][dataset_key]["R"]

        by_geoid[geoid] = {"Tot": tot, "D": d, "R": r}

    return by_geoid


# Block assignments

# This is a standard block-assignment file
plan_path: str = os.path.expanduser(f"{data_path}/NC_2022_Congress_Official.csv")
plan = read_csv(plan_path, [str, int])

# Invert it & index it by geoid, for later use
inverted_plan: defaultdict[int | str, set[str]] = defaultdict(set)
for row in plan:
    geoid: str = row["GEOID20"]
    district: int = row["District"]
    inverted_plan[district].add(geoid)

# TODO
# assignments_by_block: dict[str, int | str] = {
#     row["GEOID20"]: row["District"] for row in plan
# }

# Election

# NOTE - This is a proprietary DRA file, derived elections data from partners
election_path: str = os.path.expanduser(
    f"{data_path}/2020vt_2016Composite_block_37_data2.json"
)
# But the starting point for partisan analytics is simply
# the total votes and D(emocratic) and R(epublican) votes by geoid.
election: dict[str, dict[str, int]] = read_election(election_path)

# TODO: More

pass

### END ###
