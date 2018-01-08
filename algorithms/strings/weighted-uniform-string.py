import sys
import string

s = input()

def prepare(s):
    dic = {}
    for i, c in enumerate(list(string.ascii_lowercase)):
        dic[c] = i+1

    current_weight = 0
    current_char = None
    weights = {}

    for i in range(len(s)):
        if s[i] != current_char:
            current_char = s[i]
            current_weight = dic[current_char]
        else:
            current_weight += dic[current_char]

        weights[current_weight] = True

    return weights

weights = prepare(s)

for _ in range(int(input())):
    x = int(input())
    print("Yes" if x in weights else "No")
