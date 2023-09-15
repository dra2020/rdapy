#!/usr/bin/env python3

"""
Sample adjacencies analysis starting from raw data
"""

from rdapy import *
from testutils import *

### FILES ###

data_dir: str = "~/local/sample-data"

# Exported from DRA
plan_file: str = "NC_2022_Congress_Official.csv"

# This is block-adjacency adjacencies dervied from the block shapes.
# It contains a virtual OUT_OF_STATE border node that surrounds the state.
contiguity_file: str = "block_contiguity.json"

## 1 - READ BLOCK-ASSIGNMENT FILE ###

plan_path: str = os.path.expanduser(f"{data_dir}/{plan_file}")
plan = read_csv(plan_path, [str, int])

### 2 - INVERT THE PLAN & INDEX IT BY GEOID ###

inverted_plan: defaultdict[int | str, set[str]] = defaultdict(set)
for row in plan:
    geoid: str = row["GEOID20"]  # Your field names may vary
    district: int = row["District"]  # Your field names may vary
    inverted_plan[district].add(geoid)

assignments_by_block: dict[str, int | str] = {
    row["GEOID20"]: row["District"] for row in plan
}

### 3 - CHECK CONTIGUITY & EMBEDDEDNESS ###

contiguity_path: str = os.path.expanduser(f"{data_dir}/{contiguity_file}")
adjacencies: dict[str, list[str]] = read_json(contiguity_path)

contiguity_by_district: dict[int | str, bool] = {}
for id, geos in inverted_plan.items():
    connected: bool = is_connected(list(geos), adjacencies)

    contiguity_by_district[id] = connected

not_embedded_by_district: dict[int | str, bool] = {}
for id, geos in inverted_plan.items():
    not_embedded: bool = not is_embedded(
        id, assignments_by_block, inverted_plan, adjacencies
    )
    not_embedded_by_district[id] = not_embedded

### 4 - PRINT THE RESULTS ###

print(f"Contiguous:")
for id, connected in sorted(contiguity_by_district.items()):
    print(f"- District {id}: {connected}")

print()

print(f"Not embedded:")
for id, not_embedded in sorted(not_embedded_by_district.items()):
    print(f"- District {id}: {not_embedded}")

### END ###
