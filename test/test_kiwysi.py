#!/usr/bin/env python3

"""
TEST KIWYSI COMPACTNESS MODEL
"""

from rdapy.compactness import *
from pytest import approx


INDEX: int = 0
VALUE: int = 1


class TestKIWYSI:
    def test_first_20(self) -> None:
        """Replicate predictions for the first 20 shapes against the original, INCORRECT PCA model.

        Verifies correct *featureization* of the first 20 shapes.
        """

        sample_features_csv = "testdata/compactness/first20/smartfeats_first20.csv"
        featureized_shapes, predictions = load_features(sample_features_csv)

        sample_shapes_shp = "testdata/compactness/first20"
        source_shapes, _ = load_shapes(sample_shapes_shp, id="OBJECTID")

        for i, t in enumerate(predictions):
            score = t[VALUE]
            prediction = score_shape(
                source_shapes[i][VALUE], geodesic=True, revised=False
            )

            assert prediction == approx(score, abs=1)

    def test_evenly_spaced_20(self) -> None:
        """Replicate predictions for 20 evenly spaces shapes against the revised, CORRECT PCA model.

        Verifies both correct *featureization* and the correct PCA model.
        """

        sample_features_csv = "testdata/compactness/evenlyspaced20/evenlyspaced20.csv"
        featureized_shapes, predictions = load_features(sample_features_csv)

        sample_shapes_shp = "testdata/compactness/evenlyspaced20"
        source_shapes, _ = load_shapes(sample_shapes_shp, id="GEOID")

        for i, t in enumerate(predictions):
            score = t[VALUE]
            prediction = score_shape(
                source_shapes[i][VALUE], geodesic=True, revised=True
            )

            assert prediction == approx(score, abs=1)

    def test_rank_shape(self) -> None:
        assert rank_shape(77.6086471426305) == 78
        assert rank_shape(77.2586455094345) == 77
        assert rank_shape(25.00594161) == 25
        assert rank_shape(-32.4080845) == 1

    def test_rate_shape(self) -> None:
        assert rate_shape(1) == 100
        assert rate_shape(100) == 1


### END ###
