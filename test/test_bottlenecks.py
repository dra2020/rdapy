"""
Test suite for bottleneck detection in connected geographic units.

Tests cover:
- Disconnected graphs
- Connected graphs without bottlenecks (triangles, grids, cycles, parallel paths)
- Connected graphs with bottlenecks (dumbbells, hourglasses, linear chains)
- Edge cases (empty, single node, two nodes)
"""

from rdapy import not_bottlenecked


class TestBottleneckDetection:
    def test_disconnected_two_components(self) -> None:
        r"""
        Two separate triangles - not connected
        
        A---B       D---E
        \ /         \ /
        C           F
        """
        graph = {
            'A': ['B', 'C'],
            'B': ['A', 'C'],
            'C': ['A', 'B'],
            'D': ['E', 'F'],
            'E': ['D', 'F'],
            'F': ['D', 'E'],
        }
        ids = ['A', 'B', 'C', 'D', 'E', 'F']
        assert not_bottlenecked(ids, graph) == True  # Not connected → True


    def test_disconnected_isolated_node(self) -> None:
        r"""
        Triangle with isolated node
        
        A---B    D
         \ /
          C
        """
        graph = {
            'A': ['B', 'C'],
            'B': ['A', 'C'],
            'C': ['A', 'B'],
            'D': [],
        }
        ids = ['A', 'B', 'C', 'D']
        assert not_bottlenecked(ids, graph) == True  # Not connected → True


    def test_simple_triangle_no_bottleneck(self) -> None:
        r"""
        Simple triangle - no degree-2 nodes, fully connected
        
        A---B
         \ /
          C
        """
        graph = {
            'A': ['B', 'C'],
            'B': ['A', 'C'],
            'C': ['A', 'B'],
        }
        ids = ['A', 'B', 'C']
        assert not_bottlenecked(ids, graph) == True


    def test_grid_no_bottleneck(self) -> None:
        r"""
        2x2 grid with diagonals - multiple independent paths
        
        A---B
        |\ /|
        | X |
        |/ \|
        C---D
        """
        graph = {
            'A': ['B', 'C', 'D'],
            'B': ['A', 'C', 'D'],
            'C': ['A', 'B', 'D'],
            'D': ['A', 'B', 'C'],
        }
        ids = ['A', 'B', 'C', 'D']
        assert not_bottlenecked(ids, graph) == True


    def test_pure_cycle_no_bottleneck(self) -> None:
        r"""
        Simple square cycle - all nodes have degree 2
        
        A---B
        |   |
        D---C
        """
        graph = {
            'A': ['B', 'D'],
            'B': ['A', 'C'],
            'C': ['B', 'D'],
            'D': ['C', 'A'],
        }
        ids = ['A', 'B', 'C', 'D']
        assert not_bottlenecked(ids, graph) == True


    def test_complete_graph_no_bottleneck(self) -> None:
        r"""
        Complete graph K4 - every node connected to every other node
        (visualized as square with both diagonals)
        
        A---B
        |\ /|
        | X |
        |/ \|
        D---C
        """
        graph = {
            'A': ['B', 'D', 'C'],
            'B': ['A', 'C', 'D'],
            'C': ['B', 'D', 'A'],
            'D': ['C', 'A', 'B'],
        }
        ids = ['A', 'B', 'C', 'D']
        assert not_bottlenecked(ids, graph) == True


    def test_classic_dumbbell_bottleneck(self) -> None:
        r"""
        Classic dumbbell - two triangles connected by single degree-2 node
        
        A---B           E---F
         \ /             \ /
          C---D (d=2)  ---G
        """
        graph = {
            'A': ['B', 'C'],
            'B': ['A', 'C'],
            'C': ['A', 'B', 'D'],
            'D': ['C', 'E'],  # degree-2 bottleneck
            'E': ['D', 'F', 'G'],
            'F': ['E', 'G'],
            'G': ['E', 'F'],
        }
        ids = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        assert not_bottlenecked(ids, graph) == False  # Has bottleneck


    def test_long_chain_bottleneck(self) -> None:
        r"""
        Two triangles connected by long chain of degree-2 nodes
        
        A---B               E---F
         \ /                 \ /
          C--1---2---3 (d=2)--G
        """
        graph = {
            'A': ['B', 'C'],
            'B': ['A', 'C'],
            'C': ['A', 'B', '1'],
            '1': ['C', '2'],  # degree-2
            '2': ['1', '3'],  # degree-2
            '3': ['2', 'E'],  # degree-2
            'E': ['3', 'F', 'G'],
            'F': ['E', 'G'],
            'G': ['E', 'F'],
        }
        ids = ['A', 'B', 'C', '1', '2', '3', 'E', 'F', 'G']
        assert not_bottlenecked(ids, graph) == False  # Has bottleneck


    def test_direct_junction_bridge_no_bottleneck(self) -> None:
        r"""
        Two triangles connected by junction-to-junction edge (no degree-2 chain)
        
        A---B       E---F
         \ /         \ /
          C-----------G
        
        C and G both have degree 3, direct connection has no degree-2 nodes
        """
        graph = {
            'A': ['B', 'C'],
            'B': ['A', 'C'],
            'C': ['A', 'B', 'G'],
            'E': ['F', 'G'],
            'F': ['E', 'G'],
            'G': ['E', 'F', 'C'],
        }
        ids = ['A', 'B', 'C', 'E', 'F', 'G']
        assert not_bottlenecked(ids, graph) == True  # No degree-2 chain → not a bottleneck


    def test_parallel_chains_no_bottleneck(self) -> None:
        r"""
        Two clusters connected by TWO independent degree-2 chains
        
        A---B       E---F
         \ /         \ /
          C---1---2---G
           \         /
            3---4---/
        
        Chain 1: C-1-2-G (nodes 1,2 are degree-2)
        Chain 2: C-3-4-G (nodes 3,4 are degree-2)
        """
        graph = {
            'A': ['B', 'C'],
            'B': ['A', 'C'],
            'C': ['A', 'B', '1', '3'],
            '1': ['C', '2'],  # degree-2
            '2': ['1', 'G'],  # degree-2
            '3': ['C', '4'],  # degree-2
            '4': ['3', 'G'],  # degree-2
            'E': ['F', 'G'],
            'F': ['E', 'G'],
            'G': ['E', 'F', '2', '4'],
        }
        ids = ['A', 'B', 'C', '1', '2', '3', '4', 'E', 'F', 'G']
        assert not_bottlenecked(ids, graph) == True  # No bottleneck (multiple paths)


    def test_y_shape_no_bottleneck(self) -> None:
        r"""
        Y-shaped graph - B has degree 3 (branches to C and D)
        
            A
            |
            B (d=3)
           / \
          C   D
        """
        graph = {
            'A': ['B'],
            'B': ['A', 'C', 'D'],  # degree-3
            'C': ['B'],
            'D': ['B'],
        }
        ids = ['A', 'B', 'C', 'D']
        assert not_bottlenecked(ids, graph) == True


    def test_pendant_chain_no_bottleneck(self) -> None:
        r"""
        T-shaped with degree-2 chain on pendant arm
        Chain connects leaf node E to junction B
        (Not a dumbbell - E is isolated, not a cluster)
        
        A---B---C
            |
            D (d=2)
            |
            E
        """
        graph = {
            'A': ['B'],
            'B': ['A', 'C', 'D'],
            'C': ['B'],
            'D': ['B', 'E'],  # degree-2
            'E': ['D'],
        }
        ids = ['A', 'B', 'C', 'D', 'E']
        assert not_bottlenecked(ids, graph) == True


    def test_complex_dumbbell_bottleneck(self) -> None:
        r"""
        Larger clusters connected by single degree-2 node
        
        A---B---C       G---H---I
         \ / \ /         \ / \ /
          D---E--F (d=2)--J---K
        """
        graph = {
            'A': ['B', 'D'],
            'B': ['A', 'C', 'D', 'E'],
            'C': ['B', 'E'],
            'D': ['A', 'B', 'E'],
            'E': ['B', 'C', 'D', 'F'],
            'F': ['E', 'J'],  # degree-2 bottleneck
            'G': ['H', 'J'],
            'H': ['G', 'I', 'J', 'K'],
            'I': ['H', 'K'],
            'J': ['F', 'G', 'H', 'K'],
            'K': ['H', 'I', 'J'],
        }
        ids = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
        assert not_bottlenecked(ids, graph) == False  # Has bottleneck at F


    def test_single_node(self) -> None:
        r"""
        Single node - trivially not bottlenecked
        
        A
        """
        graph = {'A': []}
        ids = ['A']
        assert not_bottlenecked(ids, graph) == True


    def test_two_nodes_connected(self) -> None:
        r"""
        Two nodes connected - both degree 1, no bottleneck
        
        A---B
        """
        graph = {
            'A': ['B'],
            'B': ['A'],
        }
        ids = ['A', 'B']
        assert not_bottlenecked(ids, graph) == True


    def test_linear_chain_not_bottleneck(self) -> None:
        r"""
        Linear chain - degree-2 nodes connect two leaf nodes
        (NOT a dumbbell - both "clusters" are single nodes, not clusters)
        
        A---B (d=2)---C (d=2)---D (d=2)---E
        """
        graph = {
            'A': ['B'],
            'B': ['A', 'C'],  # degree-2
            'C': ['B', 'D'],  # degree-2
            'D': ['C', 'E'],  # degree-2
            'E': ['D'],
        }
        ids = ['A', 'B', 'C', 'D', 'E']
        assert not_bottlenecked(ids, graph) == True


    def test_empty_ids(self) -> None:
        r"""Empty ids list"""
        graph = {'A': ['B'], 'B': ['A']}
        ids = []
        assert not_bottlenecked(ids, graph) == True


    def test_star_no_bottleneck(self) -> None:
        r"""
        Star graph - one central hub connected to leaves
        
            B
            |
        C---A---D
            |
            E
        """
        graph = {
            'A': ['B', 'C', 'D', 'E'],
            'B': ['A'],
            'C': ['A'],
            'D': ['A'],
            'E': ['A'],
        }
        ids = ['A', 'B', 'C', 'D', 'E']
        assert not_bottlenecked(ids, graph) == True


    def test_hourglass_bottleneck(self) -> None:
        r"""
        Hourglass - two triangles connected by degree-2 chain
        
        A---B
         \ /
          C
          |
          D (d=2)
          |
          E
         / \
        F---G
        """
        graph = {
            'A': ['B', 'C'],
            'B': ['A', 'C'],
            'C': ['A', 'B', 'D'],
            'D': ['C', 'E'],  # degree-2
            'E': ['D', 'F', 'G'],
            'F': ['E', 'G'],
            'G': ['E', 'F'],
        }
        ids = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        assert not_bottlenecked(ids, graph) == False  # Bottleneck at D

### END ###