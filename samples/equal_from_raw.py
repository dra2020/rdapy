#!/usr/bin/env python3

"""
Sample population deviation starting from raw data
"""

from rdapy import *
from testutils import *

### FILES ###

data_dir: str = "~/local/sample-data"

# Exported from DRA
plan_file: str = "NC_2022_Congress_Official.csv"

# This is a proprietary DRA file, derived from the Census PL file.
census_file: str = "2020vt_Census_block_37_data2.json"

### HELPERS ###


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


## 1 - READ A BLOCK-ASSIGNMENT FILE ###

plan_path: str = os.path.expanduser(f"{data_dir}/{plan_file}")
plan = read_csv(plan_path, [str, int])


### 2 - READ CENSUS DATA ###

census_path: str = os.path.expanduser(f"{data_dir}/{census_file}")

# The starting point for analyzing population deviations is simply
# the total census population by geoid.
population: dict[str, int] = read_census(census_path)


### 3 - SUM POPULATION BY DISTRICT ###

total_pop: int = 0
pop_by_district: defaultdict[int | str, int] = defaultdict(int)
for row in plan:
    geoid: str = row["GEOID20"]  # Your field names may vary
    district: int = row["District"]  # Your field names may vary
    pop: int = population[geoid]

    pop_by_district[district] += pop
    total_pop += pop

### 4 - CALCULATE POPULATION DEVIATION ###

max_pop: int = max(pop_by_district.values())
min_pop: int = min(pop_by_district.values())
target_pop: int = int(total_pop / len(pop_by_district))

deviation: float = calc_population_deviation(max_pop, min_pop, target_pop)

### 5 - PRINT THE RESULTS ###

print(f"Population deviation:")
print(f"{deviation:.4%}")

### END ###
