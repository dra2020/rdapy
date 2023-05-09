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


### END ###
