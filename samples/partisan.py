#!/usr/bin/env python3

"""
Sample partisan analytics
"""

from rdapy import *
from testutils import *

# Load data

sample_path: str = f"testdata/partisan/nagle/partisan-NC-2012.json"
sample: dict = read_json(sample_path)

Vf: float = sample["statewide"]
Vf_array: list[float] = sample["byDistrict"]

# Calculate metrics

results: dict = calc_partisan_metrics(Vf, Vf_array)

# Print the results

print(f"Partisan analytics:")
print(results)

### END ###
