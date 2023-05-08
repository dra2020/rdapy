#!/usr/bin/env python3

"""
TEST COMPACTNESS
"""

from rdapy.compactness import *
from testutils import *


INDEX: int = 0
VALUE: int = 1


class TestCompactness:
    def test_NC_116th(self) -> None:
        """Replicate Jowei Chen's compactness for NC 116th Congressional Districts."""

        shapes_path = "testdata/compactness/NC-116th-Congressional"
        shapes, _ = load_shapes(shapes_path, id="id")
        shapes = [item[VALUE] for item in shapes]  # discard the id

        expected_path = "testdata/compactness/NC-116th-Congressional/expected.json"
        expected = read_json(expected_path)

        actual: dict = calc_compactness(shapes)

        assert approx_equal(actual["avgReock"], expected["avgReock"], abs=0.005)
        assert approx_equal(actual["avgPolsby"], expected["avgPolsby"], abs=0.005)
        assert approx_equal(actual["avgKIWYSI"], expected["avgKIWYSI"], abs=0.005)

        for i in range(len(actual["byDistrict"])):
            assert approx_equal(
                actual["byDistrict"][i]["reock"],
                expected["byDistrict"][i]["reock"],
                abs=0.005,
            )
            assert approx_equal(
                actual["byDistrict"][i]["polsby"],
                expected["byDistrict"][i]["polsby"],
                abs=0.005,
            )
            assert approx_equal(
                round(actual["byDistrict"][i]["kiwysiRank"]),
                round(expected["byDistrict"][i]["kiwysiRank"]),
                abs=0.005,
            )


### END ###
