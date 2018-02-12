n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dic = {}
for a in A:
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1

nb_pairs = 0
for b in B:
    if b in dic and dic[b] > 0:
        dic[b] -= 1
        nb_pairs += 1

print(nb_pairs-1 if nb_pairs == n else nb_pairs+1)
