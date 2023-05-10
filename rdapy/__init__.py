# rdapy/__init__.py

from .compactness import (
    calc_compactness,
    calc_sym_x,
    calc_sym_y,
    calc_reock,
    calc_bbox,
    calc_polsby,
    calc_hull,
    score_shape,
    rate_shape,
    rank_shape,
)
from .graph import is_connected, is_embedded, OUT_OF_STATE
from .equal import calc_population_deviation
from .splitting import calc_splitting, split_score  # TODO: More

name = "rdapy"
