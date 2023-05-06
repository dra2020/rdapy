#!/usr/bin/env python3

"""
DEBUG
"""

from pyproj import CRS
from rdapy import *


sample_features_csv = "testdata/compactness/first20/smartfeats_first20.csv"
featureized_shapes, predictions = load_features(sample_features_csv)

sample_shapes_shp = "testdata/compactness/first20"
source_shapes, _ = load_shapes(sample_shapes_shp, id="OBJECTID")


sample_features_csv = "testdata/compactness/evenlyspaced20/evenlyspaced20.csv"
featureized_shapes, predictions = load_features(sample_features_csv)

sample_shapes_shp = "testdata/compactness/evenlyspaced20"
source_shapes, _ = load_shapes(sample_shapes_shp, id="GEOID")

pass

# Replicate predicted compactness scores from feature-ized sample shapes
score_featureized_shapes(featureized_shapes, predictions)


# Replicate feature-ization of sample shapes (geodesic calcs)
featureize_shapes(source_shapes, featureized_shapes)


# Replicate predicted compactness scores from sample shapes
score_shapes(source_shapes, predictions)

### END ###
