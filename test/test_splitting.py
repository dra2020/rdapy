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

    def test_lefthand_example(self) -> None:
        """Lefthand examples from P. 2 of Moon Duchin's Appendix"""

        CxD: list[list[float]] = [
            [40, 40, 20, 0, 0, 0, 0],
            [0, 0, 20, 80, 0, 0, 0],
            [0, 0, 0, 0, 88, 12, 0],
            [0, 0, 0, 0, 0, 20, 80],
        ]
        counties: list[float] = [40, 40, 40, 80, 88, 32, 80]

        fExpected: list[list[float]] = [
            [1.0, 1.0, 0.5, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 1.0, 0.375, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.625, 1.0],
        ]
        wExpected: list[float] = [0.1, 0.1, 0.1, 0.2, 0.22, 0.08, 0.2]

        districts: list[float] = [100, 100, 100, 100]

        gExpected: list[list[float]] = [
            [0.4, 0.4, 0.2, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.2, 0.8, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.88, 0.12, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.8],
        ]
        xExpected = [0.25, 0.25, 0.25, 0.25]

        # County splitting

        fActual: list[list[float]] = calc_county_fractions(CxD, counties)
        wActual: list[float] = calc_county_weights(counties)

        assert matrix_approx_equal(fActual, fExpected, places=3)
        assert vector_approx_equal(wActual, wExpected, places=3)

        assert approx_equal(county_split_score(0, fExpected), 1.0, places=3)
        assert approx_equal(county_split_score(1, fExpected), 1.0, places=3)
        assert approx_equal(county_split_score(2, fExpected), 1.4142, places=3)
        assert approx_equal(county_split_score(3, fExpected), 1.0, places=3)
        assert approx_equal(county_split_score(4, fExpected), 1.0, places=3)
        assert approx_equal(county_split_score(5, fExpected), 1.4029, places=3)
        assert approx_equal(county_split_score(6, fExpected), 1.0, places=3)

        assert approx_equal(county_splitting(fActual, wActual), 1.0737, places=3)
        # TODO - One more

        # District splitting

        gActual: list[list[float]] = calc_district_fractions(CxD, districts)
        xActual: list[float] = calc_district_weights(districts)

        assert matrix_approx_equal(gActual, gExpected, places=3)
        assert vector_approx_equal(xActual, xExpected, places=3)

        assert approx_equal(district_split_score(0, gExpected), 1.7121, places=3)
        assert approx_equal(district_split_score(1, gExpected), 1.3416, places=3)
        assert approx_equal(district_split_score(2, gExpected), 1.2845, places=3)
        assert approx_equal(district_split_score(3, gExpected), 1.3416, places=3)

        assert approx_equal(district_splitting(gActual, xActual), 1.4200, places=3)
        # TODO - One more

    def test_rightthand_example(self) -> None:
        """Righthand examples from P. 2 of Moon Duchin's Appendix"""

        assert True  # TODO

    def test_reduce_splits(self) -> None:
        """Reduce splits test cases"""

        assert True  # TODO

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

        # Calculate county & district splitting scores
        cActual: float = calc_county_splitting_reduced(CxD, dTExpected, cTExpected)
        assert approx_equal(cActual, 1.3523, places=4)

        dActual: float = calc_district_splitting_reduced(CxD, dTExpected, cTExpected)
        assert approx_equal(dActual, 1.4240, places=4)


### END ###
