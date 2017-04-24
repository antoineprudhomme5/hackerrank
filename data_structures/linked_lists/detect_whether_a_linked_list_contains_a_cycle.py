def has_cycle(head):
    curr = head
    while curr.next != None:
        if curr.next.next == curr:
            return True
        curr = curr.next
    return False