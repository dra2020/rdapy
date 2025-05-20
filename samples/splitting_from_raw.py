#!/usr/bin/env python3

"""
Sample county-districting splitting starting from raw data

TODO - Rework this to use a `testdata` GeoJSON.
"""

from collections import defaultdict

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


class GeoID:
    """Parse 15-character GeoIDs into their component parts."""

    def __init__(self, id: str) -> None:
        self.state: str = id[0:2]
        self.county: str = id[0:5]  # id[2:5]
        self.tract: str = id[0:11]  # id[5:11]
        self.bg: str = id[0:12]  # id[11:12]
        self.block: str = id  # id[12:15]


## 1 - READ A BLOCK-ASSIGNMENT FILE ###

plan_path: str = os.path.expanduser(f"{data_dir}/{plan_file}")
plan = read_csv(plan_path, [str, int])

### 2 - READ CENSUS DATA ###

census_path: str = os.path.expanduser(f"{data_dir}/{census_file}")

# The starting point for analyzing county-district splitting is simply
# the total census population by geoid.
population: dict[str, int] = read_census(census_path)

### 3 - AGGREGATE POPULATION BY COUNTY & DISTRICT ###

counties: set[str] = set()
districts: set[int | str] = set()

for row in plan:
    geoid: str = row["GEOID20"]  # Your field names may vary
    district: int = row["District"]  # Your field names may vary

    county: str = GeoID(geoid).county[2:]

    counties.add(county)
    districts.add(district)

county_to_index: dict[str, int] = {county: i for i, county in enumerate(counties)}
district_to_index: dict[int | str, int] = {
    district: i for i, district in enumerate(districts)
}

CxD: list[list[float]] = [[0.0] * len(counties) for _ in range(len(districts))]
for row in plan:
    geoid: str = row["GEOID20"]  # Your field names may vary
    district: int = row["District"]  # Your field names may vary

    county: str = GeoID(geoid).county[2:]
    pop: int = population[geoid]

    i: int = district_to_index[district]
    j: int = county_to_index[county]

    CxD[i][j] += pop

### 4 - CALCULATE COUNTY-DISTRICT SPLITTING ###

results: dict = calc_county_district_splitting(CxD)

### 5 - PRINT THE RESULTS ###

print(f"County-district splitting:")
print(f"- County splitting: {results['county']:0.2f}")
print(f"- District splitting: {results['district']:0.2f}")

### END ###
