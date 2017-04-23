def RemoveDuplicates(head):
    d = {}
    prev = head
    curr = prev.next
    d[prev.data] = 1
    while curr != None:
        if curr.data in d:
            prev.next = curr.next
        else:
            d[curr.data] = 1
            prev = prev.next
        curr = curr.next
    return head