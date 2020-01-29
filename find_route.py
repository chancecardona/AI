#import libs
from collections import defaultdict #better dict type. easier to make graphs
import sys

inf = float('inf')

#define graph class
class Graph:
    #Constructor
    def __init__(self):
        self.nodes = set()                  #can only be 1 of each node so we use set
        self.edges = defaultdict(list)      #want a dictionary of lists. defaultdict is best for this
        self.distances = {}                 #want dictionary for distances

    #add edge
    def addEdge(self, n1, n2, d):
        self.nodes.add(n1)
        self.nodes.add(n2)
        self.edges[n1].append(n2)
        self.edges[n2].append(n1)       #assuming 2 way graph... can typically go to/from cities
        self.distances[(n1, n2)] = d



def dijkstra(graph, source, dest):
    unvisited = set(graph.nodes)
    visited = set()
    dist = {}

    for n in unvisited:
        dist[n] = inf #infinity
    dist[source] = 0

    cur = source
    while unvisited:
        if visited.
        for n in graph.edges[cur]:
            sum = dist[cur] + graph.distances[(cur, n)]
            if sum < dist[n]
                dist[n] = sum
        unvisited.remove(cur)
        visited.add(cur)
        cur = min(dist, key=d.get)




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
    g.addEdge(words[0], words[1], words[2])       #from city, to city, distance

f.close()

print('beginning search')

#uninformed search
dijkstra(g, fromCity, toCity)

#go throughs all nodes. need to stop at destination node.
#need a way to add distance as well and find shortest path
#"path" list?




#output simplified results
