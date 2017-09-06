import queue

class Node:
    def __init__(self, index):
        self.neighbors = []
        self.index = index
        self.visited = False

class Graph:
    def __init__(self, size = 0):
        self.nodes = {}
        self.size = size
        self.init_nodes()

    def init_nodes(self):
        for i in range(1, self.size + 1):
            self.nodes[i] = Node(i)

    def connect(self, x, y):
        self.nodes[x].neighbors.append(y)
        self.nodes[y].neighbors.append(x)

    def find_all_distances(self, s):
        # init dic with all node as key
        distances = {}
        for i in range(self.size):
            distances[i+1] = -1
        distances.pop(s, None)

        # do BFS starting from the given node
        currQueue = queue.Queue() # nodes of the current level
        nextQueue = queue.Queue() # nodes of the next level
        currQueue.put(s)
        self.nodes[s].visited = True
        level = 0
        while not currQueue.empty() or not nextQueue.empty():
            if currQueue.empty():
                level += 1;
                currQueue = nextQueue
                nextQueue = queue.Queue()

            curr = self.nodes[currQueue.get()]
            if curr.index in distances:
                distances[curr.index] = 6 * level
            # enqueue neighbors that are not already visited
            for neighbor in curr.neighbors:
                if not self.nodes[neighbor].visited:
                    nextQueue.put(self.nodes[neighbor].index)
                    self.nodes[neighbor].visited = True

        # return distances
        return " ".join(list(map(str, distances.values())))

# for each test case
for _ in range(int(input())):
    nb_nodes, nb_edges = [int(value) for value in input().split()]
    # init the graph
    graph = Graph(nb_nodes)
    # reach the edges
    for i in range(nb_edges):
        x, y = [int(x) for x in input().split()]
        graph.connect(x, y)
    s = int(input())
    print(graph.find_all_distances(s))
