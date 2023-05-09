#!/usr/bin/env python3

"""
DEBUG
"""

from rdapy.splitting import *
from testutils import *

sample: dict = read_json("testdata/splitting/samples/splitting-AZ-benchmark.json")
CxD: list[list[float]] = sample["countyByDistrict"]
cT: list[float] = county_totals(CxD)
dT: list[float] = district_totals(CxD)

pass

### END ###
