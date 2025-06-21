#!/usr/bin/env python3

"""
TEST BIAS METRICS
"""

from math import atan

from rdapy import (
    calc_efficiency_gap,
    approx_equal,
    OUT_OF_STATE_THRESHOLD,
)
from rdapy.partisan.bias import (
    is_sweep,
    radians_to_degrees,
)


class TestBiasMetrics:
    def test_sweeps(self) -> None:
        assert is_sweep(1.0, 10)
        assert is_sweep(10 - (1 / 10) + OUT_OF_STATE_THRESHOLD, 10)
        assert is_sweep(0.0, 10)
        assert is_sweep((1 / 10 - OUT_OF_STATE_THRESHOLD), 10)

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
        assert approx_equal(calc_efficiency_gap(Vf, Sf), EG, places=1)

        # NC 2018
        Vf: float = 0.508
        Sf: float = 3 / 13
        EG: float = 0.277
        assert approx_equal(calc_efficiency_gap(Vf, Sf), EG, places=1)


### END ###
