#!/usr/bin/env python3

"""
TEST MINORITY OPPORTUNITY
"""


from rdapy.minority import *
from testutils import *

EPSILON: float = 1 / 10**6


class TestMinority:
    def test_calc_proportional_districts(self) -> None:
        n_districts = 10

        # Zero
        assert calc_proportional_districts(0.0, n_districts) == 0

        # Not quite one
        assert (
            calc_proportional_districts((1 / n_districts) - 0.05 - EPSILON, n_districts)
            == 0
        )

        # One
        assert calc_proportional_districts(1 / n_districts, n_districts) == 1

        # Not quite two
        assert (
            calc_proportional_districts(
                (2 * (1 / n_districts)) - 0.05 - EPSILON, n_districts
            )
            == 1
        )

        # Two
        assert calc_proportional_districts(2 * (1 / n_districts), n_districts) == 2

    def test_est_minority_opportunity(self) -> None:
        # 35%
        assert approx_equal(est_minority_opportunity(0.3500), 0.0)
        # 37%
        assert approx_equal(est_minority_opportunity(0.3700), 0.6914624612740132)
        # 38%
        assert approx_equal(est_minority_opportunity(0.3800), 0.773372647623132)
        # 49%
        assert approx_equal(est_minority_opportunity(0.4900), 0.9997673709209645)
        # 50%
        assert approx_equal(est_minority_opportunity(0.5000), 0.9999115827147992)
        # 51%
        assert approx_equal(est_minority_opportunity(0.5100), 0.9999683287581669)
        # 90%
        assert approx_equal(est_minority_opportunity(0.9000), 1.0)


### END ###
