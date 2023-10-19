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
results: dict[str, float] = {
    "opportunity_districts": od,
    "proportional_opportunities": pod,
    "coalition_districts": cd,
    "proportional_coalitions": pcd
}
```