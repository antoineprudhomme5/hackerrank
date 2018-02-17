import sys

class Node:
    def __init__(self, value, depth, parent=None):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None
        self.height = 0
        self.depth = depth

class BST:
    def __init__(self):
        self.root = None
        self.depth = 0

    def insert_value(self, value):
        if self.root == None:
            self.root = Node(value, 0)
        else:
            # Down the tree
            previous = None
            curr = self.root
            depth = 0
            while curr:
                depth += 1
                previous = curr
                # No duplicates !!
                if curr.value == value:
                    return
                curr = curr.left if curr.value > value else curr.right
            # create and add the new Node to the BST
            node = Node(value, depth, previous)
            if value < previous.value:
                previous.left = node
            else:
                previous.right = node
            # update graph's depth
            self.depth = max(depth, self.depth)

    def print_bst(self, attribute="value"):
        current_level = [self.root]
        next_level = []
        while len(current_level):
            print(' '.join([str(getattr(n, attribute)) for n in current_level]), file=sys.stderr)
            for n in current_level:
                if n.left: next_level.append(n.left)
                if n.right: next_level.append(n.right)
            current_level = next_level
            next_level = []

    def find_leaves(self):
        # store leaves by depth
        leaves = {}
        # use BFS to find leaves
        current_level = [self.root]
        next_level = []
        while len(current_level):
            for n in current_level:
                if n.left: next_level.append(n.left)
                if n.right: next_level.append(n.right)
                if not n.left and not n.right:
                    if n.depth not in leaves:
                        leaves[n.depth] = []
                    leaves[n.depth].append(n)
            current_level = next_level
            next_level = []
        return leaves

    def calculate_total_height(self):
        # we start with the leaves of the last level, not all the leaves !!!
        #
        # total = sum of the height of all the nodes
        # visited = nodes already visited
        # leaves = nodes without children in the tree
        # current_depth = level to analyse
        # current_level = nodes of the level to analyse
        # next_level = nodes to analyse in the next level
        total = 0
        visited = {}
        leaves = self.find_leaves()
        current_depth = self.depth
        current_level = leaves[current_depth]
        next_level = []

        while len(current_level):
            for n in current_level:
                if n.depth == current_depth:
                    print("- %d" % (n.value), file=sys.stderr)
                    if n.parent and n.parent.value not in visited:
                        visited[n.parent.value] = True
                        next_level.append(n.parent)
                    if n.left:
                        n.height = n.left.height + 1
                    if n.right and (n.right.height+1) > n.height:
                        n.height = n.right.height + 1
                    total += n.height
            current_depth -= 1
            current_level = next_level
            if current_depth in leaves:
                current_level += leaves[current_depth]
            next_level = []

        return total

if __name__ == '__main__':
    # read inputs and build the tree
    n = int(input())
    bst = BST()
    for v in list(map(int, input().split())):
        bst.insert_value(v)
    # calculate the height of each node and keep track of the total
    total = bst.calculate_total_height()
    # print the result
    print(bst.root.height)
    print(total)
