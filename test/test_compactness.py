#!/usr/bin/env python3

"""
TEST COMPACTNESS
"""

from rdapy.compactness import *
from testutils import *
from pytest import approx


INDEX: int = 0
VALUE: int = 1


class TestCompactness:
    def test_NC_116th(self) -> None:
        """Replicate Jowei Chen's compactness for NC 116th Congressional Districts."""

        shapes_path = "testdata/compactness/NC-116th-Congressional"
        shapes, _ = load_shapes(shapes_path, id="id")

        scorecard_path = "testdata/compactness/NC-116th-Congressional/expected.json"
        scorecard = read_json(scorecard_path)

        assert True  # TODO


### END ###
