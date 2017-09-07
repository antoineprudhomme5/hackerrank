class MyHeap:
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

    def swapp(self, i, j):
        self.values[i], self.values[j] = self.values[j], self.values[i]

    def insert(self, v):
        self.values.append(v)
        self.up_inserted_value()

    def extract(self):
        self.swapp(0, len(self.values) - 1)
        extracted = self.values.pop()
        self.down_top_value()
        return extracted

    def peek(self):
        return self.values[0]

    def down_top_value(self):
        value_index = 0
        left_child = self.left_child(value_index)
        while len(self.values) > left_child:
            smallest_child = left_child
            right_child = self.right_child(value_index)
            if len(self.values) > right_child and self.values[right_child] < self.values[left_child]:
                smallest_child = right_child

            if self.values[value_index] < self.values[smallest_child]:
                break

            self.swapp(value_index, smallest_child)
            value_index = smallest_child
            left_child = self.left_child(value_index)

    def up_inserted_value(self):
        inserted_index = len(self.values) - 1
        parent_index = self.parent(inserted_index)
        while parent_index >= 0 and self.values[parent_index] > self.values[inserted_index]:
            self.swapp(inserted_index, parent_index)
            inserted_index = parent_index
            parent_index = self.parent(inserted_index)

heap = MyHeap()
nb_cookies, sweetness = list(map(int, input().split()))
for cookie in list(map(int, input().split())):
    heap.insert(cookie)

operations_count = 0

# increase cookies sweetness
while sweetness > heap.peek():
    if heap.size() < 2:
        operations_count = -1
        break

    c1 = heap.extract()
    c2 = heap.extract()
    new_cookie = c1 + 2*c2
    heap.insert(new_cookie)
    operations_count += 1

print(operations_count)
