#!/usr/bin/env python3

"""
Sample starting from raw data
"""

from rdapy import *
from testutils import *

# Parameters

xx: str = "NC"
data_path: str = "~/local/sample-data"

do_assignments: bool = True
do_census: bool = False
do_elections: bool = True
do_shapes: bool = False
do_contiguity: bool = True

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


# Assignments

if do_assignments:
    plan_path: str = os.path.expanduser(f"{data_path}/NC_2022_Congress_Official.csv")
    assignments = read_csv(plan_path, [str, int])

    inverted_plan: defaultdict[int, set[str]] = defaultdict(set)
    for row in assignments:
        geoid: str = row["GEOID20"]
        district: int = row["District"]
        inverted_plan[district].add(geoid)

    # TODO: More

    pass

# Census data

if do_census:
    census_path: str = os.path.expanduser(
        f"{data_path}/2020vt_Census_block_37_data2.json"
    )
    population: dict[str, int] = read_census(census_path)

    # TODO: More

    pass

# Elections

if do_elections:
    # TODO: get this data

    pass

# Shapes

if do_shapes:
    shapes_path: str = os.path.expanduser(f"{data_path}/tl_2020_37_tabblock20")
    shapes, _ = load_shapes(shapes_path, id="GEOID20")
    # shapes = [item[1] for item in shapes]  # discard the id

    # TODO: More

    pass

# Contiguity

if do_contiguity:
    contiguity_path: str = os.path.expanduser(f"{data_path}/block_contiguity.json")
    graph: dict[str, list[str]] = read_json(contiguity_path)

    # TODO: more

    pass

pass

### END ###
