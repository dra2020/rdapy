#!/usr/bin/env python3

"""
DEBUG
"""

from rdapy.graph import *
from testutils import *

from collections import defaultdict

plan_path = "testdata/graph/SAMPLE-BG-map.csv"
graph_path = "testdata/graph/SAMPLE-BG-graph.json"


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


assert check_embeddedness(plan_path, graph_path)

pass

### END ###
