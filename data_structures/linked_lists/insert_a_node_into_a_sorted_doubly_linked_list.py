def SortedInsert(head, data):
    n = Node()
    n.data = data
    if head == None:
        return n
    if data <= head.data:
        n.next = head
        head.prev = n
        return n

    rest = SortedInsert(head.next, data);
    head.next = rest;
    rest.prev = head;
    return head;
