def ReversePrint(head):
    stack = []
    t = head
    while t != None:
        stack.append(str(t.data))
        t = t.next
    stack.reverse()
    [print(v) for v in stack]
