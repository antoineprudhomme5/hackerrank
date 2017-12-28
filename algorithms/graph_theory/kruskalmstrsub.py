class Edge(object):
    def __init__(self, x, y, weight):
        self.x = x
        self.y = y
        self.weight = weight

def kruskal(edges, nb_nodes):
    edges = sorted(edges, key=lambda x: x.weight)

    # by default, each nodes is in a different tree
    nodes = {}
    for i in range(nb_nodes):
        nodes[i+1] = i

    # the goal is to have 1 tree at the end
    nb_trees = n
    result = 0
    for edge in edges:
        # if the edge merge 2 trees
        if nodes[edge.x] != nodes[edge.y]:
            result += edge.weight
            nb_trees -= 1

            if nb_trees == 1:
                break

            # do the merge
            temp = nodes[edge.y]
            for k, v in nodes.items():
                if v == temp:
                    nodes[k] = nodes[edge.x]

    return result

n, m = map(int, input().split())

edges = [None]*m
for i in range(m):
    x, y, w = map(int, input().split())
    edges[i] = Edge(x, y, w)

print(kruskal(edges, n))
