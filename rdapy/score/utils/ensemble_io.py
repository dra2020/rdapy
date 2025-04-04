"""
ENSEMBLE I/O
"""

from typing import Any, Optional, Dict, Generator, TextIO

import os, sys, contextlib, json


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


@contextlib.contextmanager
def smart_read(
    filename: Optional[str] = None,
) -> Generator[TextIO | TextIO, None, None]:
    """Read from a file or stdin."""

    if filename and filename != "-":
        fh: TextIO = open(os.path.expanduser(filename), "r")
    else:
        fh = sys.stdin

    try:
        yield fh
    finally:
        if fh is not sys.stdin:
            fh.close()


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


### LEGACY HELPERS FOR TEST CASES ###


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


### END ###
