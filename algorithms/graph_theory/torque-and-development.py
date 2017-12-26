from collections import deque

def dfs(n, visited, graph):
    visited[n] = True
    size = 1

    for c in graph[n]:
        if not visited[c]:
            child_size, visited =  dfs(c, visited, graph)
            size += child_size

    return size, visited

def find_connected_components_sizes(graph, nb_nodes):
    connected_components_sizes = []

    visited = {}
    for i in range(nb_nodes):
        visited[i] = False

    for i in range(nb_nodes):
        if not visited[i]:
            size, visited = dfs(i, visited, graph)
            connected_components_sizes.append(size)

    return connected_components_sizes

for _ in range(int(input())):
    n, m, c_lib, c_road = map(int, input().split())

    graph = {}
    cost = 0

    # init nodes
    for i in range(n):
        graph[i] = []

    # init edges
    for _ in range(m):
        i, j = map(int, input().split())
        graph[i-1].append(j-1)
        graph[j-1].append(i-1)

    # if it cost less to build lib than fix a road, build libs
    if c_lib <= c_road:
        cost = n*c_lib
    else:
        # find all connected components
        connected_components_sizes = find_connected_components_sizes(graph, n)
        # calculate the min cost for each connected component
        for connected_component_size in connected_components_sizes:
            # as a lib cost more that a road, we need a lib for each
            # connected component and roads to connect each node of this
            # connected component (= n-1 roads for for n nodes)
            cost += c_lib + (connected_component_size-1)*c_road

    print(cost)
