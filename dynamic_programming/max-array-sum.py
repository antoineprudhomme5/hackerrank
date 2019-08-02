"""
[2, 1, 5, 8, 4]

[2, 1, None, None, None]
[2, 1, None, None, None]
[2, 1, 7, None, None]
[2, 1, 7, 9, None]
[2, 1, 7, 9, 11]

"""

def max_subset_sum(v):
  m = [None] * len(v)

  if len(v) == 1:
    return v[0]
  
  m[0] = v[0]
  m[1] = max(v[0], v[1])

  for i in range(2, len(v)):
    s1 = v[i]
    s2 = m[i-1]
    s3 = v[i] + m[i-2]
    m[i] = max(max(s1, s2), s3)
  return m[-1]  
   