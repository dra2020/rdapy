#!/usr/bin/env python3

"""
TEST KIWYSI COMPACTNESS MODEL
"""

from pytest import approx

from rdapy import load_features, load_shapes, kiwysi_rank_shape, trim_kiwysi_rank

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
            prediction = kiwysi_rank_shape(
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
            prediction = kiwysi_rank_shape(
                source_shapes[i][VALUE], geodesic=True, revised=True
            )

            assert prediction == approx(score, abs=1)

    def test_trim_kiwysi_rank(self) -> None:
        assert trim_kiwysi_rank(102.3) == 100.0
        assert trim_kiwysi_rank(77.2586455094345) == 77.2586455094345
        assert trim_kiwysi_rank(-32.4080845) == 1.0


### END ###
