from lib.edmonds_karp_algorithm import *

a = [[0 for x in range(100)] for x in range(100)]
mincut = [0 for x in range(100)]
maxminmincut = [[0 for x in range(100)] for x in range(100)]
flow = [[0 for x in range(100)] for x in range(100)]
prev = [0 for x in range(100)]
capto = [0 for x in range(100)]
queue = [0 for x in range(100)]	

#taking input
def tunnels():


	n = 0 
	e = 0
	file=open('input_tunnel_1.txt','r')
	fline = file.readline().strip()
	first = True
	for node in fline.split(' '):
		if first:
			first = False
			n = int(node)
			for i in range(0,n+1):
				for j in range(0,n+1):
					a[i][j]=0
		else:
			e = int(node)

	firstline = True
	print("\n\n\t\t\tThe input is:")
	for line in file:
	    line=line.strip()
	    print("\t\t\t"+str(line))
	    first=True
	    for node in line.split(' '):
	        if first:
	            first=False
	            x=int(node)
	        else:
	        	y=int(node)
	    a[x][y] += 1
	    a[y][x] += 1    

	file.close()

	for i in range(0,n+1):
		for j in range(0,n+1):
			maxminmincut[i][j]=0
		mincut[i]=0

	#n = input("enter the number of vertices(other than the exit):")
	#n = int(n)
	#e = input("enter the number of edges(paths)")
	#e = int(e)

	#for i in range(0,n+1):
	#	for j in range(0,n+1):
	#		maxminmincut[i][j]=0
	#	mincut[i]=0

	#for i in range(int(e)):
	#	x=input("enter the vertex 1 of the edge: ")
	#	y=input("enter the vertex 2 of the edge: ")
	#	x=int(x)
	#	y=int(y)
	#	a[x][y]+=1
	#	a[y][x]+=1

	#print()


	for i in range(1,n+1):
		mincut[i]=max_flow_value = edmonds_karp_max_flow(a, 0, i)
	findmaxminmincut(n)

	#dumpMat("maxMinMinCut", maxminmincut);
	#print()
	#print()
	#print("The number of Edges is :" + str(maxminmincut[0][1]));
	#print()
	return maxminmincut[0][1]

#dump contents of a matrix in rectangular form
def dumpMatrix(name,M):
	print()
	print("-------" + name + "---------")
	for i in range(len(M)):
		print(str(i) + ": ")
		for j in range(len(M[i])):
			print(str(M[i][j]) + " ")
		print()

#dump conents of a matrix in list form
def dumpMat(name,M):
	print()
	print("------- The Maxminmincut Matrix formed is: ---------")
	for i in range(len(M)):
		for j in range(len(M[i])):
			if (M[i][j] > 0):
				print("M[" + str(i) + "][" + str(j) + "] = " + str(M[i][j]))
			elif (M[i][j] != -M[j][i]):
				print("M[" + str(i) + "][" + str(j) + "] = " + str(M[i][j]))



def findmaxminmincut(n):
	for i in range(n+1):
		for j in range(n+1):
			if a[i][j]>0:
				maxminmincut[i][j]=mincut[j]
	for k in range(n+1):
		for i in range(n+1):
			for j in range(n+1):
				ij = maxminmincut[i][j]
				ik = maxminmincut[i][k]
				kj = maxminmincut[k][j]
				if ik>0 and kj>0:
					kk=min(ik,kj)
					if kk>=ij:
						maxminmincut[i][j]=kk







def main():
	tunnels()

#main()
#findmaxmincut

#print the final output


