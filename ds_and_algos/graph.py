
# adjaceny matrix and adjacency list representations

# unweighted and nonweighted representations

# DFS and BFS (iterative and recursive algorithms)

# topo sort and strongly-connected components implementations

# find cycle in graph algorithm

NUM_VERTS = 10
adj_matrix = [[0]*NUM_VERTS] * NUM_VERTS
adj_list = [[]] * NUM_VERTS

# unweighted, weighted
# directed vs undirected
class Graph:
    def __init__(self, verts):
        self.matrix = [[0]*verts]*verts
        self.list = [[]]*verts
    def add_edge(self, vert, edge):
        if vert >= 0 and vert < len(self.list):
            if edge >= 0 and edge < len(self.list):
                self.list[vert].append(edge)
                self.matrix[vert][edge] = 1

    def dfs_recursive(self):
        pass
    def dfs_iterative(self):
        pass
    def bfs_recursive(self):
        pass
    def bfs_iterative(self):
        pass
    def contains_cycle(self):
        pass
    def is_undirected(self):
        pass
    def strongly_connected_components(self):
        pass
