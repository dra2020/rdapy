---
layout: page
title: County-District & COI Splitting
permalink: splitting/
---

You can calculate county-district splitting metrics, as well as community of interest (COI) splitting metrics.

## County & District Splitting

To calculate the county & district splitting scores for a plan:

```python
def calc_county_district_splitting(CxD: list[list[float]]) -> dict:
```

where "CxD" is are county totals (columns) by district (rows), i.e.,
each row represents a district, and each value in the row represents 
the number of people in that county in that district.

Examples can be found in the "counties" section of the profiles in the testdata/CD116 directory.

This returns a simple dictionary of results:

```python
result: dict = {"county": county, "district": district}
```

These measures are described in [Measuring County & District Splitting](https://medium.com/dra-2020/measuring-county-district-splitting-48a075bcce39). 
Note: The example in figure shows districts as columns and counties as rows, the opposite of how
they are represented in the code.
As that post describes, these measures are based on Moon Duchin's raw square root entropy split score:

```python
def split_score(split: list[float]) -> float:
```

## Community of Interest (COI) Splitting

To calculate the COI splitting for a set of communities:

```python
def calc_coi_splitting(communities: list[dict[str, list[float]]]) -> dict:
```

where "communities" is a list of communities of interest (COIs), each of which is a dictionary with a "name" and "splits" entry, the latter being a list of floats in the range [0-1] representing how a COI is fractionated 
across districts.

This returns a dictionary of results:

```python
results: dict = {"byCOI": by_coi}
```

where the entry for each COI is of the form:

```python
{"name": coi["name"], "effectiveSplits": es, "uncertainty": u}
```

These two measures are described in [COI Splitting](https://medium.com/dra-2020/coi-splitting-b7c9b541e175).

The metrics can also be called individually:

```python
def uncertainty_of_membership(splits: list[float]) -> float:
```

```python
def effective_splits(splits: list[float]) -> float:
```

where "splits" is, again, a list of floats in the range [0-1] representing how a COI 
is fractionated across districts.