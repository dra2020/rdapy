#!/usr/bin/env python3

"""
Sample compactness analytics
"""

from rdapy import *
from testutils import *

# Load data

sample_path: str = f"testdata/compactness/NC-116th-Congressional"
shapes, _ = load_shapes(sample_path, id="id")
shapes = [item[1] for item in shapes]  # discard the id

# Calculate metrics

results: dict = calc_compactness(shapes)

# Print the results

print(f"Compactness analytics:")
print(results)

### END ###
