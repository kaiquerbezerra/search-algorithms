class FloydWarshallGraph():
    def __init__(self, n_nodes):
        self.N = n_nodes
        self.graph = [[float('inf')] * n_nodes for _ in range(n_nodes)]
        for i in range(n_nodes):
            self.graph[i][i] = 0

    def prettier(self):
        for i in range(1, 50):
            print("-", end='')
        print("")

    def addEdge(self, u, v, w):
        self.graph[u][v] = w

    def showResult(self, distance):
        self.prettier()
        print("Source Node \tDestination Node \tDistance")
        for u in range(self.N):
            for v in range(self.N):
                if u != v:
                    print(f"{u}\t\t{v}\t\t\t{distance[u][v]}")
        self.prettier()

    def floydWarshallSearch(self):
        distance = [row[:] for row in self.graph]

        for t in range(self.N):
            for u in range(self.N):
                for v in range(self.N):
                    if distance[u][v] > distance[u][t] + distance[t][v]:
                        distance[u][v] = distance[u][t] + distance[t][v]

        self.showResult(distance)

fwgraph = FloydWarshallGraph(6)

fwgraph.addEdge(0, 1, 2)
fwgraph.addEdge(0, 3, 5)
fwgraph.addEdge(0, 4, 3)
fwgraph.addEdge(1, 0, 3)
fwgraph.addEdge(1, 5, 6)
fwgraph.addEdge(1, 2, 2)
fwgraph.addEdge(1, 3, 2)
fwgraph.addEdge(2, 5, 1)
fwgraph.addEdge(2, 3, 1)
fwgraph.addEdge(3, 4, 1)
fwgraph.addEdge(4, 3, 2)

fwgraph.floydWarshallSearch()
