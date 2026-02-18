"""
BOTTLENECK DETECTION

A bottleneck is a chain of degree-2 nodes connecting or "bridging"
between two clusters of geographies (precincts, blocks) and
resembling a dumbbell or hourglass structure.
"""

from typing import List, Dict, Any
from collections import defaultdict, deque

from .connected import is_connected

# Minimum size for a component to be considered a "cluster"
MIN_CLUSTER_SIZE = 2


def not_bottlenecked(ids: List[Any], graph: Dict[str, List[str]]) -> bool:
    """
    Returns True if the geographies are NOT bottlenecked (or are not connected).
    Returns False if they ARE connected AND a bottleneck exists.
    
    A bottleneck is defined as a chain of one or more degree-2 nodes whose removal
    would disconnect the subgraph into two clusters (each with 2+ nodes).
    
    Args:
        ids: List of geographic unit identifiers (e.g., precinct or block IDs)
        graph: Adjacency list representing geographic neighbors. Nodes in ids that
               are not present in graph or have no neighbors are treated as isolated
               (degree 0) and handled gracefully.
        
    Returns:
        True if no bottleneck exists or if the subgraph is disconnected
        False if a bottleneck exists in a connected subgraph
        
    Algorithm:
        1. Check the trivial cases (empty or single-node -> no bottleneck)
        2. Check connectivity (not connected -> return True)
        3. Build induced subgraph and classify nodes by degree
        4. Contract all degree-2 chains into single skeleton edges
        5. Use Tarjan's bridge algorithm to find bridges in skeleton
        6. For each chain bridge, check if both components have 2+ nodes
        7. Return False only if a chain bridge separates two true clusters
    """

    # Handle default case of empty ids or single node (trivially not bottlenecked)
    if len(ids) <= 1:
        return True
    
    # Not connected -> not bottlenecked per specification
    if not is_connected(ids, graph):
        return True

    # Build induced subgraph restricted to ids
    id_set = set(ids)
    induced: Dict[Any, List[Any]] = {
        node: [nb for nb in graph.get(node, []) if nb in id_set]
        for node in ids
    }
    degree = {node: len(nbs) for node, nbs in induced.items()}

    # Junction nodes (degree != 2) anchor the skeleton graph
    junction = {n for n, d in degree.items() if d != 2}

    # Pure cycle (all degree 2) -> no bottleneck possible
    if not junction:
        return True

    # ------------------------------------------------------------------
    # Build skeleton graph: contract degree-2 chains into single edges.
    # Each edge gets a unique ID to handle parallel edges correctly.
    # ------------------------------------------------------------------
    skel_adj: Dict[Any, List[tuple]] = defaultdict(list)  # node -> [(neighbor, edge_id)]
    edge_is_chain: Dict[int, bool] = {}
    eid = 0

    visited_direct: set = set()   # Track direct junction-junction edges
    visited_chain: set = set()    # Track degree-2 nodes already in a chain

    for u in junction:
        for v in induced[u]:
            if v in junction:
                # Direct junction-to-junction edge (no degree-2 nodes between)
                key = frozenset((u, v))
                if key not in visited_direct:
                    visited_direct.add(key)
                    skel_adj[u].append((v, eid))
                    skel_adj[v].append((u, eid))
                    edge_is_chain[eid] = False
                    eid += 1
            elif v not in visited_chain:
                # Traverse and contract the degree-2 chain starting at v
                prev, curr = u, v
                chain_nodes: List[Any] = []
                while curr not in junction:
                    chain_nodes.append(curr)
                    a, b = induced[curr]
                    nxt = b if a == prev else a
                    prev, curr = curr, nxt
                w = curr  # Junction node at far end of chain
                visited_chain.update(chain_nodes)
                skel_adj[u].append((w, eid))
                skel_adj[w].append((u, eid))
                edge_is_chain[eid] = True
                eid += 1

    # ------------------------------------------------------------------
    # Tarjan's bridge-finding algorithm on the skeleton graph.
    # Uses edge IDs (not parent nodes) to correctly handle parallel edges.
    # ------------------------------------------------------------------
    disc: Dict[Any, int] = {}
    low: Dict[Any, int] = {}
    timer = [0]
    chain_bridges: List[tuple] = []  # Store (u, v) pairs for chain bridges

    def dfs(u: Any, parent_eid: int) -> None:
        disc[u] = low[u] = timer[0]
        timer[0] += 1
        for v, e in skel_adj[u]:
            if e == parent_eid:
                # Skip the exact tree edge we arrived on
                continue
            if v in disc:
                # Back edge -> update low-link
                low[u] = min(low[u], disc[v])
            else:
                # Tree edge -> recurse
                dfs(v, e)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u] and edge_is_chain[e]:
                    # Bridge AND it's a degree-2 chain -> candidate bottleneck
                    chain_bridges.append((u, v))

    dfs(next(iter(junction)), -1)

    # Helper function to count component size
    def count_component_size(start: Any, graph: Dict[Any, List[Any]]) -> int:
        """Count nodes reachable from start in the given graph."""
        visited = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    stack.append(neighbor)
        return len(visited)

    # Check each chain bridge to see if it's a true bottleneck
    # A pendant arm (single node on one side) is NOT a bottleneck
    for u, v in chain_bridges:
        # Find the actual degree-2 chain nodes between u and v in the original graph
        # We need to remove these from the induced graph to count components
        chain_to_remove = set()
        
        # BFS from u to v in induced graph, collecting degree-2 nodes
        visited = {u}
        queue = deque([u])
        parent = {u: None}
        
        while queue:
            node = queue.popleft()
            if node == v:
                break
            for neighbor in induced[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = node
                    queue.append(neighbor)
        
        # Check if path was found (defensive check)
        if v not in parent:
            # This shouldn't happen if skeleton is correct, but handle gracefully
            continue
        
        # Reconstruct path from u to v
        path = []
        curr = v
        while curr != u:
            path.append(curr)
            curr = parent[curr]
        path.append(u)
        path.reverse()
        
        # The chain nodes are the interior degree-2 nodes in the path
        for node in path[1:-1]:  # Exclude endpoints u and v
            if degree[node] == 2:
                chain_to_remove.add(node)
        
        # Count component sizes in original induced graph with chain removed
        # Build temporary graph without chain nodes
        temp_graph = {
            node: [nb for nb in neighbors if nb not in chain_to_remove]
            for node, neighbors in induced.items()
            if node not in chain_to_remove
        }
        
        size_u = count_component_size(u, temp_graph)
        size_v = count_component_size(v, temp_graph)
        
        # Bottleneck ONLY if both components are clusters (2+ nodes)
        if size_u >= MIN_CLUSTER_SIZE and size_v >= MIN_CLUSTER_SIZE:
            return False  # Found a genuine bottleneck

    return True  # No genuine bottlenecks found

### END ###