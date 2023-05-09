#!/usr/bin/env python3

"""
TEST GRAPH FUNCTIONS
"""


from rdapy.graph import *
from testutils import *


class TestGraph:
    def test_is_connected(self) -> None:
        geos: list[str] = ["a", "b", "c"]
        adjacency: dict[str, list[str]] = {
            "a": ["b", "c"],
            "b": ["a", "c"],
            "c": ["a", "b"],
        }
        assert is_connected(geos, adjacency)

        geos: list[str] = ["a", "b", "c", "d", "e", "f"]
        adjacency: dict[str, list[str]] = {
            "a": ["b", "c"],
            "b": ["a", "c"],
            "c": ["a", "b"],
            "d": ["e", "f"],
            "e": ["d", "f"],
            "f": ["d", "e"],
        }
        assert not is_connected(geos, adjacency)

        geos: list[str] = ["a", "b", "c"]
        adjacency: dict[str, list[str]] = {
            "a": ["b", "c"],
            "b": ["a", "c"],
            "c": ["a", "b"],
        }
        assert is_connected(geos, adjacency)

    def test_is_embedded(self) -> None:
        assert True  # TODO


### END ###
