"""
CONSTANTS

TODO - Move these.
"""

from typing import Any, List, Dict

### STATES ###

DISTRICTS_BY_STATE: Dict[str, Any] = {
    "AL": {"congress": 7, "upper": 35, "lower": 105},
    "AK": {"congress": 1, "upper": 20, "lower": 40},
    "AZ": {"congress": 9, "upper": 30, "lower": None},
    "AR": {"congress": 4, "upper": 35, "lower": 100},
    "CA": {"congress": 52, "upper": 40, "lower": 80},
    "CO": {"congress": 8, "upper": 35, "lower": 65},
    "CT": {"congress": 5, "upper": 36, "lower": 151},
    "DE": {"congress": 1, "upper": 21, "lower": 41},
    "FL": {"congress": 28, "upper": 40, "lower": 120},
    "GA": {"congress": 14, "upper": 56, "lower": 180},
    "HI": {"congress": 2, "upper": 25, "lower": 51},
    "ID": {"congress": 2, "upper": 35, "lower": None},
    "IL": {"congress": 17, "upper": 59, "lower": 118},
    "IN": {"congress": 9, "upper": 50, "lower": 100},
    "IA": {"congress": 4, "upper": 50, "lower": 100},
    "KS": {"congress": 4, "upper": 40, "lower": 125},
    "KY": {"congress": 6, "upper": 38, "lower": 100},
    "LA": {"congress": 6, "upper": 39, "lower": 105},
    "ME": {"congress": 2, "upper": 35, "lower": 151},
    "MD": {"congress": 8, "upper": 47, "lower": 67},
    "MA": {"congress": 9, "upper": 40, "lower": 160},
    "MI": {"congress": 13, "upper": 38, "lower": 110},
    "MN": {"congress": 8, "upper": 67, "lower": 134},
    "MS": {"congress": 4, "upper": 52, "lower": 122},
    "MO": {"congress": 8, "upper": 34, "lower": 163},
    "MT": {"congress": 2, "upper": 50, "lower": 100},
    "NE": {"congress": 3, "upper": 49, "lower": None},
    "NV": {"congress": 4, "upper": 21, "lower": 42},
    "NH": {"congress": 2, "upper": 24, "lower": 164},
    "NJ": {"congress": 12, "upper": 40, "lower": None},
    "NM": {"congress": 3, "upper": 42, "lower": 70},
    "NY": {"congress": 26, "upper": 63, "lower": 150},
    "NC": {"congress": 14, "upper": 50, "lower": 120},
    "ND": {"congress": 1, "upper": 47, "lower": 49},
    "OH": {"congress": 15, "upper": 33, "lower": 99},
    "OK": {"congress": 5, "upper": 48, "lower": 101},
    "OR": {"congress": 6, "upper": 30, "lower": 60},
    "PA": {"congress": 17, "upper": 50, "lower": 203},
    "RI": {"congress": 2, "upper": 38, "lower": 75},
    "SC": {"congress": 7, "upper": 46, "lower": 124},
    "SD": {"congress": 1, "upper": 35, "lower": 37},
    "TN": {"congress": 9, "upper": 33, "lower": 99},
    "TX": {"congress": 38, "upper": 31, "lower": 150},
    "UT": {"congress": 4, "upper": 29, "lower": 75},
    "VT": {"congress": 1, "upper": 13, "lower": 104},
    "VA": {"congress": 11, "upper": 40, "lower": 100},
    "WA": {"congress": 10, "upper": 49, "lower": None},
    "WV": {"congress": 2, "upper": 17, "lower": 100},
    "WI": {"congress": 8, "upper": 33, "lower": 99},
    "WY": {"congress": 1, "upper": 31, "lower": 62},
}

COUNTIES_BY_STATE: Dict[str, int] = {
    "AL": 67,
    "AK": 30,
    "AZ": 15,
    "AR": 75,
    "CA": 58,
    "CO": 64,
    "CT": 8,
    "DE": 3,
    "FL": 67,
    "GA": 159,
    "HI": 5,
    "ID": 44,
    "IL": 102,
    "IN": 92,
    "IA": 99,
    "KS": 105,
    "KY": 120,
    "LA": 64,
    "ME": 16,
    "MD": 24,
    "MA": 14,
    "MI": 83,
    "MN": 87,
    "MS": 82,
    "MO": 115,
    "MT": 56,
    "NE": 93,
    "NV": 17,
    "NH": 10,
    "NJ": 21,
    "NM": 33,
    "NY": 62,
    "NC": 100,
    "ND": 53,
    "OH": 88,
    "OK": 77,
    "OR": 36,
    "PA": 67,
    "RI": 5,
    "SC": 46,
    "SD": 66,
    "TN": 95,
    "TX": 254,
    "UT": 29,
    "VT": 14,
    "VA": 133,
    "WA": 39,
    "WV": 55,
    "WI": 72,
    "WY": 23,
}


def is_water_only(geoid):
    """A more general solution: A lexical hack to identify water-only precincts that are sometimes missing from plans."""

    return geoid.endswith("ZZZZZZ")


### MISCELLANEOUS ###

# EPSILON: float = 1 / (10**6)

### END ###
