def CompareLists(headA, headB):
    p_a = headA
    p_b = headB
    while p_a is not None or p_b is not None:
        if (p_a is None and p_b is not None) or (p_a is not None and p_b is None) or (p_a.data is not p_b.data):
            return 0
        p_a = p_a.next
        p_b = p_b.next
    return 1