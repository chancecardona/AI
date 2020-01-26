#import libs
from collections import defaultdict #better dict type. easier to make graphs
import sys

#define graph class
def Graph:
    #Constructor
    def __init__(self):
        self.node = defaultdict(list)  #a node is just a list (of vertice - cost tuples) in the graph
    #add edge
    def addEdge(self,n,v):
        self.node[n].append(v)     #adds edge v to node n.

    def DFSUtil(self, v, visited):
        visited[v] = True   #current node has now been visited
        for i in self.node[v]:
            if visited[i] == False: #for all unvisited edges repeat this
                self.DFSUtil(i, visited)

    def DFS(self):
        V = len(self.node) #total vertices
        visited = [False]*V #all vertices start uninitialized
        for i in range(V):
            if visited[i] == False:
                self.DFSUtil(i, visited)


#Open input file, set goals
fileName = sys.argv[1]
fromCity = sys.argv[2]
toCity = sys.argv[3]

f = open(fileName, 'r')

#form tree
g = Graph()
for line in f:
    words = line.split()
    g.addEdge(words[0], (words[1], words[2]))       #input node, and vertice/distance tuple

f.close()

#uninformed search
g.DFS(fileName)

#go throughs all nodes. need to stop at destination node.
#need a way to add distance as well and find shortest path
#"path" list?




#output simplified results
