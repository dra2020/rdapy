#!/usr/bin/env python3

"""
TEST KIWYSI COMPACTNESS MODEL
"""

from rdapy.compactness import *
from pytest import approx


class TestKIWYSI:
    def test_first_20(self) -> None:
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

        assert True  # TODO

    def test_evenly_spaced_20(self) -> None:
        """
        describe('Score the evenly spaced 20 reference shapes', () =>
        {
            test('Using async/await', async () =>
            {
                const featureEntries: T.FeaturesEntry[] = FU.readFeatureSets('testdata/compactness/evenlyspaced20/evenlyspaced20.csv');
                const shapes: GeoJSON.FeatureCollection = await FU.readShapefile('./testdata/compactness/evenlyspaced20/evenlyspaced20.shp');

                for (let i in featureEntries)
                {
                const featureEntry: T.FeaturesEntry = featureEntries[i];
                const score: number = featureEntry.score;

                const prediction: number = kiwysiScoreShapeRAW(shapes.features[i], T.PCAModel.Revised);

                expect(prediction).toBeCloseTo(score, 0);
                }
            });
        });
        """

        sample_features_csv = "testdata/compactness/evenlyspaced20/evenlyspaced20.csv"
        featureized_shapes, predictions = load_features(sample_features_csv)

        sample_shapes_shp = "testdata/compactness/evenlyspaced20"
        source_shapes, _ = load_shapes(sample_shapes_shp, id="GEOID")

        assert True


### END ###
