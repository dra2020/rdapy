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
        rCActual: list[list[float]] = reduce_county_splits(CxD, dTExpected)
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

        rDActual: list[list[float]] = reduce_district_splits(CxD, cTExpected)
        rDExpected: list[list[float]] = [
            [
                359045,
                0,
                0,
                0,
                26230,
                0,
                0,
                0,
                2994,
                1635,
                0,
                92091,
                197708,
                0,
                30521,
                0,
            ],
            [131346, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 578878, 0, 0, 0, 0],
            [47420, 0, 0, 0, 0, 0, 0, 0, 225734, 0, 0, 309294, 545, 0, 0, 127231],
            [
                20489,
                0,
                0,
                0,
                27367,
                0,
                0,
                0,
                37268,
                198551,
                0,
                0,
                177517,
                0,
                180512,
                68520,
            ],
            [0, 0, 0, 0, 0, 0, 0, 0, 710224, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 710224, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 710224, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 710225, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 710224, 0, 0, 0, 0, 0, 0, 0],
        ]
        assert matrix_approx_equal(rDActual, rDExpected, places=0)

        # Calculate county & district weights
        wExpected: list[float] = [
            0.011,
            0.021,
            0.021,
            0.008,
            0.006,
            0.001,
            0.003,
            0.597,
            0.031,
            0.017,
            0.153,
            0.059,
            0.007,
            0.033,
            0.031,
        ]
        wActual: list[float] = calc_county_weights(cTExpected)
        assert vector_approx_equal(wActual, wExpected, places=3)

        xExpected: list[float] = [
            0.111,
            0.111,
            0.111,
            0.111,
            0.111,
            0.111,
            0.111,
            0.111,
            0.111,
        ]
        xActual: list[float] = calc_district_weights(dTExpected)
        assert vector_approx_equal(xActual, xExpected, places=3)

        # Calculate county & district fractions
        fExpected: list[list[float]] = [
            [
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.9303,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
            ],
            [
                1.0000,
                0.0000,
                1.0000,
                0.4894,
                1.0000,
                1.0000,
                0.0000,
                0.0008,
                0.0082,
                1.0000,
                0.0939,
                0.5261,
                0.0000,
                0.1446,
                0.0000,
            ],
            [
                0.0000,
                1.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.5905,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
            ],
            [
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0591,
                0.0000,
                0.0000,
                0.3155,
                0.0015,
                1.0000,
                0.0000,
                0.6500,
            ],
            [
                0.0000,
                0.0000,
                0.0000,
                0.5106,
                0.0000,
                0.0000,
                1.0000,
                0.0098,
                0.9918,
                0.0000,
                0.0000,
                0.4724,
                0.0000,
                0.8554,
                0.3500,
            ],
            [
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
            ],
            [
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
            ],
            [
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
            ],
            [
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
            ],
            [
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
                0.0000,
            ],
        ]
        fActual: list[list[float]] = calc_county_fractions(rCExpected, cTExpected)
        assert matrix_approx_equal(fActual, fExpected, places=3)

        gExpected: list[list[float]] = [
            [
                0.5055,
                0,
                0,
                0,
                0.0369,
                0,
                0,
                0,
                0.0042,
                0.0023,
                0,
                0.1297,
                0.2784,
                0,
                0.043,
                0,
            ],
            [0.1849, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.8151, 0, 0, 0, 0],
            [0.0668, 0, 0, 0, 0, 0, 0, 0, 0.3178, 0, 0, 0.4355, 0.0008, 0, 0, 0.1791],
            [
                0.0288,
                0,
                0,
                0,
                0.0385,
                0,
                0,
                0,
                0.0525,
                0.2796,
                0,
                0,
                0.2499,
                0,
                0.2542,
                0.0965,
            ],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        ]
        gActual: list[list[float]] = calc_district_fractions(rDExpected, dTExpected)
        assert matrix_approx_equal(gActual, gExpected, places=3)

        # TODO - More tests ...


### END ###
