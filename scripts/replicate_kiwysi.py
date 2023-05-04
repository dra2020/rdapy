#!/usr/bin/env python3
#
# SAMPLE CODE TO REPLICATE THE KIWYSI COMPACTNESS MODEL

from pyproj import CRS

from kiwysic import *


# Load the sample shapes and the features derived from them

sample_shapes_shp = 'samples/first20'
source_shapes, _ = load_shapes(sample_shapes_shp)

sample_features_csv = 'samples/smartfeats_first20.csv'
featureized_shapes, predictions = load_features(sample_features_csv)


# Replicate predicted compactness scores from feature-ized sample shapes
score_featureized_shapes(featureized_shapes, predictions)


# Replicate feature-ization of sample shapes (geodesic calcs)
featureize_shapes(source_shapes, featureized_shapes)


# Replicate predicted compactness scores from sample shapes
score_shapes(source_shapes, predictions)
