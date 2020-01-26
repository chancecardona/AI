#import libs
from collections import defaultdict #better dict type. easier to make graphs

#define graph class
def Graph:
    #Constructor
    def __init__(self):
        self.node = defaultdict(list)  #a node is just a list (of vertices) in the graph
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


#create data array from input file

#form tree

#uninformed search
#using DFS. need LIFO queue.


#frontier.append(start)
#while frontier.len > 0
    #cur = pop.frontier
    #if cur == goal
        #return
    #if cur not in explored
        #explored.append(cur)
    #frontier.append(cur.children[i])
    #i++





#output simplified results
