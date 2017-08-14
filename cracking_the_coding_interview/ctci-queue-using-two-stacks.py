class MyQueue(object):
    def __init__(self):
        self.newestOnTop = []
        self.oldestOnTop = []

    def peek(self):
        self._digest()
        return self.oldestOnTop[-1]

    def pop(self):
        self._digest()
        self.oldestOnTop.pop()

    def put(self, value):
        self.newestOnTop.append(value)

    def _digest(self):
        if len(self.oldestOnTop) == 0:
            while self.newestOnTop:
                self.oldestOnTop.append(self.newestOnTop.pop())


queue = MyQueue()
for _ in range(int(input())):
    values = list(map(int, input().split()))
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
