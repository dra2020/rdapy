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


class ParseGeoID:
    """Parse a 15-character GeoIDs into its component parts."""

    def __init__(self, id: str) -> None:
        self.state: str = id[0:2]
        self.county: str = id[0:5]  # id[2:5]
        self.tract: str = id[0:11]  # id[5:11]
        self.bg: str = id[0:12]  # id[11:12]
        self.block: str = id  # id[12:15]


### END ###
