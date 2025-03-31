import math
import random
from typing import NamedTuple, Iterator, Callable

# adapted from "Smallest enclosing disks (balls and ellipsoids)" by EMO WELZL, p.362


class Point(NamedTuple):
    x: float
    y: float


class Circle(NamedTuple):
    center: Point
    r: float


class AlecCircle(NamedTuple):
    x: float
    y: float
    r: float


class WelzlCircle(NamedTuple):
    circle: Circle
    defining: list[Point]


def B_MINIDISK(points: list[Point], R: list[Point]) -> WelzlCircle:
    if len(points) == 0 or len(R) == 3:
        return b_md(points, R)
    p = points[0]
    remaining: list[Point] = points[1:]
    D: WelzlCircle = B_MINIDISK(remaining, R)
    if not D.defining or not new_in_circle(D.circle, p):
        return B_MINIDISK(remaining, R + [p])
    return D


# non-recursive version of B_MINIDISK
def wl_B_MINIDISK(points: list[Point], _: list[Point]) -> WelzlCircle:
    wl: list[tuple[tuple[int, int], list[Point]]] = [((0, 0), [])]
    retval: WelzlCircle = WelzlCircle(Circle(Point(999, 999), 999), [])  # phony value
    while wl:
        (index, phase), R = wl.pop()
        if phase == 0:
            if index >= len(points) or len(R) == 3:
                retval = b_md([], R)
            else:
                wl.append(((index, 1), R))
                wl.append(((index + 1, 0), R))
        elif phase == 1:
            if not retval.defining or not new_in_circle(retval.circle, points[index]):
                # wl.append(((index, 2), R)) # phase 2 is a no-op
                wl.append(((index + 1, 0), R + [points[index]]))
        # elif phase == 2:
        #     continue
        else:
            raise ValueError("phase out of range")

    return retval


def b_md(points: list[Point], R: list[Point]) -> WelzlCircle:
    if len(R) == 0:
        return WelzlCircle(Circle(Point(0, 0), 0), [])
    elif len(R) == 1:
        return WelzlCircle(Circle(R[0], 0), R)
    elif len(R) == 2:
        return WelzlCircle(
            Circle(
                Point((R[0].x + R[1].x) / 2, (R[0].y + R[1].y) / 2),
                math.hypot(R[0].x - R[1].x, R[0].y - R[1].y) / 2,
            ),
            R,
        )
    elif len(R) == 3:
        c: Circle = circleRadius(R[0], R[1], R[2])
        return WelzlCircle(c, R)
    else:
        raise ValueError("R is too large")


def new_in_circle(D: Circle, p: Point) -> bool:
    return math.hypot(D.center.x - p.x, D.center.y - p.y) <= D.r


# adapted from https://stackoverflow.com/questions/52990094/calculate-circle-given-3-points-code-explanation
def circleRadius(b: Point, c: Point, d: Point) -> Circle:
    temp: float = c[0] ** 2 + c[1] ** 2
    bc: float = (b[0] ** 2 + b[1] ** 2 - temp) / 2
    cd: float = (temp - d[0] ** 2 - d[1] ** 2) / 2
    det: float = (b[0] - c[0]) * (c[1] - d[1]) - (c[0] - d[0]) * (b[1] - c[1])

    if abs(det) < 1.0e-10:
        raise ValueError(f"The three points are colinear {b}, {c}, {d}")

    # Center of circle
    cx: float = (bc * (c[1] - d[1]) - cd * (b[1] - c[1])) / det
    cy: float = ((b[0] - c[0]) * cd - (c[0] - d[0]) * bc) / det

    radius: float = ((cx - b[0]) ** 2 + (cy - b[1]) ** 2) ** 0.5

    return Circle(Point(cx, cy), radius)


# ----------------------------------------------------------------------------
# Todd's driver routine to marry it to Alec's code


def stride(points: list[Point]) -> Iterator[Point]:
    half = len(points) // 2
    yield from stride0([points[:half], points[half:]])


def stride0(L: list[list[Point]]) -> Iterator[Point]:
    if len(L) == 0:
        return
    left: list[list[Point]] = []
    right: list[list[Point]] = []
    for v in L:
        if len(v) == 0:
            continue
        yield v[0]
        remaining = v[1:]
        half = len(remaining) // 2
        left.append(remaining[:half])
        right.append(remaining[half:])
    yield from stride0(left + right)


def do_make_circle(
    points: list[tuple[float, float]],
    fn: Callable[[list[Point], list[Point]], WelzlCircle],
) -> AlecCircle:
    ordered = list(set(Point(x, y) for x, y in points))
    # ordered: list[Point] = [Point(x, y) for x, y in set(points)]
    for _ in range(10):
        try:
            random.shuffle(ordered)  # shuffle to avoid worst case
            # ordered = list(stride(ordered))  # optimize for convex hull path?
            # ordered = list(reversed(ordered))
            x: WelzlCircle = fn(ordered, [])
            return AlecCircle(x.circle.center.x, x.circle.center.y, x.circle.r)
        except ValueError:
            # print(f"Unable to find circle after {_} tries")
            continue
    raise ValueError("Unable to find circle after 10 tries")


# DO NOT USE THIS FUNCTION because of recursion depth issues
def new_make_circle(points: list[tuple[float, float]]) -> AlecCircle:
    return do_make_circle(points, B_MINIDISK)


# uses non-recursive version of B_MINIDISK
def wl_make_circle(points: list[tuple[float, float]]) -> AlecCircle:
    return do_make_circle(points, wl_B_MINIDISK)


### END ###
