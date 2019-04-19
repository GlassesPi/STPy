from math import inf
class Graph:
    def __init__(self, v, e):
        self.vertices = v
        self.edges = e

    def dfs(self, u, d):
        self.vertices[u].is_visited = True
        self.vertices[u].distance = d
        print('{} {}'.format(self.vertices[u].key, self.vertices[u].distance))
        for v in self.edges[u]:
            if not self.vertices[v].is_visited:
                self.dfs(v, d + 1)

class Node:
    def __init__(self, k):
        self.key = k
        self.is_visited = False
        self.distance = inf

vertex = [Node('Tehran'),Node('Mazandaran'),Node('Qom'),Node('Kashan'),Node('Markazi'),Node('Isfahan'),]
edge = [[1,2], [0], [0, 3, 4], [2, 5], [2], [3]]
g = Graph(vertex, edge)
g.dfs(0,0)
