"""
TEST "MORE" SCORES THAT WE'VE ADDED
"""

from typing import List

from rdapy import approx_equal, calc_efficiency_gap_wasted_votes, calc_gallagher_index
from rdapy.minority.majority_minority import _is_single_demo_mmd, _is_coalition_mmd


class TestMoreScores:
    def test_eg_wasted_vote(self) -> None:
        d: List[int] = [75, 60, 43, 48, 49]
        r: List[int] = [25, 40, 57, 52, 51]

        actual: float = calc_efficiency_gap_wasted_votes(d, r)
        expected: float = 0.202
        assert approx_equal(actual, expected)

    def test_is_single_demo_mmd(self) -> None:
        assert _is_single_demo_mmd(51, 100)
        assert not _is_single_demo_mmd(49, 100)

    def test_is_coalition_mmd(self) -> None:
        assert not _is_coalition_mmd([20, 10], 100)
        assert not _is_coalition_mmd([51, 10], 100)
        assert _is_coalition_mmd([30, 25], 100)

    def test_gallagher_index(self) -> None:
        """
        Canada's 2015 federal election, which had a Gallagher index of 0.1202.
        https://en.wikipedia.org/wiki/Gallagher_index
        """
        Vf: List[float] = [0.3947, 0.3189, 0.1971, 0.0466, 0.0345, 0.0082]
        Sf: List[float] = [0.5444, 0.2929, 0.1302, 0.0296, 0.0029, 0.0000]

        actual: float = calc_gallagher_index(Vf, Sf)
        expected: float = 0.1202
        assert approx_equal(actual, expected, places=4)


### END ###
