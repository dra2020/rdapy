#!/usr/bin/env python3

"""
DEBUG
"""

from rdapy.partisan import *
from testutils import *

"""CA 2012 from research project #2 w/ John Nagle"""

profile_path: str = "testdata/partisan/nagle/partisan-CA-2012.json"
profile: dict = read_json(profile_path)


s: dict = calc_partisan_metrics(profile["statewide"], profile["byDistrict"])

x = s["bias"]["bSV"]
# assert approx_equal(s["bias"]["bSV"], 0.0330327, places=4)

y = s["bias"]["lO"]
# assert approx_equal(s["bias"]["lO"], 9.23242870162867 / 100, places=4)

pass

### END ###
