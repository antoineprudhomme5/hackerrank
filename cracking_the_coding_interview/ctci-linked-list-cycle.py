def has_cycle(head):
    if head:
        turtle = head
        rabbit = head.next
        while rabbit and rabbit.next:
            if turtle == rabbit:
                return True
            turtle = turtle.next
            rabbit = rabbit.next.next

    return False
