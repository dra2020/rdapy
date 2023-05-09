#!/usr/bin/env python3

"""
DEBUG
"""

from rdapy.splitting import *
from testutils import *

sample: dict = read_json("testdata/splitting/samples/splitting-AZ-benchmark.json")
CxD: list[list[float]] = sample["countyByDistrict"]

# County & district totals
cTActual: list[float] = county_totals(CxD)
dTActual: list[float] = district_totals(CxD)

# Reduce county & district splits

rDActual: list[list[float]] = reduceDistrictSplits(CxD, cTActual)
rDExpected: list[list[float]] = [
    [
        359045,
        0,
        0,
        0,
        26230,
        0,
        0,
        0,
        2994,
        1635,
        0,
        92091,
        197708,
        0,
        30521,
        0,
    ],
    [131346, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 578878, 0, 0, 0, 0],
    [47420, 0, 0, 0, 0, 0, 0, 0, 225734, 0, 0, 309294, 545, 0, 0, 127231],
    [
        20489,
        0,
        0,
        0,
        27367,
        0,
        0,
        0,
        37268,
        198551,
        0,
        0,
        177517,
        0,
        180512,
        68520,
    ],
    [0, 0, 0, 0, 0, 0, 0, 0, 710224, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 710224, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 710224, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 710225, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 710224, 0, 0, 0, 0, 0, 0, 0],
]
matrix_approx_equal(rDActual, rDExpected, places=0)

pass

### END ###
