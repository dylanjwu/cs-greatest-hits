import heapq

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

    
# Python program for Dijkstra's single 
# source shortest path algorithm. The program is 
# for adjacency matrix representation of the graph 

# Library for INT_MAX 
import sys 

class Graph(): 

	def __init__(self, vertices): 
		self.V = vertices 
		self.graph = [[0 for column in range(vertices)] 
					for row in range(vertices)] 

	def printSolution(self, dist): 
		print ("Vertex tDistance from Source") 
		for node in range(self.V): 
			print (node, "t", dist[node]) 

	# A utility function to find the vertex with 
	# minimum distance value, from the set of vertices 
	# not yet included in shortest path tree 
	def minDistance(self, dist, sptSet): 

		# Initilaize minimum distance for next node 
		min = sys.maxsize 

		# Search not nearest vertex not in the 
		# shortest path tree 
		for v in range(self.V): 
			if dist[v] < min and sptSet[v] == False: 
				min = dist[v] 
				min_index = v 

		return min_index 

	# Funtion that implements Dijkstra's single source 
	# shortest path algorithm for a graph represented 
	# using adjacency matrix representation 
	def dijkstra(self, src): 

		dist = [sys.maxsize] * self.V 
		dist[src] = 0
		sptSet = [False] * self.V 

		for cout in range(self.V): 

			# Pick the minimum distance vertex from 
			# the set of vertices not yet processed. 
			# u is always equal to src in first iteration 
			u = self.minDistance(dist, sptSet) 

			# Put the minimum distance vertex in the 
			# shotest path tree 
			sptSet[u] = True

			# Update dist value of the adjacent vertices 
			# of the picked vertex only if the current 
			# distance is greater than new distance and 
			# the vertex in not in the shotest path tree 
			for v in range(self.V): 
				if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]: 
					    dist[v] = dist[u] + self.graph[u][v] 

		self.printSolution(dist) 

# Driver program 
g = Graph(9) 
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
		[4, 0, 8, 0, 0, 0, 0, 11, 0], 
		[0, 8, 0, 7, 0, 4, 0, 0, 2], 
		[0, 0, 7, 0, 9, 14, 0, 0, 0], 
		[0, 0, 0, 9, 0, 10, 0, 0, 0], 
		[0, 0, 4, 14, 10, 0, 2, 0, 0], 
		[0, 0, 0, 0, 0, 2, 0, 1, 6], 
		[8, 11, 0, 0, 0, 0, 1, 0, 7], 
		[0, 0, 2, 0, 0, 0, 6, 7, 0] 
		]; 

g.dijkstra(0); 

# This code is contributed by Divyanshu Mehta 

