#!/usr/bin/env python3

"""
DEBUG
"""

from rdapy.equal import *
from testutils import *

from collections import defaultdict

profile: dict = read_json("testdata/population/population-NC-116th.json")
max_pop: int = max(profile["byDistrict"])
min_pop: int = min(profile["byDistrict"])
target_pop: int = profile["targetSize"]
print(calc_population_deviation(max_pop, min_pop, target_pop))

pass

### END ###
