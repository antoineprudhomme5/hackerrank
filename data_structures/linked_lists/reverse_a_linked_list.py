def Reverse(head):
    if head == None:
        return None
    s = []
    t = head
    while t != None:
        s.append(t.data)
        t = t.next
    new_head = Node(s.pop())
    t = new_head
    while len(s):
        t.next = Node(s.pop())
        t = t.next
    return new_head
    