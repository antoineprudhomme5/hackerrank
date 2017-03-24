""" Merge the 2 sorted lists
"""
def MergeLists(headA, headB):
    if headA is not None and headB is not None:
        if headA.data < headB.data:
            headA.next = MergeLists(headA.next, headB)
            return headA
        else:
            headB.next = MergeLists(headA, headB.next)
            return headB
    elif headA is not None:
        return headA
    else:
        return headB
        