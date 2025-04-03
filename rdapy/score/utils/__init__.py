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
    read_plan,
    index_plan,
    write_plan,
    ParseGeoID,
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

# TODO - Rationalize imports
from .data import (
    load_data_map,
    load_data,
    load_graph,
    unpack_input_data,
    geoids_from_precinct_data,
    collect_metadata,
)

from .ensemble_io import (
    PlanRecord,
    MetadataRecord,
    ensemble_plans,
    smart_write,
    write_record,
    smart_read,
    read_record,
    format_scores,
    capture_warnings,
)


name: str = "utils"
