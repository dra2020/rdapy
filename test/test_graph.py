#!/usr/bin/env python3

"""
TEST GRAPH FUNCTIONS
"""


from rdapy.graph import *
from testutils import *


def check_embeddedness(plan_path: str, graph_path: str) -> bool:
    """Test helper for is_embedded()"""

    plan_rows = read_csv(plan_path, [str, int])
    graph = read_json(graph_path)

    plan: dict[str, int | str] = {row["GEOID"]: row["DISTRICT"] for row in plan_rows}
    inverted_plan: defaultdict[int | str, set[str]] = defaultdict(set)
    for k, v in plan.items():
        inverted_plan[v].add(k)

    for id, features in inverted_plan.items():
        embedded: bool = is_embedded(id, plan, inverted_plan, graph)

        if embedded:
            return False

    return True


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
        plan_path = "testdata/graph/SAMPLE-BG-map.csv"
        graph_path = "testdata/graph/SAMPLE-BG-graph.json"
        assert check_embeddedness(plan_path, graph_path)


### END ###
