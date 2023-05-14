# Partisan

TODO

## Scorecard

```python
def calc_partisan_metrics(Vf: float, Vf_array: list[float]) -> dict:
    """Calculate partisan metrics for a set of districts and statewide vote share."""
```

The variable names here match those in the dra2020/dra-analytics TypeScript code.

## Measures of Bias

```python
def calc_best_seats(N: int, Vf: float) -> int:
```

```python
def calc_disproportionality_from_best(est_Sf: float, best_Sf: float) -> float:
    """B% - The deviation from proportionality calculated as ^S% — S%"""
```

```python
def calc_disproportionality(Vf: float, Sf: float) -> float:
    """PR - raw disproportionality"""
```

```python
def calc_efficiency_gap(vote_share: float, seat_share: float) -> float:
    """EG - Calculate the efficiency gap"""
```

NOTE - This alternate formulation is consistent with the rest of our metrics,
where '+' = R bias; '-' = D bias. It's *not* the same as the other common version:

EG = (Seat Share – 50%)  – (2 × (Vote Share – 50%))


```python
def calc_gamma(Vf: float, Sf: float, r: float) -> float:
    """GAMMA

    g = 50 + r<V>(<V>-50) – S(<V>)
    """
```

```python
def est_seats_bias(sv_curve_pts: list[tuple[float, float]], total_seats: int) -> float:
    """BS_50 - Seats bias as a fraction of N"""
```

```python
def est_votes_bias(sv_curve_pts: list[tuple[float, float]], total_seats: int) -> float:
    """BV_50 - Votes bias as a fraction"""
```

```python
def est_geometric_seats_bias(
    statewide_vote_share: float,
    d_sv_pts: list[tuple[float, float]],
    r_sv_pts: list[tuple[float, float]],
) -> float:
    """BS_V - Estimate geometric seats bias (@ V = statewide vote share)"""
```

```python
def calc_global_symmetry(
    d_sv_pts: list[tuple[float, float]],
    r_sv_pts: list[tuple[float, float]],
    S50V: float,
) -> float:
    """GS - Global symmetry

    * gSym is the area of asymmetry between the two curves.
    * The choice of what base to normalize it by is somewhat arbitrary.
    * We actually only infer the S–V curve over the range [0.25–0.75] <<< 101 points (not 100!)
    * But dividing by 100 normalizes the area of asymmetry to the area of the SxV unit square.
    """
```

```python
def calc_declination(Vf_array: list[float]) -> Optional[float]:
    """Declination is calculated using the key r(v) points, defined in Fig. 16.

    NOTE - District vote shares are D shares, so party A = Rep & B = Dem.
    """
```

```python
def calc_mean_median_difference(
    Vf_array: list[float], Vf: Optional[float] = None
) -> float:
    """Both:
    * MM  - Mean – median difference using statewide Vf -and-
    * MM' - Mean – median difference using average district Vf
    """
```

```python
def calc_turnout_bias(statewide: float, Vf_array: list[float]) -> float:
    """TO - Turnout bias

    The difference between the statewide turnout and the average district turnout
    """
```

```python
def calc_lopsided_outcomes(Vf_array: list[float]) -> Optional[float]:
    """LO - Lopsided outcomes

    This is a measure of packing bias is:

    LO = (1⁄2 - vB) - (vA – 1⁄2)     Eq. 5.4.1 on P. 26

    "The ideal for this measure is that the excess vote share for districts
    won by party A averaged over those districts equals the excess vote share
    for districts won by party B averaged over those districts.
    A positive value of LO indicates greater packing of party B voters and,
    therefore, indicates a bias in favor of party A."
    """
```

## Measures of Responsiveness

```python
def count_competitive_districts(Vf_array: list[float]) -> int:
    """Cn - Count the # of competitive districts, defined as [45–55%]."""
```

```python
def est_competitive_districts(Vf_array: list[float]) -> float:
    """cD - The estimated # of competitive districts"""
```

```python
def est_district_competitiveness(Vf: float) -> float:
    """Estimate the district competitiveness, a synonym for responsiveness."""
```

```python
def est_responsiveness(
    Vf: float, sv_curve_pts: list[tuple[float, float]], N: int
) -> float:
    """Estimate responsiveness (little 'r') at the statewide vote share (Vf)"""
```

```python
def calc_big_R(Vf: float, Sf: float) -> Optional[float]:
    """BIG 'R'"""
```

```python
def calc_minimal_inverse_responsiveness(Vf: float, r: float) -> Optional[float]:
    """MIR - Minimal inverse responsiveness

    zeta = (1 / r) - (1 / r_sub_max)     : Eq. 5.2.1

    where r_sub_max = 10 or 20 for balanced and unbalanced states, respectively.
    """
```

```python
def est_responsive_districts(vpi_by_district) -> float:
    """Estimate the # of responsive districts [R(d)], given a set of VPI's"""
```

## Method

```python
def est_seat_probability(vpi: float) -> float:
    """Estimate the fractional probability of a seat win for district, given a VPI"""
```

```python
def est_district_responsiveness(vpi: float) -> float:
    """Estimate the responsiveness of a district, given a VPI"""
```

```python
def est_seats(Vf_array: list[float]) -> float:
    """S# - The estimated # of Democratic seats, using seat probabilities"""
```

```python
def est_fptp_seats(Vf_array: list[float]) -> int:
    """S! - The estimated # of Democratic seats, using first past the post"""
```

```python
def infer_sv_points(Vf: float, Vf_array: list[float], proportional=True) -> list[tuple]:
    """Infer the points of an S/V curve from a set of VPI's by district,
    using either proportional or uniform shifts in statewide vote share."""
```

```python
def infer_inverse_sv_points(sv_pts: list[tuple], N: int) -> list[tuple[float, float]]:
    """Infer the points of an inverse S/V curve from a set of S/V curve points."""
```
