

from lib.test import *


def main():
	# make a capacity graph
	graph = [[ 0, 3, 3, 0, 0, 0 ],  # 0
	 [ 0, 0, 2, 3, 0, 0 ],  # 1
	 [ 0, 0, 0, 0, 2, 0 ],  # 2
	 [ 0, 0, 0, 0, 4, 2 ],  # 3
	 [ 0, 0, 0, 0, 0, 2 ],  # 4
	 [ 0, 0, 0, 0, 0, 0 ]]  # 5

	source = 0  
	sink = 5   

	V = 6


	color = {}
	pred = {}
	tree = {}
	flow = {}
	depth = {}
		# node 0  1  2  3  4  5


	max_flow, color, pred, depth, flow = modified_edmonds_karp_max_flow(graph, source, sink, color, pred, depth, flow)
	print(max_flow)

if __name__ == "__main__":
	main()