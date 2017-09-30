from collections import Counter
input()
counter = Counter(list(map(int, input().split())))
print(counter.most_common(1)[0][0])
