class Node:
    def __init__(self, v):
        self.valie = v
        self.children = []


root = Node(1)
n = Node(3)
root.children.append(Node(2))
root.children.append(n)

n2 = Node(4)
n.children.append(n2)

