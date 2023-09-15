#!/usr/bin/env python3

"""
Sample graph analysis starting from raw data
"""

from rdapy import *
from testutils import *

# Parameters

data_path: str = "~/local/sample-data"

# Helpers

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

assignments_by_block: dict[str, int | str] = {
    row["GEOID20"]: row["District"] for row in plan
}

# Contiguity

# NOTE - This is block-adjacency graph dervied from the shapes above.
# It contains a virtual OUT_OF_STATE border node that surrounds the state.
contiguity_path: str = os.path.expanduser(f"{data_path}/block_contiguity.json")
graph: dict[str, list[str]] = read_json(contiguity_path)

contiguity_by_district: dict[int | str, bool] = {}
for id, geos in inverted_plan.items():
    connected: bool = is_connected(list(geos), graph)
    contiguity_by_district[id] = connected

not_embedded_by_district: dict[int | str, bool] = {}
for id, geos in inverted_plan.items():
    not_embedded: bool = not is_embedded(id, assignments_by_block, inverted_plan, graph)
    not_embedded_by_district[id] = not_embedded

print(f"Contiguous:")
for id, connected in sorted(contiguity_by_district.items()):
    print(f"- District {id}: {connected}")

print()

print(f"Not embedded:")
for id, not_embedded in sorted(not_embedded_by_district.items()):
    print(f"- District {id}: {not_embedded}")

pass

### END ###
