# rdapy/score/__init__.py

from .constants import (
    STATES,
    STATE_NAMES,
    STATE_FIPS,
    DISTRICTS_BY_STATE,
    COUNTIES_BY_STATE,
    OUT_OF_STATE,
    OTHER_POTENTIAL_BORDERS,
    is_water_only,
    EPSILON,
    STUDY_STATES,
    ENSEMBLE_STATES,
)
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

from .data import unpack_input_data, geoids_from_precinct_data, collect_metadata

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

from .majority_minority import calculate_mmd_simple

from .approxequal import (
    approx_equal,
    # vector_approx_equal,
    # matrix_approx_equal,
    # dict_approx_equal,
)

# TODO
# from .analyze import analyze_plan, default_datasets
# from .aggregate import Aggregates, Datasets, get_dataset, DatasetKey, get_fields
# from .score_ensemble import score_ensemble

name: str = "score"
