"""
ENSEMBLE I/O
"""

from typing import Any, Optional, Dict, Generator, TextIO, TypedDict

import os, sys, contextlib, json, zipfile, io, tempfile


class PlanRecord(TypedDict):
    _tag_: str
    name: str
    plan: Dict[str, int]


class MetadataRecord(TypedDict):
    _tag_: str
    properties: Dict[str, Any]


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
    """
    Context manager that reads from stdin if filename is None,
    or from a file (supporting regular files and ZIP files containing JSONL).
    Also handles ZIP content piped to stdin.
    """
    if filename is None or filename == "-":
        # Read from stdin, but check if it's ZIP content
        stdin_data = sys.stdin.buffer.read()  # Read as bytes

        # Check if this looks like ZIP data (ZIP files start with 'PK')
        if stdin_data.startswith(b"PK"):
            print("Detected ZIP content from stdin", file=sys.stderr)

            # Write to temporary file and process as ZIP
            with tempfile.NamedTemporaryFile(suffix=".zip", delete=False) as temp_zip:
                temp_zip.write(stdin_data)
                temp_zip_path = temp_zip.name

            try:
                with zipfile.ZipFile(temp_zip_path, "r") as zip_file:
                    file_list = zip_file.namelist()
                    jsonl_files = [f for f in file_list if f.endswith(".jsonl")]

                    if not jsonl_files:
                        raise ValueError(f"No .jsonl file found in ZIP from stdin")

                    if len(jsonl_files) > 1:
                        print(
                            f"Warning: Multiple .jsonl files found in ZIP. Using: {jsonl_files[0]}",
                            file=sys.stderr,
                        )

                    jsonl_filename = jsonl_files[0]

                    # Extract to temporary file
                    with tempfile.TemporaryDirectory() as temp_dir:
                        zip_file.extract(jsonl_filename, path=temp_dir)
                        extracted_path = os.path.join(temp_dir, jsonl_filename)

                        # Read the extracted file
                        with open(extracted_path, "r", encoding="utf-8") as f:
                            yield f
            finally:
                # Clean up temp ZIP file
                try:
                    os.unlink(temp_zip_path)
                except OSError:
                    pass
        else:
            # Regular text content from stdin
            text_content = stdin_data.decode("utf-8")
            text_stream = io.StringIO(text_content)
            yield text_stream
    else:
        if filename.endswith(".zip"):
            with zipfile.ZipFile(filename, "r") as zip_file:
                file_list = zip_file.namelist()
                jsonl_files = [f for f in file_list if f.endswith(".jsonl")]

                if not jsonl_files:
                    raise ValueError(f"No .jsonl file found in ZIP archive: {filename}")

                if len(jsonl_files) > 1:
                    print(
                        f"Warning: Multiple .jsonl files found in ZIP. Using: {jsonl_files[0]}",
                        file=sys.stderr,
                    )

                jsonl_filename = jsonl_files[0]

                # Extract to temporary file
                with tempfile.TemporaryDirectory() as temp_dir:
                    zip_file.extract(jsonl_filename, path=temp_dir)
                    extracted_path = os.path.join(temp_dir, jsonl_filename)

                    # Read the extracted file
                    with open(extracted_path, "r", encoding="utf-8") as f:
                        yield f
        else:
            with open(filename, "r", encoding="utf-8") as f:
                yield f


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


### END ###
