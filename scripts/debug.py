#!/usr/bin/env python3

"""
DEBUG
"""

from pyproj import CRS
from pytest import approx

from rdapy import *

INDEX: int = 0
VALUE: int = 1

sample_features_csv = "testdata/compactness/first20/smartfeats_first20.csv"
featureized_shapes, predictions = load_features(sample_features_csv)

sample_shapes_shp = "testdata/compactness/first20"
source_shapes, _ = load_shapes(sample_shapes_shp, id="OBJECTID")

for i, t in enumerate(predictions):
    score = t[VALUE]
    prediction = score_shape(source_shapes[i][VALUE], geodesic=True, revised=False)

    print(f"{i+1}: Prediction = {prediction}, Score = {score}")

    assert prediction == approx(score, abs=1)
    pass

pass

# sample_features_csv = "testdata/compactness/evenlyspaced20/evenlyspaced20.csv"
# featureized_shapes, predictions = load_features(sample_features_csv)

# sample_shapes_shp = "testdata/compactness/evenlyspaced20"
# source_shapes, _ = load_shapes(sample_shapes_shp, id="GEOID")

# pass

# # Replicate predicted compactness scores from feature-ized sample shapes
# score_featureized_shapes(featureized_shapes, predictions)


# # Replicate feature-ization of sample shapes (geodesic calcs)
# featureize_shapes(source_shapes, featureized_shapes)


# # Replicate predicted compactness scores from sample shapes
# score_shapes(source_shapes, predictions)

### END ###
