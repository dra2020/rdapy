#!/usr/bin/env python3

"""
All-up sample starting from raw data
"""

from rdapy import *
from testutils import *

# Parameters

xx: str = "NC"
data_path: str = "~/local/sample-data"

do_census: bool = False
do_elections: bool = False
do_shapes: bool = False
do_contiguity: bool = False

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


def read_elections(rel_path: str) -> dict[str, dict[str, int]]:
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


### PLAN / MAP ###

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

# Census data

if do_census:
    # NOTE - This is a proprietary DRA file, derived from the Census PL file
    census_path: str = os.path.expanduser(
        f"{data_path}/2020vt_Census_block_37_data2.json"
    )
    # But the starting point for analyzing population deviations is simply
    # the total census population by geoid.
    population: dict[str, int] = read_census(census_path)

    # TODO: More

    pass

# Elections

if do_elections:
    # NOTE - This is a proprietary DRA file, derived elections data from partners
    elections_path: str = os.path.expanduser(
        f"{data_path}/2020vt_2016Composite_block_37_data2.json"
    )
    # But the starting point for partisan analytics is simply
    # the total votes and D(emocratic) and R(epublican) votes by geoid.
    elections: dict[str, dict[str, int]] = read_elections(elections_path)

    # TODO: More

    pass

# Shapes

if do_shapes:
    # This are the Census TIGER/Line block shape for the state
    shapes_path: str = os.path.expanduser(f"{data_path}/tl_2020_37_tabblock20")
    shapes, _ = load_shapes(shapes_path, id="GEOID20")

    # TODO: More

    pass

# Contiguity

if do_contiguity:
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
        not_embedded: bool = not is_embedded(
            id, assignments_by_block, inverted_plan, graph
        )
        not_embedded_by_district[id] = not_embedded

    print(f"Contiguous:")
    for id, connected in sorted(contiguity_by_district.items()):
        print(f"- District {id}: {connected}")

    print()

    print(f"Not embedded:")
    for id, not_embedded in sorted(not_embedded_by_district.items()):
        print(f"- District {id}: {not_embedded}")

    pass

pass

### END ###
