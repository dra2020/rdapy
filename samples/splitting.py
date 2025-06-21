#!/usr/bin/env python3

"""
Sample county-districting splitting
"""

from rdapy import *
from testutils import *

# Load data

sample_path: str = f"testdata/splitting/splitting-AZ-benchmark.json"
sample: dict = read_json(sample_path)

CxD: list[list[float]] = sample["countyByDistrict"]

# Calculate metrics

results: dict = calc_county_district_splitting(CxD)

# Print the results

print(f"County-district splitting:")
print(results)

### END ###
