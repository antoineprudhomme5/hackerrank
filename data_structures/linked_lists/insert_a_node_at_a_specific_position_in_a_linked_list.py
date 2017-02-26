"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def InsertNth(head, data, position):
    if position == 0:
        return Node(data, head)

    p = head
    while position > 1:
        position -= 1
        p = p.next

    new_node = Node(data, p.next)
    p.next = new_node
    return head
