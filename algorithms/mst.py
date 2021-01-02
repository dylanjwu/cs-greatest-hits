import heapq

# MODERATE

# import weighted graph
# implement Prim's algorithm

# undir weighted graph
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


def mst_prim(graph):
    # add all edges to q    
    heap = []
    for vert in graph.keys():
        for v_edge in graph[vert]:
            print(v_edge)
            # edge = tuple((v_edge) + (vert,))
            if v_edge not in heap:
                heapq.heappush(heap, v_edge)
    # sorted_heap = heapsort(heap)
    print(heapq.heappop(heap))


mst_prim(graph1)


def test_heap():
    h = []

    heapq.heappush(h, ('I', 1, 'H'))
    heapq.heappush(h, ('H', 2, 'I'))
    print(heapq.heappop(h))

test_heap()