class Node(object):
    def __init__(self):
        self.parent = None
        self.weight = 1

n, m = map(int, input().split())

nodes = [Node() for _ in range(n)]
for _ in range(m):
    child, parent = map(int, input().split())
    child, parent = child-1, parent-1
    # insert the child and set weights of parents
    nodes[child].parent = nodes[parent]
    p = nodes[parent]
    while p:
        p.weight += 1
        p = p.parent

print(sum(1 for node in nodes if node.parent != None and node.weight % 2 == 0))
