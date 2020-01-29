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
        self.distances = {}                 #want dictionary for distances. Key will be tuple city pairs.

    #add edge. Assuming 2 way graph since you can go to/from cities.
    def addEdge(self, n1, n2, d):
        self.nodes.add(n1)
        self.nodes.add(n2)
        self.edges[n1].append(n2)
        self.edges[n2].append(n1)
        self.distances[(n1, n2)] = int(d)
        self.distances[(n2, n1)] = int(d)

#Dijkstra is simplest uninformed search returning shortest path I could find.
#Adapted directly from the pseudocode found on wikipedia:
#available: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Pseudocode
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

        #Stop searching if we've reached the destination
        if cur == dest:
            break

        #Finds total distance for each neighbor
        for n in graph.edges[cur]:
            sum = dist[cur] + graph.distances[(cur, n)]
            if sum < dist[n]:
                dist[n] = sum
                prev[n] = cur

    #Create Array for the Shortest Path
    path = []
    u = dest
    if prev[u] != 'UNDEFINED' or u == source:
        while u != 'UNDEFINED':
            path.insert(0, u)
            u = prev[u]

    return dist, path


def main():
    #Get user data, open input file
    fileName = sys.argv[1]
    fromCity = sys.argv[2]
    toCity = sys.argv[3]
    f = open(fileName, 'r')

    #form tree by reading from file
    g = Graph()
    for line in f:
        if line == 'END OF INPUT\n':
            break
        words = line.split()
        g.addEdge(words[0], words[1], words[2])       #from city, to city, distance
    f.close()

    #uninformed search
    dist, path = dijkstra(g, fromCity, toCity)

    #Print answer
    if dist[toCity] == inf: #No Route
        print('distance: infinity')
        print('route:')
        print('none')
    else:                   #Route Exists
        print('distance:', dist[toCity], 'km')
        print('route:')
        for i in range(1, len(path)):
            p = path[i-1]
            c = path[i]
            print(p, 'to', c+',', g.distances[(p, c)], 'km')


if __name__ == '__main__':
    main()
