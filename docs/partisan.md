# Partisan

You can compute a full complement of partisan analytics for a set of districts all at once,
described next, or you can compute individual metrics, described in the subsequent sections.

## Partisan Analytics for a Set of Districts

To calculate all partisan analytics for a statewide two-party vote share and two-party vote shares by district:

```python
def calc_partisan_metrics(Vf: float, Vf_array: list[float]) -> dict:
```

This returns a dictionary of results:

```python
results: dict = {
    "bias": bias_measurements,
    "responsiveness": responsiveness_measurements,
    "dSVpoints": dSVpoints,
    "rSVpoints": rSVpoints,
    "averageDVf": averageDVf,
    "averageRVf": averageRVf,
}

# where:

bias_measurements: dict = {
    "bestS": bestS,
    "bestSf": bestSf,
    "estS": estS,
    "estSf": estSf,
    "deviation": deviation,
    "tOf": TOf,
    "fptpS": fptpS,
    "bS50": Bs50f,
    "bV50": Bv50f,
    "decl": decl,
    "rvPoints": rvPoints,
    "gSym": gSym,
    "gamma": gamma,
    "eG": EG,
    "bSV": BsGf,
    "prop": prop,
    "mMs": mMs,
    "mMd": mMd,
    "lO": LO,
}

responsiveness_measurements: dict = {
    "cSimple": Cn,
    "cD": cD,
    "cDf": cDf,
    "bigR": bigR,
    "littleR": littleR,
    "mIR": MIR,
    "rD": rD,
    "rDf": rDf,
}
```

The dictionary key names here match those in the relevant sections of the 
[Map Analytics Format](https://medium.com/dra-2020/map-analytics-export-format-d0aa75f6b041).

## Measures of Bias

The bias measures above are described in [Advanced Measures of Bias & Responsiveness](https://medium.com/dra-2020/advanced-measures-of-bias-responsiveness-c1bf182d29a9).
They may be calculated individually.

In the functions below:

* Vf - generally statewide two-party vote share, but sometimes the two-party vote share for a district
* Sf - statewide two-party seat share
* N - number of districts
* Vf_array - array of two-party vote shares by district

```python
def calc_best_seats(N: int, Vf: float) -> int:
```

```python
def calc_disproportionality_from_best(est_Sf: float, best_Sf: float) -> float:
```

```python
def calc_disproportionality(Vf: float, Sf: float) -> float:
```

```python
def calc_efficiency_gap(Vf: float, Sf: float) -> float:
```

```python
def calc_gamma(Vf: float, Sf: float, r: float) -> float:
```

```python
def est_seats_bias(sv_curve_pts: list[tuple[float, float]], N: int) -> float:
```

```python
def est_votes_bias(sv_curve_pts: list[tuple[float, float]], N: int) -> float:
```

```python
def est_geometric_seats_bias(
    Vf: float,
    d_sv_pts: list[tuple[float, float]],
    r_sv_pts: list[tuple[float, float]],
) -> float:
```

```python
def calc_global_symmetry(
    d_sv_pts: list[tuple[float, float]],
    r_sv_pts: list[tuple[float, float]],
    S50V: float,
) -> float:
```

```python
def calc_declination(Vf_array: list[float]) -> Optional[float]:
```

Note: This function supports both median difference using average district vote share and
median difference using statewide vote share, if provided.

```python
def calc_mean_median_difference(
    Vf_array: list[float], Vf: Optional[float] = None
) -> float:
```

```python
def calc_turnout_bias(Vf: float, Vf_array: list[float]) -> float:
```

```python
def calc_lopsided_outcomes(Vf_array: list[float]) -> Optional[float]:
```

## Measures of Responsiveness

Similarly, you can compute the responsiveness measures individually:

```python
def count_competitive_districts(Vf_array: list[float]) -> int:
```

```python
def est_competitive_districts(Vf_array: list[float]) -> float:
```

```python
def est_district_competitiveness(Vf: float) -> float:
```

```python
def est_responsiveness(
    Vf: float, sv_curve_pts: list[tuple[float, float]], N: int
) -> float:
```

```python
def calc_big_R(Vf: float, Sf: float) -> Optional[float]:
```

```python
def calc_minimal_inverse_responsiveness(Vf: float, r: float) -> Optional[float]:
```

```python
def est_responsive_districts(Vf_array: list[float]) -> float:
```

## Method

Finally, several functions expose John Nagle's method for estimating fractional seat
probabilities and district responsiveness and inferring seats-votes curves.

To estimate the fractional probability of a seat win for district, given a two-party vote share:

```python
def est_seat_probability(Vf: float) -> float:
```

Similarly, to estimate the responsiveness of a district, given a two-party vote share:

```python
def est_district_responsiveness(Vf: float) -> float:
```

To estimate the fractional # of seats for a set of two-party vote shares, using seat probabilities:

```python
def est_seats(Vf_array: list[float]) -> float:
```

To estimate the fractional # of seats for a set of two-party vote shares, using first past the post accounting:

```python
def est_fptp_seats(Vf_array: list[float]) -> int:
```

To infer the points of an seats-votes curve from a set of two-party vote shares by district,
using either proportional or uniform shifts in statewide vote share:

```python
def infer_sv_points(Vf: float, Vf_array: list[float], proportional=True) -> list[tuple]:
```

Finally, to infer the points of an *inverse* points from a set of inferred seats-votes curve points:

```python
def infer_inverse_sv_points(sv_pts: list[tuple], N: int) -> list[tuple[float, float]]:
```
