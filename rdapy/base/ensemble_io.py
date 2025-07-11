"""
ENSEMBLE I/O
"""

from typing import Any, Optional, Dict, Generator, TextIO, TypedDict

import os, sys, contextlib, json, zipfile, tempfile


class PlanRecord(TypedDict):
    _tag_: str
    name: str
    plan: Dict[str, int]


class MetadataRecord(TypedDict):
    _tag_: str
    properties: Dict[str, Any]


def format_scores(
    scores_in: Dict[str, int | float], *, precision="{:.6f}"
) -> Dict[str, int | float]:
    """Format scores to a desired, fixed precision."""

    scores_out: Dict = dict()
    for k, v in scores_in.items():
        if isinstance(v, float):
            scores_out[k] = precision.format(v)
        else:
            scores_out[k] = v

    return scores_out


def read_record(line) -> Dict[str, Any]:
    record = json.loads(line.strip())

    return record


def write_record(record: Any, outstream: TextIO) -> None:
    """
    Write a plan or metadata record as a JSONL "line" to a file

    The indent=None forces the JSON to be written on a single line
    The sort_keys=True sorts the keys alphabetically, which is good for consistency
    """

    json.dump(record, outstream, indent=None, sort_keys=True)
    outstream.write("\n")


### SMART READ/WRITE CONTEXT MANAGERS ###


@contextlib.contextmanager
def smart_read(
    filename: Optional[str] = None,
) -> Generator[TextIO | TextIO, None, None]:
    """
    Context manager that reads from stdin if filename is None,
    or from a file (supporting regular files and a zipped JSONL).
    """
    if filename is None or filename == "-":
        yield sys.stdin
    elif filename.endswith(".zip"):
        with _read_zip_file(filename) as f:
            yield f
    else:
        with open(filename, "r", encoding="utf-8") as f:
            yield f


@contextlib.contextmanager
def _read_zip_file(zip_path: str) -> Generator[TextIO, None, None]:
    """Extract and read a .jsonl file from a ZIP archive."""

    with zipfile.ZipFile(zip_path, "r") as zip_file:
        jsonl_filename = _find_jsonl_in_zip(zip_file)

        with tempfile.TemporaryDirectory() as temp_dir:
            zip_file.extract(jsonl_filename, path=temp_dir)
            extracted_path = os.path.join(temp_dir, jsonl_filename)

            with open(extracted_path, "r", encoding="utf-8") as f:
                yield f


def _find_jsonl_in_zip(zip_file: zipfile.ZipFile) -> str:
    """Find and return the first .jsonl file in a ZIP archive."""

    file_list = zip_file.namelist()
    jsonl_files = [f for f in file_list if f.endswith(".jsonl")]

    if not jsonl_files:
        raise ValueError("No .jsonl file found in ZIP archive")

    if len(jsonl_files) > 1:
        print(
            f"Warning: Multiple .jsonl files found in ZIP. Using: {jsonl_files[0]}",
            file=sys.stderr,
        )

    return jsonl_files[0]


@contextlib.contextmanager
def smart_write(
    filename: Optional[str] = None,
) -> Generator[TextIO | TextIO, None, None]:
    """Write to a file or stdout.

    Patterned after: https://stackoverflow.com/questions/17602878/how-to-handle-both-with-open-and-sys-stdout-nicely
    """

    if filename and filename != "-":
        fh: TextIO = open(os.path.expanduser(filename), "w")
    else:
        fh = sys.stdout

    try:
        yield fh
    finally:
        if fh is not sys.stdout:
            fh.close()


### END ###
