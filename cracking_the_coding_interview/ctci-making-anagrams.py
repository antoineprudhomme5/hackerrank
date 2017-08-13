import math

def string_to_hashtable(a):
    h = {}
    for c in a:
        if c in h:
            h[c] += 1
        else:
            h[c] = 1
    return h

def number_needed(a, b):
    h_a = string_to_hashtable(a)
    h_b = string_to_hashtable(b)
    counter = 0

    for c in h_a:
        if c in h_b:
            counter += math.fabs(h_a[c] - h_b[c])
        else:
            counter += h_a[c]

    for c in h_b:
        if c not in h_a:
            counter += h_b[c]

    return counter


a = input().strip()
b = input().strip()

print(number_needed(a, b))
