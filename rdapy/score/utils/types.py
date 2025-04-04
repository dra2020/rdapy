"""
UTILITIES FOR READING & WRITING AND WORKING WITH PLANS
"""

from typing import TypeAlias, List, Dict, Any, Optional

import os, json
from csv import DictReader

# from .readwrite import read_csv, FileSpec

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


### CLONED FROM testutils/readwrite.py -- TODO: Rationalize these ###


class FileSpec:
    """Parse a file path into its components."""

    def __init__(self, path: str, name=None) -> None:
        file_name: str
        file_extension: str
        file_name, file_extension = os.path.splitext(path)

        self.rel_path: str = path
        self.abs_path: str = os.path.abspath(path)
        self.name: str = name.lower() if (name) else os.path.basename(file_name).lower()
        self.extension: str = file_extension


def read_csv(rel_path: str, types: Optional[list] = None) -> list[dict]:
    """Read a CSV with DictReader. Return a list of dicts.

    Patterned after: https://stackoverflow.com/questions/8748398/python-csv-dictreader-type
    """

    abs_path: str = FileSpec(rel_path).abs_path

    try:
        rows: list = []
        with open(abs_path, "r", encoding="utf-8-sig") as file:
            reader: DictReader[str] = DictReader(
                file, fieldnames=None, restkey=None, restval=None, dialect="excel"
            )
            fieldnames: list[str] = list(reader.fieldnames) if reader.fieldnames else []
            field_types: list[Any] = types if types else [str] * len(fieldnames)
            for t in field_types:
                assert t in [str, int, float]

            for row_in in reader:
                if len(field_types) >= len(fieldnames):
                    # Extract the values in the same order as the csv header
                    ivalues: map[str | Any | None] = map(row_in.get, fieldnames)

                    # Apply type conversions
                    iconverted: list = [x(y) for (x, y) in zip(field_types, ivalues)]

                    # Pass the field names and the converted values to the dict constructor
                    row_out: dict = dict(zip(fieldnames, iconverted))

                    rows.append(row_out)

        return rows

    except:
        raise Exception("Exception reading CSV with explicit types.")


def write_json(rel_path, data) -> None:
    """Write a JSON file from a dictionary."""

    try:
        abs_path: str = FileSpec(rel_path).abs_path

        with open(abs_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except:
        raise Exception("Exception writing JSON.")


### END ###
