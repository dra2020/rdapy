# Splitting

TODO

## County & District Splitting

```python
def calc_county_district_splitting(CxD: list[list[float]]) -> dict:
    """Calculate the county & district splitting scores for a plan."""
```

```python
result: dict = {"county": county, "district": district}
```

```python
def split_score(split: list[float]) -> float:
    """Moon Duchin's raw split score"""
```

## Community of Interest (COI) Splitting

```python
def calc_coi_splitting(communities: list[dict[str, list[float]]]) -> dict:
    """Calculate the COI metrics for a set of communities of interest."""
```

```python
analysis: dict = {"byCOI": by_coi}
```

```python
def uncertainty_of_membership(splits: list[float]) -> float:
    """Calculate the uncertainty of membership for a set of splits."""
```

```python
def effective_splits(splits: list[float]) -> float:
    """Calculate the effective splits for a set of splits."""
```