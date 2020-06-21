#Edmonds-Karp Algorithm
from collections import deque
from sys import maxsize as maxint

#find path by using BFS
def ek_bfs(graph, start, target, flow):
	
	V = len(graph)

	queue = deque()
	queue.append(start)
	paths = {start:[]}
	if start == target:
			return paths[start]

	while queue:
		u = queue.popleft()

		for v in range(V):

			if(graph[u][v]-flow[u][v]>0) and v not in paths:
				paths[v] = paths[u]+[(u,v)]

				if v == target:
					#print(paths[v])
					return paths[v]

				queue.append(v)

	return None


def edmonds_karp_max_flow(graph, source, sink):
	
	V = len(graph) 
	flow = []

	for i in range(V):
		flow.append([0] * V)       
	
	path = ek_bfs(graph, source, sink, flow)
 
	while path != None:

		f = min(graph[u][v] - flow[u][v] for u,v in path)

		for u,v in path:
			flow[u][v] += f
			flow[v][u] -= f

		path = ek_bfs(graph, source, sink, flow)

	final_flow = []
	for i in range(V):
		final_flow.append(flow[source][i])              # Find the final total flow by adding flows across all paths

	return (sum(final_flow))