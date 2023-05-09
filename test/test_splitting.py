#!/usr/bin/env python3

"""
TEST SPLITTING
"""


from rdapy.splitting import *
from testutils import *


class TestSplitting:
    def test_split_score(self) -> None:
        """These tests replicate the examples at the end of Section 6.1.1 of Moon Duchin's Appendix."""

        # A = 1.16
        assert approx_equal(split_score([97 / 100, 3 / 100]), 1.16, places=2)
        # B = 1.28
        assert approx_equal(split_score([88 / 100, 12 / 100]), 1.28, places=2)
        # C = 1.41
        assert approx_equal(split_score([50 / 100, 50 / 100]), 1.41, places=2)
        # D = 1.26
        assert approx_equal(split_score([96 / 100, 2 / 100, 2 / 100]), 1.26, places=2)
        # E = 1.71
        assert approx_equal(split_score([50 / 100, 25 / 100, 25 / 100]), 1.71, places=2)
        # F = 1.73
        assert approx_equal(
            split_score([33.3 / 100, 33.3 / 100, 33.3 / 100]), 1.73, places=2
        )
        # G = 2.00
        assert approx_equal(
            split_score([25 / 100, 25 / 100, 25 / 100, 25 / 100]), 2.0, places=2
        )
        # No splits
        assert approx_equal(split_score([]), 1.0, places=2)

    def test_AZ_splitting(self) -> None:
        sample: dict = read_json(
            "testdata/splitting/samples/splitting-AZ-benchmark.json"
        )
        CxD: list[list[float]] = sample["countyByDistrict"]

        # County & district totals
        cTActual: list[float] = county_totals(CxD)
        dTActual: list[float] = district_totals(CxD)

        cTExpected: list[float] = [
            71518,
            131346,
            134421,
            53597,
            37220,
            8437,
            20489,
            3817117,
            200186,
            107449,
            980263,
            375770,
            47420,
            211033,
            195751,
        ]
        dTExpected: list[float] = [
            710224,
            710224,
            710224,
            710224,
            710224,
            710224,
            710224,
            710225,
            710224,
        ]

        assert vector_approx_equal(cTActual, cTExpected, places=0)
        assert vector_approx_equal(dTActual, dTExpected, places=0)

        # Reduce county & district splits
        rCActual: list[list[float]] = reduceCSplits(CxD, dTActual)
        rCExpected: list[list[float]] = [
            [0, 0, 0, 0, 0, 0, 0, 3551121, 0, 0, 0, 0, 0, 0, 0],
            [
                71518,
                0,
                134421,
                26230,
                37220,
                8437,
                0,
                2994,
                1635,
                107449,
                92091,
                197708,
                0,
                30521,
                0,
            ],
            [0, 131346, 0, 0, 0, 0, 0, 0, 0, 0, 578878, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 225734, 0, 0, 309294, 545, 47420, 0, 127231],
            [
                0,
                0,
                0,
                27367,
                0,
                0,
                20489,
                37268,
                198551,
                0,
                0,
                177517,
                0,
                180512,
                68520,
            ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        assert matrix_approx_equal(rCActual, rCExpected, places=0)

        # rDActual: list[list[float]] = reduceDSplits(rC, cTActual)

        # TODO - More tests ...


### END ###
