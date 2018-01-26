""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check(root, min_v, max_v):
    if root == None:
        return True
    if root.data < min_v or root.data > max_v:
        return False
    return check(root.left, min_v, root.data) and check(root.right, root.data, max_v)

def check_binary_search_tree_(root):
    return check(root, 0, float("+Inf"))
