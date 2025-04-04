# rdapy/score/utils/__init__.py

from .constants import (
    DISTRICTS_BY_STATE,
    COUNTIES_BY_STATE,
    OUT_OF_STATE,
    is_water_only,
    EPSILON,
)

from .types import (
    Precinct,
    District,
    PlanCSV,
    GeoIDIndex,
    Graph,
    County,
    ParseGeoID,
    # Legacy for test cases
    read_plan,
    index_plan,
    # TODO - DELETE
    # write_plan,
)

from .approxequal import approx_equal

from .readwrite import (
    file_name,
    path_to_file,
    read_csv,
    write_csv,
    read_json,
    read_jsonl,
    write_json,
    read_shapes,
    read_scores,
)

from .data import (
    load_data,
    load_graph,
    collect_metadata,
    geoids_from_precinct_data,
    # Legacy for test cases
    unpack_input_data,
)

from .ensemble_io import (
    smart_read,
    smart_write,
    format_scores,
    # Legacy for test cases
    write_record,
    read_record,
)


name: str = "utils"
