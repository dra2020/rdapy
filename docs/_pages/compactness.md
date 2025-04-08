---
layout: page
title: Compactness
permalink: compactness/
---

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

KYIWYSI compactness is described below.

## Measures of Compactness for One District (Shape)

These are functions to calculate compactness for a single district (shape).
They are seven are the "features" for Aaron Kaufman's "know it when you see it" (KIWYSI) compactness ML model,
which is described in the next section.

These functions can compute their metric either assuming the Earth is curved (geodesic=True) 
or assuming it is flat (geodesic=False). [The Earth is, obviously, spherical, but sometimes compactness
is calculated on a flat plane.]

Y-symmetry is the area of a district overlapping with its reflection around a vertical line going through 
the centroid, divided by the area of the district. Values range [1–2].

```python
def calc_sym_y(shp: Polygon | MultiPolygon, geodesic: bool = True) -> float:
```

 X-symmetry is the same as Y-symmetry except the district is reflected over a horizontal line going through 
 the centroid.
 
```python
def calc_sym_x(shp: Polygon | MultiPolygon, geodesic: bool = True) -> float:
```

Reock is the primary measure of the dispersion of district shapes, calculated as
“the area of the district to the area of the minimum spanning circle that can enclose the district.”

```python
def calc_reock(shp: Polygon | MultiPolygon, geodesic: bool = True) -> float:
```

"Bounding-box" here is shorthand for "the ratio of the area of the district to the area of the minimum 
bounding box of the district."

```python
def calc_bbox(shp: Polygon | MultiPolygon, geodesic: bool = True) -> float:
```

Polsby-Popper is the primary measure of the indentation of district shapes,
calculated as the “the ratio of the area of the district to the area of a circle whose circumference
is equal to the perimeter of the district.”

```python
def calc_polsby(shp: Polygon | MultiPolygon, geodesic: bool = True) -> float:
```

Convex Hull is a secondary measure of the dispersion of district shapes,
calculated as “the ratio of the district area to the area of the minimum convex bounding polygon
(also known as a convex hull) enclosing the district.”

```python
def calc_hull(shp: Polygon | MultiPolygon, geodesic: bool = True) -> float:
```

Schwartzberg is a secondary measure of the
degree of indentation of district shapes, calculated as “the ratio of the
perimeter of the district to the circumference of a circle whose area is equal
to the area of the district.”

```python
def calc_schwartzberg(shp: Polygon | MultiPolygon, geodesic: bool = True) -> float:
```

## "Know it when you see it" (KIWYSI) Compactness

KIYWSI compactness implements Kaufman, King, and Komisarchik's 
["know it when you see it" (KIWYSI) compactness model](https://gking.harvard.edu/compact).

To feature-ize a shape and then rank it [1-100], smaller is better:

```python
def kiwysi_rank_shape(
    shp: Polygon | MultiPolygon, *, geodesic: bool = True, revised: bool = True
) -> float:
```

The above gives raw results which may fall outside the range [1–100]. 
To constrain them to that range:

```python
def trim_kiwysi_rank(raw_rank: float) -> float:
```
