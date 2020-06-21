from lib.ford_fulkerson_algorithm import *
from lib.edmonds_karp_algorithm import *
from lib.push_relabel_algorithm import *
from lib.dinic_algorithm import *

from gomory_hu import GomoryHuTree
from tunnels import *

def main():

	print("------------------------------------------------------------------------------------------")
	print("Hello, and welcome")
	print("Enter the option to execute the option you want")
	print("1 - Test various implementations of Max-Flow algorithms")
	print("2 - Test the Gomory-Hu Data Structure, built on the Edmonds-Karp Algorithm for Max-Flow ")
	print("3 - Application of Max Flow: Analysis of escape routes in an underground tunnel network and determining most efficient way to prevent escape")
	print("4 - Exit")
	option = int(input())
	while(option in [1, 2, 3]):

		if(option in [1, 2]):

			C = []

			
			# C = [[ 0, 3, 3, 0, 0, 0 ],  # 0
			# 	 [ 0, 0, 2, 3, 0, 0 ],  # 1
			# 	 [ 0, 0, 0, 0, 2, 0 ],  # 2
			# 	 [ 0, 0, 0, 0, 4, 2 ],  # 3
			# 	 [ 0, 0, 0, 0, 0, 2 ],  # 4
			# 	 [ 0, 0, 0, 0, 0, 0 ]]  # 5

			# C = [[ 0 , 10, 0, 0, 0, 8 ],  # 0
			# 	 [ 10, 0 , 4, 0, 2, 3 ],  # 1
			# 	 [ 0,  4,  0, 5, 4, 2 ],  # 2
			# 	 [ 0,  0,  5, 0, 7, 2 ],  # 3
			# 	 [ 0,  2,  4, 7, 0, 3 ],  # 4
			# 	 [ 8,  3,  2, 2, 3, 0 ]]  # 5

			

			file=open('input_gomoryhu_1.txt','r')
			for line in file:
				line=line.strip()
				adjacentVertices = []
				#first=True
				for node in line.split(' '):
					#if first:
					#    first=False
					#    continue
					adjacentVertices.append(int(node))
				C.append(adjacentVertices)

			file.close()

			#print(C) 

		if (option == 1):
			print("	--------------------------------------------------------------------------------")
			print("	Enter the algorithm option to test it's implementation")
			print("	1 - Ford-Fulkerson Algorithm ")
			print("	2 - Edmonds-Karp Algorithm")
			print("	3 - Dinic's Algorithm")
			print("	4 - Push-Relabel Algorithm") 

			algorithm = int(input("	"))

			if(algorithm in [1, 2, 3, 4, 5]):

				print()
				print("		The input graph is obtained from file 'input.txt' in weighted adjacency matrix format, with 0 being the first node")
				
				for vector in C:
					print("		", vector)

				print()
				print("		Enter the source vertex:")
				source = int(input("		"))
				print("		Enter the sink vertex:")
				sink = int(input("		"))

				if(source == sink):
					print()
					print("		The source can't be the same as sink. Please try again")
					print()
					continue

				if(algorithm == 1):  

					print()
					max_flow_value = ford_fulkerson_max_flow(C, source, sink)
					print ("	Ford-Fulkerson algorithm")
					print ("	max flow value is: ", max_flow_value)
					print()

				elif(algorithm == 2):

					print()
					max_flow_value = edmonds_karp_max_flow(C, source, sink)
					print ("	Edmonds-Karp algorithm")
					print ("	max flow value is: ", max_flow_value)
					print()

				elif(algorithm == 3):	

					print()
					max_flow_value = dinic_maxflow(C, source, sink)
					print ("	Dinic's algorithm")
					print ("	max flow value is: ", max_flow_value)
					print()

				else:
					print()
					max_flow_value = push_relabel_max_flow(C, source, sink)
					print ("	Push-Relabel algorithm")
					print ("	max flow value is: ", max_flow_value)
					print()

			else:
				print("		Invalid option, please try again")

		elif (option == 2):

			print()

			print()
				
			#print(gomory_tree)

			print("	Gomory-Hu Tree(shown below) constructed. Ready to handle queries")
			print()
			tree = GomoryHuTree(C)

			print()


			# Print Tree Contents
			gomory_tree = {}
			for node in tree.tree:
				
				if(tree.tree[node] > 0):
					gomory_tree[node] = tree.tree[node]
					print("	", node, tree.tree[node])	
			print()
			print("	This tree can be used to find the minimum of all s-t cuts.")
			print("	From max-flow min-cut theorem states that:")
			print()
			print("		 amount of maximum flow = capacity of the minimum cut.")
			print()
			print("	For this graph, the minimum cut of the entire network is", min(gomory_tree.values()))
			print()
			print("	This tree can also be used to achieve an approximate solution for minimum k-cut problem")
			print("	This is an NP Hard problem, but Gomory-Hu Tree provides results within bounds of (2 - 2/k).")
			print("	For the given network, the minimum k-cut results in the following components, for K = 3")
			K = 3
			sorted_weights = sorted(list(gomory_tree.values()))

			for i in range(K-1):
				sorted_weights.pop(0)

			component_edges = []
			for weight in sorted_weights:
				component_edges.append(list(list(gomory_tree.keys())[list(gomory_tree.values()).index(weight)]))
			
			#print(component_edges)

			total_components = []

			for u, v in component_edges:
				#for u,v in edge:
				#print(u, v)
				flag = 0
				for component in total_components:
					if ((u in component) or (v in component)): 
						component.add(u)
						component.add(v)
						flag = 1
						break

				if(not flag):
					#print("here")		
					component = {u, v}
					total_components.append(component)

			for node in range(len(C)):
				flag = 0
				for component in total_components:
					if node in component:
						flag = 1
						break 
				if(not flag):		
					component = {node}
					total_components.append(component)

			print()
			print("	", total_components)


			print()
			print("	This tree can also be used to find the minimum s-t cut for any/all pairs of vertices.")
			print("	To test this, enter any 2 vertices and the program will return the minimum s-t cut across 2 vertices")
			print()
			# Query for min cut between 0 and 4
			print("        Enter the 2 vertices to query for the minimum cut")
			print()

			print("        Enter the vertex 1 - ", end = " ")
			v1 = int(input())
			print("        Enter the vertex 2 - ", end = " ")
			v2 = int(input())
			print()
			#print("        The Max-Flow minimum-cut between them is")
			print("	The minimum s-t cut between the 2 vertices is - ", tree.query(v1, v2))

			print()
			#print("       ", tree.query(v2, v1))

		elif (option == 3):
			result = tunnels()
			print("\n\n\n\t\t\tThe answer for the minimum number of tunnels to collapse is : " + str(result))
		
		print()
		print("------------------------------------------------------------------------------------------")
		print("Enter the option to execute the option you want")
		print("1 - Test various implementations of Max-Flow algorithms")
		print("2 - Test the Gomory-Hu Data Structure, built on the Edmonds-Karp Algorithm for Max-Flow ")
		print("3 - Application of Max Flow: Analysis of escape routes in an underground tunnel network and determining most efficient way to prevent escape")
		print("4 - Exit")
		option = int(input())


if __name__ == "__main__":
	main()