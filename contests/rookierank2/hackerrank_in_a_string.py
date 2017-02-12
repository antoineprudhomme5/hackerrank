hackerrank = "hackerrank"
last_index = len(hackerrank) - 1

for _ in range(int(input())):
    i = 0
    for c in input():
        if hackerrank[i] == c:
            i += 1
        if i > last_index:
            print("YES")
            break
    if i <= last_index:
        print("NO")