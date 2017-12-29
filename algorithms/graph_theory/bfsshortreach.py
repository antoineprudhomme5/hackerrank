from collections import deque

def BFS(graph, s, n):
    # by default, each node is unreachable (-1)
    distances = {}
    for i in range(n):
        distances[i+1] = -1

    visited = {s: True}
    q = deque()
    next_q = deque()
    q.append(s)
    current_depth = 1
    # continue while the queue is not empty
    while len(q):
        current = q.popleft()
        for child in graph[current]:
            # if this child hasn't been visited
            if child not in visited:
                visited[child] = True
                next_q.append(child)
                # set the shortest distance from start to this node
                distances[child] = current_depth*6

        # if current depth level is done, switch to the next level
        if len(q) == 0:
            current_depth += 1
            q = next_q
            next_q = deque()

    return distances


for _ in range(int(input())):
    n, m = map(int, input().split())

    # init the graph
    graph = {}
    for i in range(n):
        graph[i+1] = []
    # read each edge and set the graph
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # calculate distances from start to each nodes, using BFS
    start = int(input())
    distances = BFS(graph, start, n)

    print(' '.join([str(distances[i+1]) for i in range(n) if (i+1) != start]))
