#import libs
from collections import defaultdict #better dict type. easier to make graphs
import sys

#define graph class
class Graph:
    #Constructor
    def __init__(self):
        self.graph = defaultdict(list)  #a node is just a list (of vertice - cost tuples) in the graph
    #add edge
    def addEdge(self,n,v):
        self.graph[n].append(v)     #adds edge v to node n.

    def DFSUtil(self, v, visited):
        visited.append(v)   #current node has now been visited
        #print(visited)
        print(v)
        for i in self.graph[v]:
            i = i[0]
            if i not in visited: #for all unvisited edges repeat this
                self.DFSUtil(i, visited)

    def DFS(self, start):
        V = len(self.graph) #total vertices
        print('Total Vertices', V)
        visited = [] #all vertices start uninitialized
        self.DFSUtil(start, stop, visited)


#Open input file, set goals
fileName = sys.argv[1]
fromCity = sys.argv[2]
toCity = sys.argv[3]

f = open(fileName, 'r')

#form tree
g = Graph()
for line in f:
    if line == 'END OF INPUT\n':
        break
    words = line.split()
    g.addEdge(words[0], (words[1], words[2]))       #input node, and vertice/distance tuple

f.close()

print('beginning search')
#uninformed search
g.DFS(fromCity, toCity)

#go throughs all nodes. need to stop at destination node.
#need a way to add distance as well and find shortest path
#"path" list?




#output simplified results
