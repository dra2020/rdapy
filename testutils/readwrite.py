#!/usr/bin/env python3

"""
READ/WRITE ROUTINES
"""

import os
from csv import DictReader, DictWriter
import json
from typing import Any, Optional


### FILE NAMES & PATHS ###


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


### CSV ###


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


def write_csv(rel_path, rows, cols, *, precision="{:.6f}", header=True) -> None:
    """Write a CSV file from a list of dicts."""

    try:
        abs_path: str = FileSpec(rel_path).abs_path

        with open(abs_path, "w") as f:
            writer: DictWriter = DictWriter(f, fieldnames=cols)
            if header:
                writer.writeheader()

            for row in rows:
                mod: dict = dict()
                for k, v in row.items():
                    if isinstance(v, float):
                        mod[k] = precision.format(v)
                    else:
                        mod[k] = v
                writer.writerow(mod)

    except:
        raise Exception("Exception writing CSV.")


### JSON ###


def read_json(rel_path) -> dict[str, Any]:
    """Load a JSON file into a dictionary."""

    try:
        abs_path: str = FileSpec(rel_path).abs_path

        with open(abs_path, "r") as f:
            return json.load(f)

    except:
        raise Exception("Exception reading JSON.")


def write_json(rel_path, data) -> None:
    """Write a JSON file from a dictionary."""

    try:
        abs_path: str = FileSpec(rel_path).abs_path

        with open(abs_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except:
        raise Exception("Exception writing JSON.")


### END ###
