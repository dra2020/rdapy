#!/usr/bin/env python3

"""
TEST NORMALIZATION & RATINGS
"""

import random

from rdapy.rate import *
from testutils import *

EPSILON: float = 1 / 10**6


class TestNormalizer:
    """Test Normalizer class"""

    def test_identity(self) -> None:
        x: float = random.random()
        n: Normalizer = Normalizer(x)
        n.identity()
        assert approx_equal(n.wip_num, x)

    def test_invert(self) -> None:
        n: Normalizer = Normalizer(0.75 / 100)
        n.invert()
        assert approx_equal(n.wip_num, 0.9925)

        n: Normalizer = Normalizer(0.0)
        n.invert()
        assert approx_equal(n.wip_num, 1.0)

        n: Normalizer = Normalizer(1.0)
        n.invert()
        assert approx_equal(n.wip_num, 0.0)

    def test_clip(self) -> None:
        n: Normalizer = Normalizer(0.3773)
        n.clip(0.25, 0.50)
        assert approx_equal(n.wip_num, 0.3773)

        n: Normalizer = Normalizer(0.2)
        n.clip(0.25, 0.50)
        assert approx_equal(n.wip_num, 0.25)

        n: Normalizer = Normalizer(0.55)
        n.clip(0.25, 0.50)
        assert approx_equal(n.wip_num, 0.5)

        n: Normalizer = Normalizer(0.25)
        n.clip(0.25, 0.50)
        assert approx_equal(n.wip_num, 0.25)

        n: Normalizer = Normalizer(0.5)
        n.clip(0.25, 0.50)
        assert approx_equal(n.wip_num, 0.5)

    def test_rebase(self) -> None:
        n: Normalizer = Normalizer(1.0)
        n.rebase(1.0)
        assert approx_equal(n.wip_num, 0.0)

        n: Normalizer = Normalizer(1.5)
        n.rebase(1.0)
        assert approx_equal(n.wip_num, 0.5)

        n: Normalizer = Normalizer(0.5)
        n.rebase(1.0)
        assert approx_equal(n.wip_num, -0.5)

        n: Normalizer = Normalizer(-2.0)
        n.rebase(1.0)
        assert approx_equal(n.wip_num, -3.0)

    def test_unitize(self) -> None:
        n: Normalizer = Normalizer(1.5)
        n.unitize(1.0, 2.0)
        assert approx_equal(n.wip_num, 0.5)

        n: Normalizer = Normalizer(1.0)
        n.unitize(1.0, 2.0)
        assert approx_equal(n.wip_num, 0.0)

        n: Normalizer = Normalizer(2.0)
        n.unitize(1.0, 2.0)
        assert approx_equal(n.wip_num, 1.0)

    def test_decay(self) -> None:
        n: Normalizer = Normalizer(0.90)
        n.decay()
        assert approx_equal(n.wip_num, 0.81)

        n: Normalizer = Normalizer(0.00)
        n.decay()
        assert approx_equal(n.wip_num, 0.0)

        n: Normalizer = Normalizer(1.00)
        n.decay()
        assert approx_equal(n.wip_num, 1.00)

    def test_rescale(self) -> None:
        n: Normalizer = Normalizer(0.63)
        n.rescale()
        assert n.normalized_num == 63

        n: Normalizer = Normalizer(0.6372)
        n.rescale()
        assert n.normalized_num == 64

        n: Normalizer = Normalizer(0.6312)
        n.rescale()
        assert n.normalized_num == 63

        n: Normalizer = Normalizer(0.0)
        n.rescale()
        assert n.normalized_num == 0

        n: Normalizer = Normalizer(1.0)
        n.rescale()
        assert n.normalized_num == 100


class TestRatings:
    def test_is_antimajoritarian(self) -> None:
        # Dem antimajoritarian
        assert is_antimajoritarian(0.5 - AVG_SV_ERROR - EPSILON, 0.50 + EPSILON)

        # Rep antimajoritarian
        assert is_antimajoritarian(0.5 + AVG_SV_ERROR + EPSILON, 0.5 - EPSILON)

        # Majority but not antimajoritarian
        assert not is_antimajoritarian(0.51, 0.53)

        # Minority but not antimajoritarian
        assert not is_antimajoritarian(0.49, 0.47)

        # Not big enough to be called antimajoritarian
        assert not is_antimajoritarian(0.5 - EPSILON, 0.5 - EPSILON)

    def test_extra_bonus(self) -> None:
        assert approx_equal(extra_bonus(0.50), 0.0)
        assert approx_equal(extra_bonus(0.55), 0.10 / 2)
        assert approx_equal(extra_bonus(0.60), 0.20 / 2)
        assert approx_equal(extra_bonus(0.45), 0.10 / 2)
        assert approx_equal(extra_bonus(0.40), 0.20 / 2)

    def test_adjust_deviation(self) -> None:
        # CA
        Vf: float = 0.64037
        bias: float = -0.1714
        extra: float = extra_bonus(Vf)
        assert approx_equal(extra, 0.1404, 4)
        assert approx_equal(adjust_deviation(Vf, bias, extra), -0.0310, 4)

        # NC
        Vf: float = 0.488799
        bias: float = 0.2268
        extra = extra_bonus(Vf)
        assert approx_equal(extra, 0.0112, 4)
        assert approx_equal(adjust_deviation(Vf, bias, extra), 0.2156, 4)

        # OH
        Vf: float = 0.486929
        bias: float = 0.2367
        extra = extra_bonus(Vf)
        assert approx_equal(extra, 0.0131, 4)
        assert approx_equal(adjust_deviation(Vf, bias, extra), 0.2236, 4)

        # PA
        Vf: float = 0.51148
        bias: float = 0.0397
        extra = extra_bonus(Vf)
        assert approx_equal(extra, 0.0115, 4)
        assert approx_equal(adjust_deviation(Vf, bias, extra), bias, 4)

        # TX
        Vf: float = 0.436994
        bias: float = 0.1216
        extra = extra_bonus(Vf)
        assert approx_equal(extra, 0.0630, 4)
        assert approx_equal(adjust_deviation(Vf, bias, extra), 0.0586, 4)

    def test_rate_proportionality(self) -> None:
        # Score proportionality, no winner bonus

        Vf = 0.5
        Sf = 0.5

        assert rate_proportionality(0.00, Vf, Sf) == 100  # Completely unbiased
        assert rate_proportionality(0.05, Vf, Sf) == 75  # 5% biased
        assert rate_proportionality(0.10, Vf, Sf) == 50  # 10% biased
        assert rate_proportionality(0.20, Vf, Sf) == 0  # 20% biased
        assert rate_proportionality(0.25, Vf, Sf) == 0  # 25% biased
        assert (
            rate_proportionality(0.01, 0.48 - EPSILON, 0.5 + EPSILON) == 0
        )  # Dem antimajoritarian
        assert (
            rate_proportionality(0.01, 1 - 0.48 + EPSILON, 1 - 0.5 - EPSILON) == 0
        )  # Rep antimajoritarian

        # Score proportionality, with winner bonus

        assert rate_proportionality(-0.1714, 0.6404, 43.0850 / 53) == 84  # CA 116th
        assert rate_proportionality(0.0006, 0.5286, 3.9959 / 7) == 100  # CO 116th
        assert rate_proportionality(-0.0585, 0.5838, 12.0531 / 18) == 100  # IL 116th
        assert rate_proportionality(-0.3331, 0.6321, 8.9985 / 9) == 0  # MA 116th
        assert rate_proportionality(-0.2500, 0.6336, 7.0000 / 8) == 42  # MD 116th
        assert rate_proportionality(0.2268, 0.4888, 3.0512 / 13) == 0  # NC 116th
        assert rate_proportionality(0.2367, 0.4869, 4.2120 / 16) == 0  # OH 116th
        assert rate_proportionality(0.2857, 0.4072, 1 / 7) == 4  # SC 116th
        assert rate_proportionality(0.1111, 0.3802, 2 / 9) == 100  # TN 116th
        assert rate_proportionality(0.1216, 0.4370, 11.6218 / 36) == 71  # TX 116th

    def test_rate_competitiveness(self) -> None:
        # Completely uncompetitive
        assert rate_competitiveness(0.00) == 0
        # 25% / 50% competitive
        assert rate_competitiveness(0.25) == 33
        # 50% / 50% competitive
        assert rate_competitiveness(0.50) == 67
        # Perfectly competitive
        assert rate_competitiveness(0.75) == 100
        # Over competitive
        assert rate_competitiveness(0.80) == 100

    def test_rate_minority_representation(self) -> None:
        bonus: int = 100

        # No possibilities
        assert rate_minority_representation(1, 0, 0, 0) == 0

        # No opportunities
        assert rate_minority_representation(0, 10, 0, 0) == 0

        # Half
        assert rate_minority_representation(5, 10, 0, 0) == round(bonus / 2)

        # All
        assert rate_minority_representation(10, 10, 0, 0) == bonus

        # Extra
        assert rate_minority_representation(11, 10, 0, 0) == bonus

        # Combined score

        # * Opportunity districts = (12.56 / 18) * 100 <<< 70
        # * Coalition districts = (22.92 / 18) * 100 <<< capped
        # * Combined = 70 + [0.5 * (100 - 70)]
        correct: int = 85
        assert rate_minority_representation(12.56, 18, 22.92, 18) == correct

    def test_rate_compactness(self) -> None:
        assert rate_compactness(30, 60) == 45

        # Reock compactness scorer
        # Reock: in range (AL)
        assert rate_reock(0.3848) == 54

        # Reock: in range (NC)
        assert rate_reock(0.3373) == 35

        # Reock: min
        assert rate_reock(REOCK_MIN) == 0

        # Reock: max
        assert rate_reock(REOCK_MAX) == 100

        # Reock: too low
        assert rate_reock(REOCK_MIN - EPSILON) == 0

        # Reock: too high
        assert rate_reock(REOCK_MAX + EPSILON) == 100

        # Polsby-Popper compactness scorer

        # Polsby-Popper: in range (AL)
        assert rate_polsby(0.1860) == 21

        # Polsby-Popper: in range (NC)
        assert rate_polsby(0.2418) == 35

        # Polsby-Popper: min
        assert rate_polsby(POLSBY_MIN) == 0

        # Polsby-Popper: max
        assert rate_polsby(POLSBY_MAX) == 100

        # Polsby-Popper: too low
        assert rate_polsby(POLSBY_MIN - EPSILON) == 0

        # Polsby-Popper: too high
        assert rate_polsby(POLSBY_MAX + EPSILON) == 100


### END ###
