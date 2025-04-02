"""
TEST "MORE" SCORES THAT WE'VE ADDED
"""

from typing import List

from rdapy.score.utils import approx_equal
from rdapy.score.majority_minority import is_single_demo_mmd, is_coalition_mmd
from rdapy.score.partisan import calc_efficiency_gap_wasted_votes


class TestMoreScores:
    def test_eg_wasted_vote(self) -> None:
        d: List[int] = [75, 60, 43, 48, 49]
        r: List[int] = [25, 40, 57, 52, 51]

        actual: float = calc_efficiency_gap_wasted_votes(d, r)
        expected: float = 0.202
        assert approx_equal(actual, expected)

    def test_is_single_demo_mmd(self) -> None:
        assert is_single_demo_mmd(51, 100)
        assert not is_single_demo_mmd(49, 100)

    def test_is_coalition_mmd(self) -> None:
        assert not is_coalition_mmd([20, 10], 100)
        assert not is_coalition_mmd([51, 10], 100)
        assert is_coalition_mmd([30, 25], 100)


### END ###
