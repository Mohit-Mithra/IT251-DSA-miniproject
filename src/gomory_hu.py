from collections import deque
from sys import maxsize as maxint
from lib.modified_edmonds_karp_algorithm import *

BLACK = 2
GRAY = 1
WHITE = 0


class GomoryHuTree:

    def __init__(self, graph):
        self.V = len(graph)
        self.capacity = {}
        for i in range(self.V):
            for j in range(self.V):
                self.capacity[i, j] = graph[i][j]
        self.color = {}
        self.pred = {}
        self.tree = {}
        self.graph = graph 

        self.build()
        self.prepare()

    def __repr__(self):
        return self.tree

    def __str__(self):
        return str(self.tree)

    def __getitem__(self, pos):
        i, j = pos
        return self.tree[i, j]


    def build(self):
        """Construct GomoryHuTree"""
        p = []
        f1 = []

        for i in range(self.V):
            p.append(0)
            f1.append(0)
            for j in range(self.V):
                self.tree[i, j] = 0

        for s in range(1, self.V):

            t = p[s]

            min_cut, self.color, self.pred = modified_edmonds_karp_max_flow(self.graph, s, t, self.color, self.pred)
            #print(min_cut)
            #print(self.color)
            f1[s] = min_cut

            
            for i in range(self.V):
                if i != s and p[i] == t and self.color[i] == BLACK:
                    #print("yes ", i)
                    p[i] = s

            if self.color[p[t]] == BLACK:
                p[s] = p[t]
                p[t] = s
                f1[s] = f1[t]
                f1[t] = min_cut

            #print(p)
            if s == self.V - 1:
                for i in range(1, s + 1):
                    self.tree[i, p[i]] = f1[i]


    def prepare(self):
        """Prepare for querying"""
        for i in range(self.V):
            for j in range(self.V):
                self.capacity[i, j] = self.tree[i, j]

    def query(self, u, v):
        """Query GomoryHuTree"""
        min_cut1, self.color, self.pred = modified_edmonds_karp_max_flow(self.graph, u, v, self.color, self.pred)
        min_cut2, self.color, self.pred = modified_edmonds_karp_max_flow(self.graph, v, u, self.color, self.pred)

        return max(min_cut1, min_cut2)
