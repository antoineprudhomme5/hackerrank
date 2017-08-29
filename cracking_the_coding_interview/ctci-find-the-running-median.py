class MinHeap:
    def __init__(self):
        self.values = []

    def size(self):
        return len(self.values)

    def parent(self, i):
        return (i-1)//2

    def left_child(self, i):
        return i*2 + 1

    def right_child(self, i):
        return i*2 + 2

    def insert(self, value):
        self.values.append(value)
        self.heapify_up()

    def swap(self, i, j):
        temp = self.values[i]
        self.values[i] = self.values[j]
        self.values[j] = temp

    # up in the tree the lastest inserted value while lower than his parent
    def heapify_up(self):
        i = len(self.values) - 1
        parent = self.parent(i)
        while parent >= 0 and self.values[parent] > self.values[i]:
            self.swap(parent, i)
            i = parent
            parent = self.parent(i)


    # down in the tree the root value while it's greater than his children
    def heapify_down(self):
        i = 0
        left_child = self.left_child(i)
        while len(self.values) > left_child:
            smallest_child = left_child
            right_child = self.right_child(i)
            if len(self.values) > right_child and self.values[right_child] < self.values[left_child]:
                smallest_child = right_child

            if self.values[i] < self.values[smallest_child]:
                break

            self.swap(i, smallest_child)
            i = smallest_child
            left_child = self.left_child(i)

    # return the value of the root (the min value of the tree)
    def peek(self):
        return self.values[0]

    # remove and return the root of the tree
    # after removing, reheapify the tree
    def pull(self):
        root = self.values[0]
        self.values[0] = self.values.pop()
        self.heapify_down()
        return root

    def show(self):
        print(self.values)

class MaxHeap:
    def __init__(self):
        self.values = []

    def size(self):
        return len(self.values)

    def parent(self, i):
        return (i-1)//2

    def left_child(self, i):
        return i*2 + 1

    def right_child(self, i):
        return i*2 + 2

    def insert(self, value):
        self.values.append(value)
        self.heapify_up()

    def swap(self, i, j):
        temp = self.values[i]
        self.values[i] = self.values[j]
        self.values[j] = temp

    # up in the tree the lastest inserted value while greater than his parent
    def heapify_up(self):
        i = len(self.values) - 1
        parent = self.parent(i)
        while parent >= 0 and self.values[parent] < self.values[i]:
            self.swap(parent, i)
            i = parent
            parent = self.parent(i)

    # down in the tree the root value while it's lower than his children
    def heapify_down(self):
        i = 0
        left_child = self.left_child(i)
        while len(self.values) > left_child:
            biggest_child = left_child
            right_child = self.right_child(i)
            if len(self.values) > right_child and self.values[right_child] > self.values[left_child]:
                biggest_child = right_child

            if self.values[i] > self.values[biggest_child]:
                break

            self.swap(i, biggest_child)
            i = biggest_child
            left_child = self.left_child(i)

    # return the value of the root (the min value of the tree)
    def peek(self):
        return self.values[0]

    # remove and return the root of the tree
    # after removing, reheapify the tree
    def pull(self):
        root = self.values[0]
        self.values[0] = self.values.pop()
        self.heapify_down()
        return root

    def show(self):
        print(self.values)

# create the 2 heaps
higher = MinHeap()
lower = MaxHeap()

median = 0

# foreach number to insert
for i in range(int(input())):

    # read the new value
    v = int(input())

    # insert the new value in one of the heap (depending of the median)
    if v < median:
        # the value is lower than the median
        lower.insert(v)
    else:
        # the value is greater than the median
        higher.insert(v)

    # balancing
    if higher.size() - lower.size() > 1:
        # if there are more values bigger than the median, put the first value
        # after the median in the lower values
        lower.insert(higher.pull())
    if lower.size() - higher.size() > 1:
        # if there are more values lower than the median, put the first values
        # before the median in the bigger values
        higher.insert(lower.pull())

    # calculate the new median
    if i % 2 == 0:
        # if an odd number of elements has been added, one heap should have more elements than the other
        # print the value of the root of the longest heap
        median = higher.peek() if higher.size() > lower.size() else lower.peek()
    else:
        # if an even number of elements has been added, the number of elements of each
        # heap must be equivalent. Take the average of the 2 closest to the median (average of the roots of each heap)
        median = (higher.peek() + lower.peek()) / 2

    print(float(median))
