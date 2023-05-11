#!/usr/bin/env python3

"""
TEST BIAS METRICS
"""


from rdapy.partisan import *
from testutils import *


class TestPopulationDeviation:
    def test_sweeps(self) -> None:
        assert is_sweep(1.0, 10)
        assert is_sweep(10 - (1 / 10) + EPSILON, 10)
        assert is_sweep(0.0, 10)
        assert is_sweep((1 / 10 - EPSILON), 10)

    def test_radians_to_degrees(self) -> None:
        assert radians_to_degrees(atan(1)) == 45

    def test_efficiency_gap(self) -> None:
        """Making sure the signs are right vs. precise results

        Source: https://planscore.org/north_carolina/#!2012-plan-ushouse-eg
        """

        # NC 2016
        Vf: float = 0.467
        Sf: float = 3 / 13
        EG: float = 0.194
        assert approx_equal(efficiency_gap(Vf, Sf), EG, places=1)

        # NC 2018
        Vf: float = 0.508
        Sf: float = 3 / 13
        EG: float = 0.277
        assert approx_equal(efficiency_gap(Vf, Sf), EG, places=1)

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
