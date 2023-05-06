#!/usr/bin/env python3

"""
DEBUG
"""

from pyproj import CRS
from rdapy import *

"""
describe('Score the first 20 reference shapes', () =>
{
    test('Using async/await', async () =>
    {
        const featureEntries: T.FeaturesEntry[] = FU.readFeatureSets('testdata/compactness/first20/smartfeats_first20.csv');
        const shapes: GeoJSON.FeatureCollection = await FU.readShapefile('./testdata/compactness/first20/first20.shp');

        for (let i in featureEntries)
        {
        const featureEntry: T.FeaturesEntry = featureEntries[i];
        const score: number = featureEntry.score;

        const prediction: number = kiwysiScoreShapeRAW(shapes.features[i], T.PCAModel.Original);

        expect(prediction).toBeCloseTo(score, 1);
        }
    });
});
"""

sample_features_csv = "testdata/compactness/first20/smartfeats_first20.csv"
featureized_shapes, predictions = load_features(sample_features_csv)

sample_shapes_shp = "testdata/compactness/first20"
source_shapes, _ = load_shapes(sample_shapes_shp, id="OBJECTID")

for i in range(len(sample_features_csv)):
    score = predictions[i][VALUE]
    prediction = score_shape(source_shapes[i][VALUE], geodesic=True)

    continue

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
