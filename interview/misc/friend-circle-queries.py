def get_root(parents, v):
  root = v
  while root in parents:
    root = parents.get(root)
  return root

def max_circle(queries):
  answers = []
  parents = {}
  sizes = {}
  current_max_size = 1

  for query in queries:
    a, b = query[0], query[1]
    root_a, root_b = get_root(parents, a), get_root(parents, b)
    if root_a == root_b:
      answers.append(current_max_size)
      continue

    size_a = sizes.get(root_a) if root_a in sizes else 1
    size_b = sizes.get(root_b) if root_b in sizes else 1


    parents[root_a] = root_b

    sizes[root_b] = size_a + size_b

    current_max_size = max(size_a + size_b, current_max_size)

    answers.append(current_max_size)

  return answers

# max_circle([[1, 2], [3, 4], [1, 3], [5, 7], [5, 6], [7, 4]])
# max_circle([[1, 2], [3, 4], [1, 3]])
max_circle([[6, 4], [5, 9], [8, 5], [4, 1], [1, 5], [7, 2], [4, 2], [7, 6]])

"""
8
6 4
5 9
8 5
4 1
1 5
7 2
4 2
7 6
"""

"""
2
2
3
3
6
6
8
8
"""