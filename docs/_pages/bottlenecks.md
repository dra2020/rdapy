# Bottleneck Detection in Electoral Districts

"Bridging" is a technique used in drawing redistricting maps that connects disparate geographic areas through narrow corridors.
It can be used in real-world maps, but such egregious district engineering would typically not pass muster, e.g., wrto compactness.
More commonly, however, it is used in maps in DRA to game the Notable Maps selection criteria which don't exclude such maps.

These bridges form bottlenecks in the district, and being able to detect bottlenecks would allow us to exclude such maps from
consideration as Notable Maps.

## Definition

A bottleneck exists when:
1. The district is **connected** (all units form a single contiguous region); and
2. There exists a **chain** of one or more geographic units where:
   - Each interior unit in the chain has **exactly degree 2** (connected to exactly two neighbors)
   - The chain's endpoints connect to separate **clusters** of units (each cluster has 2 or more units)
   - Removing the chain would **disconnect** the district into two components

This resembles a dumbbell or hourglass shape.

Note: A pendant arm (chain leading to a single isolated unit) or a linear chain connecting two isolated units are NOT bottlenecks, since bottlenecks require substantial clusters (2+ nodes) on both sides.

## The Algorithm

The detection algorithm uses graph theory to efficiently identify bottlenecks in O(V+E) time:

### High-Level Approach

1. **Check connectivity**: If the district isn't connected, return `True` (not bottlenecked)
2. **Build skeleton graph**: Contract all degree-2 chains into single edges
3. **Find bridges**: Use Tarjan's algorithm to find critical edges in the skeleton
4. **Identify bottlenecks**: Return `False` only if a bridge corresponds to a degree-2 chain

### Key Insight

A bottleneck in the original graph corresponds to a **bridge** (edge whose removal disconnects the graph) in a simplified "skeleton" graph where all degree-2 chains have been contracted to single edges.

However, not all bridges are bottlenecks—only those that represent degree-2 chains. A direct edge between two high-degree junction nodes is a structural bridge but not a bottleneck by our definition.

### Detailed Steps

#### Step 1: Classify Nodes

Partition nodes into two categories:
- **Junction nodes**: degree ≠ 2 (anchor points for the skeleton)
- **Chain interior nodes**: degree = 2 (will be contracted)

Special case: If all nodes have degree 2 (pure cycle), no bottleneck is possible.

#### Step 2: Build Skeleton Graph

For each junction node:
- **Direct edges**: If connected to another junction directly, add to skeleton (not a chain)
- **Chain edges**: If connected to a degree-2 node, traverse the entire chain of degree-2 nodes until reaching the far junction, then add one skeleton edge representing the entire chain

Each skeleton edge is tagged as either:
- `chain_edge = True`: represents a contracted degree-2 chain
- `chain_edge = False`: represents a direct junction-to-junction connection

#### Step 3: Find Bridges Using Tarjan's Algorithm

Tarjan's bridge-finding algorithm uses DFS with low-link values:

```
For each node u:
  disc[u] = discovery time
  low[u] = lowest discovery time reachable from u's subtree
  
  For each neighbor v:
    If tree edge (u,v):
      Recurse on v
      low[u] = min(low[u], low[v])
      If low[v] > disc[u]:  # v cannot reach above u
        (u,v) is a BRIDGE
    If back edge (u,v):
      low[u] = min(low[u], disc[v])
```

**Critical detail**: We track edges by unique IDs (not just parent nodes) to correctly handle parallel edges. Two junction nodes may be connected by multiple independent degree-2 chains, which is not a bottleneck.

#### Step 4: Check Bridge Types and Component Sizes

A bottleneck exists if and only if:
- The skeleton has at least one bridge, AND
- That bridge is tagged as a `chain_edge = True`, AND
- Removing that bridge creates two components that BOTH have 2 or more nodes (true clusters)

Direct junction-to-junction bridges are not bottlenecks. Chain bridges leading to single isolated nodes (pendant arms) are also not bottlenecks, as they don't create the problematic dumbbell structure with two substantial clusters.

## Complexity Analysis

- **Time**: O(V + E) where V = number of geographic units, E = number of adjacencies
  - Building induced subgraph: O(V + E)
  - Contracting chains: O(V + E) single-pass traversal
  - Tarjan's DFS: O(V_skeleton + E_skeleton) where skeleton is smaller than original
  
- **Space**: O(V + E) for graph storage and auxiliary data structures

## Examples

### Example 1: Classic Dumbbell (Bottleneck)
```
A---B           E---F
 \ /             \ /
  C---D (d=2)---G

District: {A, B, C, D, E, F, G}
Bottleneck: Yes (node D with degree 2)
Result: False (is bottlenecked)
```

### Example 2: Parallel Chains (No Bottleneck)
```
A---B       E---F
 \ /         \ /
  C---1---2---G
   \         /
    3---4---/

District: {A, B, C, 1, 2, 3, 4, E, F, G}
Two paths: C→1→2→G and C→3→4→G
Result: True (not bottlenecked - redundant paths exist)
```

### Example 3: Direct Junction Bridge (No Bottleneck)
```
A---B       E---F
 \ /         \ /
  C---------G

District: {A, B, C, E, F, G}
C and G both have degree 3
Direct connection has no degree-2 nodes
Result: True (not a bottleneck by definition)
```

### Example 4: Linear Chain (No Bottleneck)
```
A---B (d=2)---C (d=2)---D (d=2)---E

District: {A, B, C, D, E}
Chain connects two single nodes (not clusters)
Result: True (not a bottleneck - endpoints are isolated units, not clusters)
```

### Example 5: Pendant Arm (No Bottleneck)
```
A---B---C
    |
    D (d=2)
    |
    E

District: {A, B, C, D, E}
Chain leads to single isolated unit E
Result: True (not a bottleneck - E is not a cluster)
```

## Implementation Notes

1. **Edge ID tracking**: Use unique edge IDs in Tarjan's algorithm to handle parallel edges correctly
2. **Empty cases**: Empty district or single node returns `True` (not bottlenecked)
3. **Disconnected graphs**: Return `True` by specification (can't have bottleneck if not connected)
4. **Pure cycles**: All degree-2 nodes → return `True` (no junction points to create dumbbell)

## References

- Tarjan, R. E. (1974). "A note on finding the bridges of a graph". *Information Processing Letters*.
- Applications in computational redistricting and gerrymandering detection
