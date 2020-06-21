#Ford-Fulkerson Algorithm

#find path by using BFS
def ff_dfs(C, F, s, t):

	stack = [s]
	paths={s:[]}

	if s == t:
		return (paths[s])

	while(stack):
		u = stack.pop()

		for v in range(len(C)):

			if(C[u][v]-F[u][v]>0) and v not in paths:    # If a path exists in the residual graph C-F (if an edge is u->v(5) in C  and
														 # v->u(2) in F, then it is u->v(3) in C-F)
				paths[v] = paths[u]+[(u,v)]
				

				if v == t:
					#print (paths[v])
					return (paths[v])

				stack.append(v)

	return None

def ford_fulkerson_max_flow(C, s, t):

	n = len(C) 					#n -> number of vertices
	F = []

	for i in range(n):
		F.append([0] * n)		


	path = ff_dfs(C, F, s, t)		#Find an augmenting path if it exists, from s to t in residual graph C-F 
	
	while path != None:

		flow = min(C[u][v] - F[u][v] for u,v in path)    #Minimum flow along this path

		for u,v in path:
			F[u][v] += flow
			F[v][u] -= flow

		path = ff_dfs(C,F,s,t) 						#Find an augmenting path if it exists, from s to t in residual graph C-F 


		final_flow = []


		for i in range(n):
			final_flow.append(F[s][i])  			# Find the final total flow by adding flows across all paths

	return (sum(final_flow))
	
