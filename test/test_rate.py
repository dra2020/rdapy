#!/usr/bin/env python3

"""
TEST NORMALIZATION & RATINGS
"""

import random

from rdapy.rate import *
from testutils import *


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
    def test_foo(self) -> None:
        assert True


### END ###
