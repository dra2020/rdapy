# rdapy/__init__.py

from .base import (
    EPSILON,
    OUT_OF_STATE,
    OUT_OF_STATE_THRESHOLD,
    DatasetKey,
    Aggregates,
    #
    read_csv,
    read_json,
    write_csv,
    write_json,
    load_features,
    load_shapes,
    index_shapes,
    abstract_data,
    abstract_shape,
    #
    approx_equal,
    vector_approx_equal,
    matrix_approx_equal,
    #
    get_dataset,
    get_datasets,
    get_fields,
)

from .compactness import (
    calc_compactness,
    calc_sym_x,
    calc_sym_y,
    calc_reock,
    calc_bbox,
    calc_polsby,
    calc_hull,
    calc_schwartzberg,
    #
    featureize_shape,
    score_features,
    kiwysi_rank_shape,
    trim_kiwysi_rank,
    #
    make_circle,
    reock_formula,
    polsby_formula,
)

from .equal import calc_population_deviation

from .graph import (
    is_consistent,
    is_connected,
    is_embedded,
    connected_subsets,
    generate_contiguity_mods,
    Connection,
)

from .minority import (
    calc_proportional_districts,
    est_minority_opportunity,
    calc_minority_opportunity,
    DEMOGRAPHICS,
)

from .splitting import (
    calc_county_district_splitting,
    #
    split_score,
    county_totals,
    district_totals,
    #
    calc_county_fractions,
    calc_county_weights,
    county_split_score,
    county_splitting,
    calc_county_splitting,
    #
    calc_district_fractions,
    calc_district_weights,
    district_split_score,
    district_splitting,
    calc_district_splitting,
    #
    calc_county_splitting_reduced,
    calc_district_splitting_reduced,
    reduce_county_splits,
    reduce_district_splits,
    #
    calc_coi_splitting,
    uncertainty_of_membership,
    effective_splits,
)

from .partisan import (
    calc_partisan_metrics,
    #
    calc_best_seats,
    calc_declination,
    calc_disproportionality,
    calc_disproportionality_from_best,
    calc_efficiency_gap,
    calc_gamma,
    calc_global_symmetry,
    calc_lopsided_outcomes,
    calc_mean_median_difference,
    calc_turnout_bias,
    est_fptp_seats,
    est_geometric_seats_bias,
    est_seat_probability,
    est_seats,
    est_seats_bias,
    est_votes_bias,
    #
    calc_big_R,
    calc_minimal_inverse_responsiveness,
    count_competitive_districts,
    est_competitive_districts,
    est_district_competitiveness,
    est_district_responsiveness,
    est_responsive_districts,
    est_responsiveness,
    #
    infer_inverse_sv_points,
    infer_sv_points,
)

from .rate import (
    rate_proportionality,
    rate_competitiveness,
    rate_minority_opportunity,
    rate_reock,
    rate_polsby,
    rate_compactness,
    rate_county_splitting,
    rate_district_splitting,
    rate_splitting,
)

# TODO -- Organize this
from .score import (
    aggregate_districts,
    aggregate_plans,
    calc_geographic_baseline,
    collect_metadata,
    County,
    deserialize_bits,
    District,
    DISTRICTS_BY_STATE,
    eval_partisan_lean,
    format_scores,
    GeoIDIndex,
    Graph,
    index_data,
    index_geoids,
    init_bit_array,
    load_data,
    load_graph,
    load_neighborhoods,
    make_neighborhood,
    MetadataRecord,
    nearest_connected_neighbor,
    Neighbor,
    ParseGeoID,
    PlanCSV,
    PlanRecord,
    Precinct,
    read_record,
    reverse_index,
    score_plan,
    score_plans,
    serialize_bits,
    set_bit,
    smart_read,
    smart_write,
    sorted_geoids,
    unpack_neighborhood,
    write_record,
)


name = "rdapy"
