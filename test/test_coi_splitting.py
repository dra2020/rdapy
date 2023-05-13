#!/usr/bin/env python3

"""
TEST COI SPLITTING
"""


from rdapy.splitting.coi import *
from testutils import *


class TestCOISplitting:
    def test_paper_examples(self) -> None:
        splits: list[float]

        splits = [0.33, 0.33, 0.34]
        assert approx_equal(uncertainty_of_membership(splits), 1.59, places=1)
        assert approx_equal(effective_splits(splits), 2.0, places=2)

        splits = [0.92, 0.05, 0.03]
        assert approx_equal(uncertainty_of_membership(splits), 0.48, places=1)
        assert approx_equal(effective_splits(splits), 0.18, places=2)


### END ###
