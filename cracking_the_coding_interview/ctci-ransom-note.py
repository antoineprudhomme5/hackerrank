def list_to_hashtable(a):
    h = {}
    for w in a:
        if w in h:
            h[w] += 1
        else:
            h[w] = 1
    return h

def can_ransom_note(magazine, ransom):
    h_m = list_to_hashtable(magazine)
    h_r = list_to_hashtable(ransom)

    for w in h_r:
        if (w not in h_m) or (h_m[w] < h_r[w]):
            return False

    return True

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')

print("Yes" if can_ransom_note(magazine, ransom) else "No")
