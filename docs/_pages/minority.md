---
layout: page
title: Opportunity for Minority Representation
permalink: minority/
---

You can estimate the opportunity for minority representation.

```python
def calc_minority_metrics(
    statewide_demos: dict[str, float], demos_by_district: list[dict[str, float]]
) -> dict[str, float]:
```

where "statewide_demos" is a dictionary of statewide demographic totals, and
"demos_by_district" is a list of dictionaries of demographic totals by district.

Examples can be found in the "demographics" section of the profiles in the testdata/CD116 directory.

This returns a dictionary of results:

```python
results: dict[str, float] = {
    "opportunity_districts": od,
    "proportional_opportunities": pod,
    "coalition_districts": cd,
    "proportional_coalitions": pcd
}
```