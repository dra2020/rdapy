#!/usr/bin/env python3

"""
TEST COMPACTNESS
"""

from rdapy import load_shapes, read_json, approx_equal, calc_compactness_matrics


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

        actual: dict = calc_compactness_matrics(shapes)

        assert approx_equal(actual["avgReock"], expected["avgReock"], places=2)
        assert approx_equal(actual["avgPolsby"], expected["avgPolsby"], places=2)
        assert approx_equal(actual["avgKIWYSI"], expected["avgKIWYSI"], places=2)

        for i in range(len(actual["byDistrict"])):
            assert approx_equal(
                actual["byDistrict"][i]["reock"],
                expected["byDistrict"][i]["reock"],
                places=2,
            )
            assert approx_equal(
                actual["byDistrict"][i]["polsby"],
                expected["byDistrict"][i]["polsby"],
                places=2,
            )
            assert approx_equal(
                round(actual["byDistrict"][i]["kiwysiRank"]),
                round(expected["byDistrict"][i]["kiwysiRank"]),
                places=2,
            )


### END ###
