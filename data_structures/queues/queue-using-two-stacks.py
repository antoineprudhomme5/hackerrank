import sys

class Queue(object):
    def __init__(self):
        self.head = []
        self.tail = []

    def enqueue(self, e):
        self.tail.append(e)

    def _check_empty_head(self):
        if len(self.head) == 0:
            while len(self.tail):
                self.head.append(self.tail.pop())

    def dequeue(self):
        self._check_empty_head()
        return self.head.pop()

    def peek(self):
        self._check_empty_head()
        return self.head[-1]

q = Queue()
for _ in range(int(input())):
    query = list(map(int, input().split()))
    if query[0] == 1:
        q.enqueue(query[1])
    elif query[0] == 2:
        q.dequeue()
    else:
        print(q.peek())
