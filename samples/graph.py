#!/usr/bin/env python3

"""
Sample graph analysis
"""

from collections import defaultdict

from rdapy import *
from testutils import *

# Helpers


def check_contiguity(plan_path: str, graph_path: str) -> bool:
    """Test helper for is_connected()"""

    plan_rows = read_csv(plan_path, [str, int])
    graph = read_json(graph_path)

    plan: dict[str, int | str] = {row["GEOID"]: row["DISTRICT"] for row in plan_rows}
    inverted_plan: defaultdict[int | str, set[str]] = defaultdict(set)
    for k, v in plan.items():
        inverted_plan[v].add(k)

    for id, geos in inverted_plan.items():
        connected: bool = is_connected(list(geos), graph)

        if not connected:
            return False

    return True


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


# Load data

sample_plan_path = "testdata/graph/SAMPLE-BG-map.csv"
sample_graph_path = "testdata/graph/SAMPLE-BG-graph.json"

#

sample_contiguity: bool = check_contiguity(sample_plan_path, sample_graph_path)
sample_embeddedness: bool = check_embeddedness(sample_plan_path, sample_graph_path)

#

# Print the results

print(f"Graph analysis:")
print(f"- Contiguity: {sample_contiguity}")
print(f"- Embeddedness: {sample_embeddedness}")

### END ###
