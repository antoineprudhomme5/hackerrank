def FindMergeNode(headA, headB):
    currA = headA
    while currA is not None:
        currB = headB
        while currB is not None:
            if currB.next == currA.next:
                return currA.next.data
            currB = currB.next
        currA = currA.next
    return None
