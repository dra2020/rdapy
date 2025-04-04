# rdapy/__init__.py

from .compactness import (
    calc_compactness,
    calc_sym_x,
    calc_sym_y,
    calc_reock,
    calc_bbox,
    calc_polsby,
    calc_hull,
    calc_schwartzberg,
    featureize_shape,
    score_features,
    kiwysi_rank_shape,
    trim_kiwysi_rank,
    make_circle,
    reock_formula,
    polsby_formula,
)

from .equal import calc_population_deviation

from .graph import is_connected, is_embedded, OUT_OF_STATE

from .minority import (
    calc_proportional_districts,
    est_minority_opportunity,
    calc_minority_opportunity,
    DEMOGRAPHICS,
)

from .splitting import (
    calc_county_district_splitting,
    split_score,
    calc_county_fractions,
    calc_county_weights,
    county_split_score,
    county_splitting,
    calc_county_splitting,
    calc_district_fractions,
    calc_district_weights,
    district_split_score,
    district_splitting,
    calc_district_splitting,
    reduce_county_splits,
    reduce_district_splits,
    county_totals,
    district_totals,
    calc_county_splitting_reduced,
    calc_district_splitting_reduced,
    calc_coi_splitting,
    uncertainty_of_membership,
    effective_splits,
)

from .partisan import (
    calc_partisan_metrics,
    calc_best_seats,
    calc_disproportionality_from_best,
    calc_disproportionality,
    calc_efficiency_gap,
    calc_gamma,
    est_seats_bias,
    est_votes_bias,
    est_geometric_seats_bias,
    calc_global_symmetry,
    calc_declination,
    calc_mean_median_difference,
    calc_turnout_bias,
    calc_lopsided_outcomes,
    count_competitive_districts,
    est_competitive_districts,
    est_district_competitiveness,
    est_responsiveness,
    calc_big_R,
    calc_minimal_inverse_responsiveness,
    est_responsive_districts,
    est_seat_probability,
    est_district_responsiveness,
    est_seats,
    est_fptp_seats,
    infer_sv_points,
    infer_inverse_sv_points,
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

from .score import (
    aggregate_plans,
    Aggregates,
    score_plans,
    smart_read,
    smart_write,
    read_record,
    write_record,
    geoids_from_precinct_data,
    collect_metadata,
    load_data,
    load_graph,
    write_json,
    format_scores,
)


name = "rdapy"
