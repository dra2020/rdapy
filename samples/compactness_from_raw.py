#!/usr/bin/env python3

"""
Sample compactness analytics starting from raw data
"""

import pandas as pd
import geopandas
from geopandas import GeoDataFrame

from rdapy import *
from testutils import *

### FILES ###

data_dir: str = "~/local/sample-data"

# Exported from DRA
plan_file: str = "NC_2022_Congress_Official.csv"

district_shapes_path: str = f"testdata/compactness/NC-116th-Congressional"
# This are the Census TIGER/Line block shapes for the state.
shapes_file: str = "tl_2020_37_tabblock20"

## 1 - READ A BLOCK-ASSIGNMENT FILE ###

plan_path: str = os.path.expanduser(f"{data_dir}/{plan_file}")
plan = read_csv(plan_path, [str, int])

### 2 - READ THE DISTRICT SHAPES OR CONSTRUCT THEM FROM BLOCK SHAPES ###

# Load the district shapes from a shapefile:
shapes_path: str = os.path.expanduser(f"{district_shapes_path}")
shapes, _ = load_shapes(shapes_path, id="id")
shapes = [item[1] for item in shapes]  # discard the id

# Or construct them from block shapes:
shapes_path: str = os.path.expanduser(f"{data_dir}/{shapes_file}")
blocks_gdf: GeoDataFrame = geopandas.read_file(shapes_path)
blocks_df: pd.Series[Any] | pd.DataFrame | Any = blocks_gdf[["geometry", "GEOID20"]]
assert isinstance(blocks_df, pd.DataFrame)

# TODO - HERE
regions_gdf: GeoDataFrame = geopandas.read_file(regions_baf_path)
regions_df: pd.Series[Any] | pd.DataFrame | Any = regions_gdf[["GEOID", "REGION"]]
assert isinstance(regions_df, pd.DataFrame)

### 3 - COLLAPSE BLOCKS INTO DISTRICT SHAPES ###

### 4 - COMPUTE COMPACTNESS METRICS ###

results: dict = calc_compactness(shapes)

### 5 - PRINT THE RESULTS ###

print(f"Partisan compactness analytics:")
print(results)

pass

### END ###
