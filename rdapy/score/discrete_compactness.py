"""
CUT SCORE AND SPANNING TREE SCORE
based on "Discrete Geometry for Electoral Geography" by Moon Duchin and Bridget Eileen Tenner
"""

from typing import Any, List, Dict, Set

import numpy as np
from scipy.linalg import det
from collections import defaultdict

from ..base import (
    OUT_OF_STATE,
    is_water_only,
    Precinct,
    District,
    Graph,
)


def calc_cut_score(plan: Dict[Precinct, District], graph: Graph) -> int:
    """Given a plan and a graph, return the number of cut edges. Definition 3 in Section 5.4."""

    nodes, edges2x, boundaries, cuts2x = 0, 0, 0, 0

    for node, neighbors in graph.items():
        if node == OUT_OF_STATE:
            continue
        if (
            is_water_only(node)
        ) and node not in plan:  # if (node in OTHER_POTENTIAL_BORDERS) and node not in plan:
            continue

        nodes += 1
        boundary: bool = False

        for neighbor in neighbors:
            if neighbor == OUT_OF_STATE:
                continue
            if (
                is_water_only(neighbor)
            ) and neighbor not in plan:  # if (neighbor in OTHER_POTENTIAL_BORDERS) and neighbor not in plan:
                continue

            edges2x += 1

            if plan[node] != plan[neighbor]:
                cuts2x += 1
                boundary = True

        if boundary:
            boundaries += 1

    cuts = cuts2x // 2

    return cuts


def calc_spanning_tree_score(graph: Graph) -> float:
    """
    Calculate the *log* number of spanning trees in an undirected graph,
    to handle very large graphs.

    See count_spanning_trees() for the simple version that works on small graphs.
    """

    adjacency_matrix, vertices = convert_graph_to_matrix(graph)
    degree_matrix = np.diag(np.sum(adjacency_matrix, axis=1))
    laplacian_matrix = degree_matrix - adjacency_matrix
    reduced_laplacian = laplacian_matrix[:-1, :-1]

    sign, logdet = np.linalg.slogdet(reduced_laplacian)

    if sign <= 0:  # This shouldn't happen for a valid graph
        return float("-inf")

    return logdet


### HELPERS ###


def remove_out_of_state_border(graph: Graph) -> Dict[str, List[str]]:
    """Remove the OUT_OF_STATE node & neighbors from the graph."""

    without_border: Dict[str, List[str]] = {}

    for node, neighbors in graph.items():
        if node != OUT_OF_STATE:
            without_border[node] = [n for n in neighbors if n != OUT_OF_STATE]

    return without_border


def split_graph_by_districts(
    graph: Graph, plan: Dict[Precinct, District]
) -> Dict[int | str, Dict[str, List[str]]]:
    """
    Split a graph into subgraphs based on district assignments.

    Parameters:
    graph: Dictionary where keys are vertices and values are lists of adjacent vertices
    plan: Dictionary mapping vertex names to district numbers

    Returns:
    Dictionary mapping district numbers to their subgraphs
    """
    stripped_graph: Dict[str, List[str]] = remove_out_of_state_border(graph)

    # Validate inputs
    diff = set(stripped_graph.keys()) ^ set(plan.keys())
    # if not set(stripped_graph.keys()) == set(plan.keys()):
    if diff:
        print(f"difference: {diff}")
        raise ValueError(
            "Graph and district assignments must contain the same vertices"
        )

    # Group nodes by district
    district_nodes: Dict[int | str, Set[str]] = defaultdict(set)
    for node, district in plan.items():
        district_nodes[district].add(node)

    # Create subgraph for each district
    district_subgraphs: Dict[int | str, Dict[str, List[str]]] = {}

    for district, nodes in district_nodes.items():
        subgraph = {}
        for node in nodes:
            # Only include neighbors that are in the same district
            neighbors = [n for n in stripped_graph[node] if n in nodes]
            subgraph[node] = neighbors
        district_subgraphs[district] = subgraph

    return district_subgraphs


def convert_graph_to_matrix(graph: Graph) -> tuple[np.ndarray, list[str]]:
    """
    Convert an adjacency list representation to an adjacency matrix.

    Parameters:
    graph: Dictionary where keys are vertices and values are lists of adjacent vertices

    Returns:
    tuple: (adjacency matrix as numpy array, list of vertex names in order)
    """
    # Create a mapping of vertex names to indices
    vertices = sorted(graph.keys())
    vertex_to_index = {vertex: i for i, vertex in enumerate(vertices)}
    n = len(vertices)

    # Create the adjacency matrix
    adjacency_matrix = np.zeros((n, n), dtype=int)
    for vertex, neighbors in graph.items():
        i = vertex_to_index[vertex]
        for neighbor in neighbors:
            j = vertex_to_index[neighbor]
            adjacency_matrix[i, j] = 1
            adjacency_matrix[j, i] = 1  # Make sure the graph is undirected

    return adjacency_matrix, vertices


def validate_graph(graph: Graph) -> bool:
    """
    Verify that a graph is valid: undirected and connected.

    Parameters:
    graph: Dictionary where keys are vertices and values are lists of adjacent vertices

    Returns:
    bool: True if the graph is valid, False otherwise
    """
    # Check if graph is empty
    if not graph:
        return False

    # Check if all edges are bidirectional
    for vertex, neighbors in graph.items():
        for neighbor in neighbors:
            if vertex not in graph[neighbor]:
                return False

    # Check if graph is connected using DFS
    visited = set()
    start_vertex = next(iter(graph))

    def dfs(v):
        visited.add(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start_vertex)

    return len(visited) == len(graph)


### END ###
