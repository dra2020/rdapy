# Partisan

TODO

## Scorecard

```python
def calc_partisan_metrics(Vf: float, Vf_array: list[float]) -> dict:
    """Calculate partisan metrics for a set of districts and statewide vote share."""
```

The variable names here match those in the dra2020/dra-analytics TypeScript code.

## Measures of Bias

def calc_best_seats(N: int, Vf: float) -> int:
def calc_disproportionality_from_best(est_Sf: float, best_Sf: float) -> float:
def calc_disproportionality(Vf: float, Sf: float) -> float:
def calc_efficiency_gap(vote_share: float, seat_share: float) -> float:
def calc_gamma(Vf: float, Sf: float, r: float) -> float:
def est_seats_bias(sv_curve_pts: list[tuple[float, float]], total_seats: int) -> float:

def est_votes_bias(sv_curve_pts: list[tuple[float, float]], total_seats: int) -> float:
def est_geometric_seats_bias(
def calc_global_symmetry(
def key_RV_points(Vf_array: list[float]) -> dict[str, float]:
def is_sweep(Sf: float, n_districts: int) -> bool:

def calc_declination(Vf_array: list[float]) -> Optional[float]:
def calc_mean_median_difference(
def calc_turnout_bias(statewide: float, Vf_array: list[float]) -> float:
def calc_lopsided_outcomes(Vf_array: list[float]) -> Optional[float]:

## Measures of Responsiveness

def count_competitive_districts(Vf_array: list[float]) -> int:
def est_competitive_districts(Vf_array: list[float]) -> float:
def est_district_competitiveness(Vf: float) -> float:
def est_responsiveness(
def calc_big_R(Vf: float, Sf: float) -> Optional[float]:
def calc_minimal_inverse_responsiveness(Vf: float, r: float) -> Optional[float]:
def _is_balanced(Vf: float) -> bool:
def est_responsive_districts(vpi_by_district) -> float:

## Method

def est_seat_probability(vpi: float) -> float:
def est_district_responsiveness(vpi: float) -> float:
def est_seats(Vf_array: list[float]) -> float:
def est_fptp_seats(Vf_array: list[float]) -> int:
def infer_sv_points(Vf: float, Vf_array: list[float], proportional=True) -> list[tuple]:
def _shift_districts(
def _shift_districts_uniformly(
def _shift_districts_proportionally(
def infer_inverse_sv_points(sv_pts: list[tuple], N: int) -> list[tuple[float, float]]:
def infer_geometric_seats_bias_points(