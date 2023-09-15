#!/usr/bin/env python3

"""
Sample compactness analytics starting from raw data
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


# Shapes

# This are the Census TIGER/Line block shape for the state
shapes_path: str = os.path.expanduser(f"{data_path}/tl_2020_37_tabblock20")
shapes, _ = load_shapes(shapes_path, id="GEOID20")

# TODO: More

pass

### END ###
