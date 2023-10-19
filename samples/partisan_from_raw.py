#!/usr/bin/env python3

"""
Sample partisan analytics starting from raw data
"""

from rdapy import *
from testutils import *

### FILES ###

data_dir: str = "~/local/sample-data"

# Exported from DRA
plan_file: str = "NC_2022_Congress_Official.csv"

# This is a proprietary DRA file, derived elections data from partners.
election_file: str = "2020vt_2016Composite_block_37_data2.json"

### HELPERS ###


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


## 1 - READ A BLOCK-ASSIGNMENT FILE ###

plan_path: str = os.path.expanduser(f"{data_dir}/{plan_file}")
plan = read_csv(plan_path, [str, int])

### 2 - READ AN ELECTION CSV ###

election_path: str = os.path.expanduser(f"{data_dir}/{election_file}")

# The starting point for partisan analytics is simply the total votes and
# the D(emocratic) and R(epublican) votes by block.
election: dict[str, dict[str, int]] = read_election(election_path)

### 3 - AGGREGATE TWO-PARTY D VOTE BY DISTRICT & STATEWIDE ###

d_by_district: defaultdict[int | str, int] = defaultdict(int)
tot_by_district: defaultdict[int | str, int] = defaultdict(int)
d_statewide: int = 0
tot_statewide: int = 0

for row in plan:
    geoid: str = row["GEOID20"]
    district: int = row["District"]

    d: int = election[geoid]["D"]
    r: int = election[geoid]["R"]
    tot: int = d + r
    # tot: int = election[geoid]["Tot"]  # NOTE - Includes "other"

    d_by_district[district] += d
    d_statewide += d

    tot_by_district[district] += tot
    tot_statewide += tot

Vf: float = d_statewide / tot_statewide
Vf_array: list[float] = [
    d / tot for d, tot in zip(d_by_district.values(), tot_by_district.values())
]

### 4 - CALCULATE PARTISAN ANALYTICS ###

results: dict = calc_partisan_metrics(Vf, Vf_array)

### 5 - PRINT THE RESULTS ###

print(f"Partisan analytics:")
print(results)

pass

### END ###
