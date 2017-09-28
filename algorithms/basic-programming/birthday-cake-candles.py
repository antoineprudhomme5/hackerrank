from collections import Counter
input()
counter = Counter(list(map(int, input().split())))
print(counter[max(counter.keys())])
