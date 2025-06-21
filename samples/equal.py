#!/usr/bin/env python3

"""
Sample population deviation
"""

from rdapy import *

# Load data

sample_path: str = f"testdata/population/population-NC-116th.json"
sample: dict = read_json(sample_path)

max_pop: int = max(sample["byDistrict"])
min_pop: int = min(sample["byDistrict"])
target_pop: int = sample["targetSize"]

# Calculate metrics

result: float = calc_population_deviation(max_pop, min_pop, target_pop)

# Print the results

print(f"Population deviation:")
print(result)

### END ###
