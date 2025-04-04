"""
UTILITIES FOR READING & WRITING AND WORKING WITH PLANS
"""

from typing import TypeAlias, List, Dict

from rdapy.utils import read_csv

Precinct: TypeAlias = str
District: TypeAlias = int
PlanCSV: TypeAlias = List[Dict[Precinct, District]]
GeoIDIndex: TypeAlias = Dict[Precinct, District]

Graph: TypeAlias = Dict[Precinct, List[Precinct]]
County: TypeAlias = str


def read_plan(plan_path: str) -> PlanCSV:
    """Read a precinct-assignment file."""

    return read_csv(plan_path, [str, int])


def index_plan(plan_csv: PlanCSV) -> GeoIDIndex:
    """Index a plan by geoid."""

    geoid_fields: List[str] = ["GEOID", "GEOID20", "GEOID30"]
    district_fields: List[str] = ["District", "DISTRICT"]

    keys: List[str] = list(plan_csv[0].keys())

    geoid_field: str = list(set(geoid_fields) & set(keys))[0]
    district_field: str = list(set(district_fields) & set(keys))[0]

    return {str(row[geoid_field]): int(row[district_field]) for row in plan_csv}


class ParseGeoID:
    """Parse a 15-character GeoIDs into its component parts."""

    def __init__(self, id: str) -> None:
        self.state: str = id[0:2]
        self.county: str = id[0:5]  # id[2:5]
        self.tract: str = id[0:11]  # id[5:11]
        self.bg: str = id[0:12]  # id[11:12]
        self.block: str = id  # id[12:15]


### END ###
