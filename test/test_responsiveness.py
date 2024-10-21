#!/usr/bin/env python3

"""
TEST COMPETITIVENESS & RESPONSIVENESS METRICS
"""


from rdapy.partisan import *
from testutils import *


class TestResponsivenessMetrics:
    def test_count_competitive_districts(self) -> None:
        # 3 of 7 competitive
        Vf_array: list[float] = [
            0.40,
            0.45 - EPSILON,
            0.45,
            0.50,
            0.55,
            0.55 + EPSILON,
            0.60,
        ]
        assert count_competitive_districts(Vf_array) == 3

    def test_district_competitiveness_UNCOMPRESSED(self) -> None:
        # 40.1515% share
        assert approx_equal(est_district_competitiveness(0.401515), 0.027433)

        # 45.0000% share
        assert approx_equal(est_district_competitiveness(0.450000), 0.377952)

        # 50.1515% share
        assert approx_equal(est_district_competitiveness(0.501515), 0.999087)

        # 55.0000% share
        assert approx_equal(est_district_competitiveness(0.550000), 0.377952)

        # 60.1515% share
        assert approx_equal(est_district_competitiveness(0.601515), 0.022181)

    def test_MIR(self) -> None:
        actual: Optional[float]

        # "CA"
        actual = calc_minimal_inverse_responsiveness(0.592091, 2.1)
        assert actual is not None
        assert approx_equal(actual, 0.2762, places=4)

        # "MA"
        actual = calc_minimal_inverse_responsiveness(0.600269, 1.9)
        assert actual is not None
        assert approx_equal(actual, 0.3263, places=4)

        # "IL"
        actual = calc_minimal_inverse_responsiveness(0.600068, 3.1)
        assert actual is not None
        assert approx_equal(actual, 0.1226, places=4)

        # "MD"
        actual = calc_minimal_inverse_responsiveness(0.593369, 1.0)
        assert actual is not None
        assert approx_equal(actual, 0.8000, places=4)

        # "CO"
        actual = calc_minimal_inverse_responsiveness(0.505561, 3.9)
        assert actual is not None
        assert approx_equal(actual, 0.1564, places=4)

        # "PA"
        actual = calc_minimal_inverse_responsiveness(0.529422, 4.1)
        assert actual is not None
        assert approx_equal(actual, 0.1439, places=4)

        # "NC"
        actual = calc_minimal_inverse_responsiveness(0.515036, 4.0)
        assert actual is not None
        assert approx_equal(actual, 0.1500, places=4)

        # "OH"
        actual = calc_minimal_inverse_responsiveness(0.513062, 4.5)
        assert actual is not None
        assert approx_equal(actual, 0.1222, places=4)

        # "SC"
        actual = calc_minimal_inverse_responsiveness(0.430028, 0.9)
        assert actual is not None
        assert approx_equal(actual, 0.9111, places=4)

        # "TN"
        actual = calc_minimal_inverse_responsiveness(0.415935, 0.8)
        assert actual is not None
        assert approx_equal(actual, 1.0500, places=4)

        # "TX"
        actual = calc_minimal_inverse_responsiveness(0.404324, 1.1)
        assert actual is not None
        assert approx_equal(actual, 0.7091, places=4)


### END ###
