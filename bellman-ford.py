class BellmanFordGraph():
  def __init__(self, n_nodes):
    self.N = n_nodes
    self.graph = []
    
  def addEdge(self, u, v, w):
    self.graph.append([u, v , w])

  def prettier(self):
    for i in range(1, 80):
      print("-", end='')
    print("")

  def showNeighbors(self, neighbor):
    self.prettier()
    print("Neighbors: ", neighbor)
  
  def displayShortestPath(self, neighbor, j):
    if neighbor[j] == -1:
      print("\t", j, end=' ')
      return
    self.displayShortestPath(neighbor, neighbor[j])
    print("-->", j, end=' ')

  def showResult(self, distance, neighbor):
    print("Node \tSource Distance \tShortest Path")
    for node in range(self.N):
      print(node, "\t", distance[node], "\t\t", end='')
      self.displayShortestPath(neighbor, node)
      print("")

  def bellmanFordSearch(self, source_node):
    self.prettier()
    infinite = 1e7
    distance = [infinite] * self.N
    neighbor = [-1] * self.N
    distance[source_node] = 0
    for c in range(self.N - 1):
      for u, v, w in self.graph:
        if distance[u] != infinite and distance[u] + w < distance[v]:
          distance[v] = distance[u] + w
          neighbor[v] = u

    for u, v, w in self.graph:
      if distance[u] != infinite and distance[u] + w < distance[v]:
        print("Graph contains negative weight cycle")
        return
    
    self.showResult(distance, neighbor)
    self.showNeighbors(neighbor)

bfgraph = BellmanFordGraph(5)
bfgraph.addEdge(0, 1, 1)
bfgraph.addEdge(0, 2, -2)
bfgraph.addEdge(1, 2, 1)
bfgraph.addEdge(1, 3, 4)
bfgraph.addEdge(1, 4, 3)
bfgraph.addEdge(3, 2, 2)
bfgraph.addEdge(3, 1, 2)
bfgraph.addEdge(4, 3, -1)


bfgraph.bellmanFordSearch(0)