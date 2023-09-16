#!/usr/bin/env python3

"""
Sample compactness analytics starting from raw data
"""

from rdapy import *
from testutils import *

### FILES ###

data_dir: str = "~/local/sample-data"

# Exported from DRA
plan_file: str = "NC_2022_Congress_Official.csv"

# This are the Census TIGER/Line block shape for the state.
shapes_file: str = "tl_2020_37_tabblock20"

## 1 - READ A BLOCK-ASSIGNMENT FILE ###

plan_path: str = os.path.expanduser(f"{data_dir}/{plan_file}")
plan = read_csv(plan_path, [str, int])

### 2 - READ THE BLOCK SHAPES ###

shapes_path: str = os.path.expanduser(f"{data_dir}/{shapes_file}")
shapes, _ = load_shapes(shapes_path, id="GEOID20")

### 3 - COLLAPSE BLOCKS INTO DISTRICT SHAPES ###

### 4 - COMPUTE COMPACTNESS METRICS ###

### 5 - PRINT THE RESULTS ###

pass

### END ###
