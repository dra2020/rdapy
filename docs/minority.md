# Minority

You can calculate compactness for a set of districts (shapes), as well as various measures of
compactness for a single district (shape) including "know it when you see it" (KIWYSI) compactness.

## Compactness for a Set of Districts

To compute average Reock, Polsby-Popper, and KIWYSI compactness for a set of districts (shapes) and by district:

```python
def calc_compactness(shapes: list[Polygon | MultiPolygon]) -> dict:
```

"shapes" are shapely Polygons or MultiPolygons:

```python
from shapely.geometry import Polygon, MultiPolygon
```

This returns a dictionary of results:

```python
results: dict = {
    "avgReock": avg_reock,
    "avgPolsby": avg_polsby,
    "avgKIWYSI": avg_kiwysi,
    "byDistrict": by_district,
}
```

For each district, the results are of the form:

```python
measures: dict = {
    "reock": reock_flat,
    "polsby": polsby_flat,
    "kiwysiRank": kiwysi_rank, # 1-100, smaller is better
}
```