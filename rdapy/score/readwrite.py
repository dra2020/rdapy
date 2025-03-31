"""
READ/WRITE ROUTINES
"""

from typing import Any, List, Dict, Optional, Tuple, OrderedDict

import os, csv, json, pickle
from csv import DictReader, DictWriter

from shapely.geometry import (
    shape,
    Polygon,
    MultiPolygon,
    Point,
    MultiPoint,
    LineString,
    MultiLineString,
    LinearRing,
    GeometryCollection,
)
import fiona


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


def file_name(parts: List[str], delim: str = "_", ext: Optional[str] = None) -> str:
    """Construct a file name with parts separated by the delimeter and ending with the extension."""

    name: str = delim.join(parts) + "." + ext if ext else delim.join(parts)

    return name


def path_to_file(parts: List[str], naked: bool = False) -> str:
    """Return the directory path to a file (but not the file)."""

    rel_path: str = "/".join(parts)

    if not naked:
        rel_path = rel_path + "/"

    return rel_path


### CSV ###


def read_csv(rel_path: str, types: Optional[list] = None) -> List[Dict]:
    """Read a CSV with DictReader. Return a list of dicts.

    Patterned after: https://stackoverflow.com/questions/8748398/python-csv-dictreader-type
    """

    abs_path: str = FileSpec(rel_path).abs_path

    try:
        rows: List = []
        with open(abs_path, "r", encoding="utf-8-sig") as file:
            reader: DictReader[str] = DictReader(
                file, fieldnames=None, restkey=None, restval=None, dialect="excel"
            )
            fieldnames: List[str] = list(reader.fieldnames) if reader.fieldnames else []
            field_types: List[Any] = types if types else [str] * len(fieldnames)
            for t in field_types:
                assert t in [str, int, float]

            for row_in in reader:
                if len(field_types) >= len(fieldnames):
                    # Extract the values in the same order as the csv header
                    ivalues: map[str | Any | None] = map(row_in.get, fieldnames)

                    # Apply type conversions
                    iconverted: List = [x(y) for (x, y) in zip(field_types, ivalues)]

                    # Pass the field names and the converted values to the dict constructor
                    row_out: Dict = dict(zip(fieldnames, iconverted))

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
                mod: Dict = dict()
                for k, v in row.items():
                    if isinstance(v, float):
                        mod[k] = precision.format(v)
                    else:
                        mod[k] = v
                writer.writerow(mod)

    except:
        raise Exception("Exception writing CSV.")


### JSON ###


def read_json(rel_path: str) -> Dict[str, Any]:
    """Load a JSON file into a dictionary."""

    try:
        abs_path: str = FileSpec(rel_path).abs_path

        with open(abs_path, "r") as f:
            return json.load(f)

    except:
        raise Exception("Exception reading JSON.")


def read_jsonl(rel_path: str) -> List[Dict[str, Any]]:
    abs_path: str = FileSpec(rel_path).abs_path
    with open(abs_path, "r") as f:
        return [json.loads(line) for line in f]


def write_json(rel_path, data) -> None:
    """Write a JSON file from a dictionary."""

    try:
        abs_path: str = FileSpec(rel_path).abs_path

        with open(abs_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except:
        raise Exception("Exception writing JSON.")


### LOAD A SHAPEFILE ###


def read_shapes(shp_file: str, id: str) -> Tuple[dict, Optional[Dict[str, Any]]]:
    """Load a shapefile into a dictionary of shapes keyed by the value of the specified field."""

    shp_path: str = os.path.expanduser(shp_file)
    shapes_by_id: Dict = dict()
    meta: Optional[Dict[str, Any]] = None

    with fiona.Env():
        with fiona.open(shp_path) as source:
            if source:
                meta = source.meta
                for item in source:
                    obj_id: str = item["properties"][id]
                    shp: (
                        Point
                        | MultiPoint
                        | LineString
                        | MultiLineString
                        | Polygon
                        | MultiPolygon
                        | LinearRing
                        | GeometryCollection
                    ) = shape(
                        item["geometry"]
                    )  # type: ignore

                    shapes_by_id[obj_id] = shp

    return shapes_by_id, meta


### LOAD SCORES ###


def read_scores(scores_path: str) -> List[OrderedDict[str, Any]]:
    """Load and undefined set of scores from a CSV file."""

    results: List[OrderedDict[str, Any]] = []

    with open(os.path.expanduser(scores_path), "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            typed_row: OrderedDict = OrderedDict()
            for key, value in row.items():
                # Keep the map/plan name as a string
                if key == "map":
                    typed_row[key] = value.strip()
                    continue

                # Skip empty values
                if value == "":
                    typed_row[key] = None
                    continue

                # Try to convert to most specific type
                try:
                    # First try integer
                    typed_row[key] = int(value)
                except ValueError:
                    try:
                        # Then try float
                        typed_row[key] = float(value)
                    except ValueError:
                        # If both fail, keep as string
                        # Remove any surrounding whitespace
                        typed_row[key] = value.strip()

            results.append(typed_row)

    return results


### PICKLING ###


def write_pickle(rel_path, obj) -> bool:
    """Pickle a Python object to a file."""

    abs_path: str = FileSpec(rel_path).abs_path

    try:
        with open(abs_path, "wb") as handle:
            pickle.dump(obj, handle, protocol=pickle.HIGHEST_PROTOCOL)
        return True
    except Exception as e:
        print("Exception pickling: ", e)
        return False


def read_pickle(rel_path) -> Any:
    """Unpickle a Python object from a file."""

    abs_path: str = FileSpec(rel_path).abs_path

    try:
        with open(abs_path, "rb") as handle:
            return pickle.load(handle)
    except Exception as e:
        print("Exception unpickling: ", e)
        return None


### END ###
