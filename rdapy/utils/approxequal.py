#!/usr/bin/env python3

"""
ROUGH EQUALITY UTILITIES
"""


from pytest import approx
from typing import Any


def approx_equal(x: float, y: float, places: int = 6) -> bool:
    """Check if two floats are approximately equal"""

    return x == approx(y, abs=(10 ** (-places)) * 0.5)


def vector_approx_equal(
    actual: list[float | int], expected: list[float | int], places: int = 6
) -> bool:
    """Check if two vectors of numbers are approximately equal"""

    if len(actual) != len(expected):
        return False

    return actual == approx(expected, abs=(10 ** (-places)) * 0.5)


def matrix_approx_equal(
    actual: list[list[float | int]], expected: list[list[float | int]], places: int = 6
) -> bool:
    """Check if a 2D matrix of numbers are approximately equal"""

    for i in range(len(actual)):
        if not vector_approx_equal(actual[i], expected[i], places):
            return False

    return True


def dict_approx_equal(actual: dict, expected: dict, int_threshold: int = 0) -> bool:
    """Check if two dictionaries are approximately equal"""

    for key in expected:
        if key not in actual:
            return False

        a: Any = actual[key]
        e: Any = expected[key]

        if type(a) == float and type(e) == float:
            if not approx_equal(a, e):
                return False
        elif type(a) == int and type(e) == int:
            # int_threshold = 1 to allow for rounding differences
            if abs(a - e) > int_threshold:
                return False
        else:
            if a != e:
                return False

    return True


# DON'T LIMIT WHAT GETS EXPORTED.

### END ###
