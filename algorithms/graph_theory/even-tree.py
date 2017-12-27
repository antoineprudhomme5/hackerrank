import sys
from collections import deque

class Node(object):
    def __init__(self, index):
        self.parent = None
        self.index = index
        self.children = []
        # weight = total number of nodes from this node
        self.weight = 1

class Graph(object):
    def __init__(self, nb_nodes):
        self.nodes = {}
        for i in range(nb_nodes):
            self.nodes[i+1] = Node(index=i+1)

    def add_edge(self, child, parent):
        if child < parent:
            child, parent = parent, child
        self.nodes[parent].children.append(child)
        self.nodes[child].parent = parent

    def _find_leafs(self):
        leafs = []
        # use bfs to find leafs
        q = deque()
        q.append(1)
        visited = {}

        while len(q):
            current = self.nodes[q.popleft()]
            if len(current.children):
                for child in current.children:
                    if child not in visited:
                        visited[child] = True
                        q.append(child)
            else:
                leafs.append(current.index)

        return leafs

    def solve(self):
        visited = {}
        leafs_idx = self._find_leafs()

        while len(leafs_idx):
            new_leafs_idx = []
            for leaf_idx in leafs_idx:
                leaf = self.nodes[leaf_idx]

                if leaf.parent:
                    self.nodes[leaf.parent].weight += leaf.weight

                if leaf.parent and leaf.parent not in visited:
                    visited[leaf.parent] = True
                    new_leafs_idx.append(leaf.parent)

            leafs_idx = new_leafs_idx

        return sum(1 for k, v in self.nodes.items() if v.parent != None and v.weight % 2 == 0)

n, m = map(int, input().split())
g = Graph(n)
for _ in range(m):
    i, j = map(int, input().split())
    g.add_edge(i, j)
print(g.solve())
