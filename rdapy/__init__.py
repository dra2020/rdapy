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
    kiwysi_rank_shape,
    trim_kiwysi_rank,
)
from .equal import calc_population_deviation
from .graph import is_connected, is_embedded, OUT_OF_STATE
from .minority import (
    calc_proportional_districts,
    est_minority_opportunity,
)  # TODO: More
from .splitting import (
    calc_county_district_splitting,
    split_score,
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

name = "rdapy"
