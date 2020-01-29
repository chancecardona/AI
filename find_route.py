#import libs
import sys
from collections import defaultdict #better dict type. easier to make graphs

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
        self.distances[(n1, n2)] = int(d)
        self.distances[(n2, n1)] = int(d)


def dijkstra(graph, source, dest):
    Q = set()
    dist = {}
    prev = {}

    for n in graph.nodes:
        dist[n] = inf
        prev[n] = 'UNDEFINED'
        Q.add(n)
    dist[source] = 0

    while Q:
        #Find node with minimum distance
        cur = None
        for i in Q:
            if cur is None:
                cur = i
            elif dist[i] < dist[cur]:
                cur = i
        #Node is no longer unvisited
        Q.remove(cur)

        if cur == dest:
            break
        #Finds total distance for each neighbor
        for n in graph.edges[cur]:
            sum = dist[cur] + graph.distances[(cur, n)]
            if sum < dist[n]:
                dist[n] = sum
                prev[n] = cur

    return dist, prev



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

#uninformed search
dist, prev = dijkstra(g, fromCity, toCity)
#print(dist)
#print(prev)

path = []
u = toCity
if prev[u] != 'UNDEFINED' or u == fromCity:
    while u != 'UNDEFINED':
        path.insert(0, u)
        u = prev[u]

if dist[toCity] == inf:
    print('distance: infinity')
    print('route:')
    print('none')
else:
    print('distance:', dist[toCity], 'km')
    print('route:')
    for i in range(1, len(path)):
        p = path[i-1]
        c = path[i]
        print(p, 'to', c+',', g.distances[(p, c)], 'km')

