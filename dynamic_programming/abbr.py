"""
RULES
- capitalize letters
- remove all lowercase letters

SOLUTION 1: NAIVE
generate all possibilities from A using the 2 rules aboves
compare all possibilities with B
if there is a match, return YES
else return NO

a
-> a, A
aB
-> aB, AB
Abc
-> ABc, AbC, ABC, abc
Abcd
-> Abcd, ABcd, AbCd, AbcD, ABCd, ABcD, AbCD, ABCD

O([number of lowercase letters in A]^2)


SOLUTION 2: does not work
A = AkBceE
B = ABE
i -> index to go through A
j -> index to go through B
- loop though A (using i)
  - if A[i] is upper
    - it should match B[j] -> if not, return NO
  - else
    - either we upper it and pick it
    - either we skip it because there is this upper letter after in A
    -> knowing which choise to do is hard: dynamic programming required (solve the subproblem before)


SOLUTION 3: dynamic programming

def get_has_remaining_uppercase_letters(a, i):
  for c in range(i, len(a)):
    if a[c].isupper():
      return True
  return False

def abbreviation_rec(a, b, i, j, lookup):
  if j >= len(b):
    return not get_has_remaining_uppercase_letters(a, i)
  if i >= len(a):
    return False
  
  lookup_key = str(i) + ":" + str(j)
  if not lookup_key in lookup:
    if a[i] == b[j]:
      lookup[lookup_key] = abbreviation_rec(a, b, i+1, j+1, lookup)
    elif a[i].isupper():
      lookup[lookup_key] = False
    elif a[i].upper() != b[j]:
      lookup[lookup_key] = abbreviation_rec(a, b, i+1, j, lookup)
    else:
      r1 = abbreviation_rec(a, b, i+1, j, lookup)
      r2 = abbreviation_rec(a, b, i+1, j+1, lookup)
      lookup[lookup_key] = r1 or r2

  return lookup[lookup_key]

def abbreviation(a, b):
  is_doable = abbreviation_rec(a, b, 0, 0, {})
  return "YES" if is_doable else "NO"
"""

def abbreviation(a, b):
  is_valid = [None] * (len(a) + 1)
  for i in range(len(a) + 1):
    is_valid[i] = [False] * (len(b) + 1)
  
  is_valid[0][0] = True

  contains_uppercase = False
  # init when b is empty
  for i in range(1, len(a)+1):
    end_i = i - 1
    if a[end_i].isupper():
      contains_uppercase = True
    is_valid[i][0] = not contains_uppercase

  # tabulation from start
  for k in range(1, len(a)+1):
    for l in range(1, len(b)+1):
      i = k - 1
      j = l - 1

      if a[i] == b[j]:
        is_valid[k][l] = is_valid[k-1][l-1]
      elif a[i].upper() == b[j]:
        is_valid[k][l] = is_valid[k-1][l-1] or is_valid[k-1][l]
      elif a[i].isupper():
        is_valid[k][l] = False
      else:
        is_valid[k][l] = is_valid[k-1][l]
    
  return "YES" if is_valid[len(a)][len(b)] else "NO"

"""
AkBceE
ABE

sYoOCa
YOCN

sYoOCa
WOCA
"""

# A = "KXzQ"
# B = "K"
# A = "HLWNgBte"
# B = "HLWNB"
# A = "HLWNgBte"
# B = "AHLWNB"
# print(abbreviation(A, B))