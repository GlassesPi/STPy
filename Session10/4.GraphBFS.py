from math import inf
class Graph:
    def __init__(self, v, e):
        self.vertices = v
        self.edges = e
    def bfs(self, root):
        self.vertices[root].is_visited = True
        self.vertices[root].distance = 0
        queue = [root]
        while len(queue) > 0:
            u = queue.pop(0)
            for v in self.edges[u]:
                if not self.vertices[v].is_visited:
                    self.vertices[v].is_visited = True
                    self.vertices[v].distance = self.vertices[u].distance + 1
                    queue.append(v)
            print('{} is visited with distance {}'.format(self.vertices[u].key, self.vertices[u].distance))

class Node:
    def __init__(self, k):
        self.key = k
        self.is_visited = False
        self.distance = inf

vertex = [Node('Tehran'),Node('Mazandaran'),Node('Qom'),Node('Kashan'),Node('Markazi'),Node('Isfahan'),]
edge = [[1,2], [0], [0, 3, 4], [2, 5], [2], [3]]
g = Graph(vertex, edge)
g.bfs(root=0)