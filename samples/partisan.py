#!/usr/bin/env python3

"""
Sample partisan analytics
"""

from rdapy import *
from testutils import *

# Load data

xx: str = "NC"
yyyy: str = "2012"

profile_path: str = f"testdata/partisan/nagle/partisan-{xx}-{yyyy}.json"
profile: dict = read_json(profile_path)

Vf: float = profile["statewide"]
Vf_array: list[float] = profile["byDistrict"]

# Calculate metrics

scorecard: dict = calc_partisan_metrics(Vf, Vf_array)

# Print the results

print(f"Partisan analytics for {xx} {yyyy}:")
print(scorecard)

### END ###
