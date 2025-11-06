# rdapy/__init__.py

from .base import (
    EPSILON,
    OUT_OF_STATE,
    OUT_OF_STATE_THRESHOLD,
    DISTRICTS_BY_STATE,
    COUNTIES_BY_STATE,
    is_water_only,
    DatasetKey,
    DatasetType,
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
    load_neighborhoods,
    #
    approx_equal,
    vector_approx_equal,
    matrix_approx_equal,
    #
    get_dataset,
    get_datasets,
    get_fields,
    #
    DistanceLedger,
    distance_proxy,
    distance,
    #
    Precinct,
    District,
    PlanCSV,
    GeoIDIndex,
    Graph,
    County,
    ParseGeoID,
    #
    load_data,
    load_graph,
    collect_metadata,
    sorted_geoids,
    index_data,
    #
    smart_read,
    smart_write,
    format_scores,
    write_record,
    read_record,
    MetadataRecord,
    PlanRecord,
    #
    init_bit_array,
    set_bit,
    serialize_bits,
    deserialize_bits,
    index_geoids,
    reverse_index,
)

from .compactness import (
    calc_compactness_metrics,
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
    # make_circle,
    wl_make_circle,
    reock_formula,
    polsby_formula,
    #
    calc_cut_score,
    calc_spanning_tree_score,
    _split_graph_by_districts,
    #
    calc_energy,
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
    calc_minority_metrics,
    DEMOGRAPHICS,
    calculate_mmd_with_comparisons,
    calculate_mmd_simple,
)

from .splitting import (
    calc_splitting_metrics,
    split_score,
    #
    calc_coi_splitting,
    uncertainty_of_membership,
    effective_splits,
)

from .partisan import (
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
    #
    calc_efficiency_gap_wasted_votes,
    calc_average_margin,
    #
    Neighbor,
    make_neighborhood,
    unpack_neighborhood,
    calc_geographic_baseline,
    eval_partisan_lean,
    #
    calc_gallagher_index,
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

from .aggregate import (
    aggregate_districts,
    aggregate_plans,
)

from .score import (
    score_plan,
    score_plans,
    #
    calc_general_category,
    calc_partisan_category,
    calc_minority_category,
    calc_compactness_category,
    calc_splitting_category,
)


name = "rdapy"
