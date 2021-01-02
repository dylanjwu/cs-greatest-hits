import heapq
# HARD


graph1 = {
    'A': [('B', 4),('H', 8)],
    'B': [('A', 4),('H', 11), ('C', 8)],
    'C': [('B', 8),('I', 2),('F', 4),('D', 7)],
    'D': [('C', 7),('F', 14),('E', 9)],
    'E': [('D', 9),('F', 10)],
    'F': [('E', 10),('D', 14),('C', 4),('G', 2)],
    'G': [('F', 2),('I', 6),('H', 1)],
    'H': [('G', 1),('I',7),('B',11),('A', 8)],
    'I': [('G',6),('C', 2),('H',7)]
}

# Bellman-Ford 

# Dijkstra 

# def dijkstra(graph, start, end):
#     # for each vertex of the graph
#     # add to min priority queue (heap-based)
#     # with key, e.g. for vertex A, (A, key)
#     # set the key of the start vertex to be 0
#     # set all other keys to be INF 
#     while queue:
#         v = heapq.heappop(queue)
#         if v == end:
#             return
#         for edge in graph[v]:
#             #TODO: modify key of u of edge=(v,u)
#             key = key + edge.weight
#             #increase key, put back in heap

    

