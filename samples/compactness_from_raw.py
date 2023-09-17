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

### 1 - READ THE DISTRICT SHAPES OR CONSTRUCT THEM FROM BLOCK SHAPES ###

# Load the district shapes from a shapefile:
shapes_path: str = os.path.expanduser(f"{district_shapes_path}")
shapes, _ = load_shapes(shapes_path, id="id")
shapes = [item[1] for item in shapes]  # discard the id

# Or construct them from block shapes and a block-assigment file:
shapes_path: str = os.path.expanduser(f"{data_dir}/{shapes_file}")
blocks_gdf: GeoDataFrame = geopandas.read_file(shapes_path)
blocks_df: pd.Series | pd.DataFrame | Any = blocks_gdf[["geometry", "GEOID20"]]
del blocks_gdf
assert isinstance(blocks_df, pd.DataFrame)

plan_path: str = os.path.expanduser(f"{data_dir}/{plan_file}")
plan_gdf: GeoDataFrame = geopandas.read_file(plan_path)
plan_df: pd.Series | pd.DataFrame | Any = plan_gdf[["GEOID20", "District"]]
del plan_gdf
assert isinstance(plan_df, pd.DataFrame)

blocks_df = blocks_df.merge(
    plan_df,
    how="left",
    left_on="GEOID20",
    right_on="GEOID20",
)
blocks_df = blocks_df[["geometry", "GEOID20", "District"]]
assert isinstance(blocks_df, GeoDataFrame)
del plan_df

districts_df = blocks_df.dissolve(by="District", as_index=False)

unsorted_shapes: list[dict] = districts_df.to_dict("records")
sorted_shapes: list[dict] = sorted(unsorted_shapes, key=lambda k: k["District"])
shapes = [s["geometry"] for s in sorted_shapes]  # discard the id

### 4 - COMPUTE COMPACTNESS METRICS ###

results: dict = calc_compactness(shapes)

### 5 - PRINT THE RESULTS ###

print(f"Partisan compactness analytics:")
print(results)

pass

### END ###
