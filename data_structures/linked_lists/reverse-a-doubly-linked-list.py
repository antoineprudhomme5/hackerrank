"""
 Reverse a doubly linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list
"""
def Reverse(head):
    temp = head
    newHead = head
    while temp is not None:
        prev = temp.prev
        temp.prev = temp.next
        temp.next = prev
        newHead = temp
        temp = temp.prev
    return newHead
