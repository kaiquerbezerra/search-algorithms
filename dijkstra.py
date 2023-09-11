class DijkstraGraph():
  def __init__(self, n_nodes):
    self.N = n_nodes
    self.graph = [[0 for c in range(n_nodes)]
                  for r in range(n_nodes)]
    
  def prettier(self):
    for i in range(1, 80):
      print("-", end='')
    print("")

  def showNeighbors(self, neighbor):
    self.prettier()
    print("Neighbors: ", neighbor)

  def minDistance(self, distance, spt):
    min = 1e7
    for u in range(self.N):
      if distance[u] < min and spt[u] == False:
        min = distance[u]
        min_index = u
    return min_index  
  
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

  def dijkstraSearch(self, source_node):
    self.prettier()
    distance = [1e7] * self.N
    neighbor = [-1] * self.N
    distance[source_node] = 0
    spt = [False] * self.N
    for c in range(self.N):
      u = self.minDistance(distance, spt)
      spt[u] = True
      for v in range(self.N):
        if self.graph[u][v] > 0 and spt[v] == False and distance[v] > distance[u] + self.graph[u][v]:
          distance[v] = distance[u] + self.graph[u][v]
          neighbor[v] = u

    self.showResult(distance, neighbor)
    self.showNeighbors(neighbor)

dgraph = DijkstraGraph(12)
dgraph.graph = [
        [0, 3, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0],
        [3, 0, 5, 0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 5, 0, 4, 0, 3, 0, 0, 1, 0, 0, 0],
        [0, 0, 4, 0, 6, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 8, 9, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 4, 5, 0, 0, 0],
        [5, 7, 0, 0, 0, 0, 4, 0, 6, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 5, 6, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0]
        ]

dgraph.dijkstraSearch(0)