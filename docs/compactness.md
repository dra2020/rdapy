# Compactness

TODO

## Measures of Compactness for a Set of Shapes (Districts)

```python
def calc_compactness(shapes: list[Polygon | MultiPolygon]) -> dict:
    """Compute Reock, Polsby-Popper, and KIWYSI compactness for a set of districts and by district."""
```

```python
results: dict = {
    "avgReock": avg_reock,
    "avgPolsby": avg_polsby,
    "avgKIWYSI": avg_kiwysi,
    "byDistrict": by_district,
}
```

## Measures of Compactness for a Shape (Single District)

These are the "features" for Aaron Kaufman's "know it when you see it" (KIWYSI) compactness ML model.

TODO - geodesic vs. flat

```python
def calc_sym_x(shp: Polygon | MultiPolygon, geodesic: bool = True) -> float:
    """FEATURE 1: X-SYMMETRY

    The same as Y-SYMMETRY except reflect the district D around a horizontal line going through the centroid.
    See below.
    """
```

```python
def calc_sym_y(shp: Polygon | MultiPolygon, geodesic: bool = True) -> float:
    """FEATURE 2: Y-SYMMETRY

    The area of a district overlapping with its reflection around a vertical line going through the centroid,
    divided by the area of the district. Values range [1–2].

    1. Find the centroid
    2. Take the area of the district
    3. Flip the shape about its x or y axis, running through the centroid
    4. Calculate the union of the original shape and its mirror
    5. Take the ratio of the area of that union* and the area of the original shape
    """

```

```python
def calc_reock(shp: Polygon | MultiPolygon, geodesic: bool = True) -> float:
    """FEATURE 3: REOCK

    Reock is the primary measure of the dispersion of district shapes, calculated as
    “the area of the district to the area of the minimum spanning circle that can enclose the district.”

    R = A / A(Minimum Bounding Circle)
    R = A / (π * (d / 2)^2)

    R = 4A / πd^2

    This simplifies to:

    R = A / πr^2

    where r is the radius of the minimum bounding circle.
    """
```

```python
def calc_bbox(shp: Polygon | MultiPolygon, geodesic: bool = True) -> float:
    """FEATURE 4: "BOUNDING-BOX"

    This is shorthand for the ratio of the area of the district to the area of the minimum bounding box of the district.
    """
```

```python
def calc_polsby(shp: Polygon | MultiPolygon, geodesic: bool = True) -> float:
    """FEATURE 5: POLSBYPOPPER

    Polsby-Popper is the primary measure of the indentation of district shapes,
    calculated as the “the ratio of the area of the district to the area of a circle whose circumference
    is equal to the perimeter of the district.”

    PP = A / A(C)

    where C is that circle. In other words:

    P = 2πRc and A(C) = π(P / 2π)^2

    where P is the perimeter of the district and Rc is the radius of the circle.

    Hence, the measure simplifies to:

    PP = 4π * (A / P^2)
    """
```

```python
def calc_hull(shp: Polygon | MultiPolygon, geodesic: bool = True) -> float:
    """FEATURE 6: Hull(D)

    Convex Hull is a secondary measure of the dispersion of district shapes,
    calculated as “the ratio of the district area to the area of the minimum convex bounding polygon
    (also known as a convex hull) enclosing the district.”

    CH = A / A(Convex Hull)

    where a convex hull is the minimum perimeter that encloses all points in a shape,
    basically the shortest unstretched rubber band that fits around the shape.
    """
```

```python
def calc_schwartzberg(shp: Polygon | MultiPolygon, geodesic: bool = True) -> float:
    """FEATURE 7: SCHWARTZBERG

    Schwartzberg is a secondary measure of the
    degree of indentation of district shapes, calculated as “the ratio of the
    perimeter of the district to the circumference of a circle whose area is equal
    to the area of the district.”

    https://www.azavea.com/blog/2016/07/11/measuring-district-compactness-postgis/
    defines Schwartzberg as:

    S = 1 / (P / C)

    where P is the perimeter of the district and C is the circumference of the
    circle. The radius of the circle is:

    Rc = SQRT(A / π)

    So, the circumference of the circle is:

    C = 2πRc or C = 2π * SQRT(A / π)

    Hence:

    S = 1 / (P / 2π * SQRT(A / π))

    S = (2π * SQRT(A / π)) / P

    NOTE - Aaron's feature matches the verbal description of P/C (feature_helpers.R).
    """
```

## "Know it when you see it" (KIWYSI) Compactness

TODO - the result is raw, unconstrained and not normalized

```python

```python
def score_shape(
    shp: Polygon | MultiPolygon, *, geodesic: bool = True, revised: bool = True
) -> float:
    """Feature-ize a shape and then score it [1-100], smaller is better."""
```

```python
def rank_shape(raw_rank: float) -> float:
    """Constrain values to the range [1–100].

    Smaller is better.
    """
```
