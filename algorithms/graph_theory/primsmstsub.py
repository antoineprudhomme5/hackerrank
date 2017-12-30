import sys

class Node(object):
    def __init__(self):
        self.parent = None
        self.connections = {}

n, m = map(int, input().split())
# init each node
graph = {}
for i in range(n):
    graph[i+1] = Node()
# add connections
for _ in range(m):
    x, y, r = map(int, input().split())
    graph[x].connections[y] = r
    graph[y].connections[x] = r

# init costs
costs = {}
for i in range(n):
    costs[i+1] = float('+Inf')
# read start node
start = int(input())
costs[start] = 0

# prim's algorithm
visited = {}
q = sorted(list(costs.keys()), key=lambda x: costs[x])
while len(q):
    u = q.pop(0)
    visited[u] = True

    for node, weight in graph[u].connections.items():
        if node not in visited and costs[node] > weight:
            graph[node].parent = u
            costs[node] = weight

    q = sorted(q, key=lambda x: costs[x])

print(sum(costs[cost] for cost in costs.keys()))
