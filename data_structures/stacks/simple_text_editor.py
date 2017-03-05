def read_query():
    query = list(input().strip().split())
    if len(query) == 1:
        return query[0], None
    return query[0], query[1]

previous = []
s = ""
# for each query
for _ in range(int(input())):
    q, p = read_query()
    # save state
    if q == '1' or q == '2':
        previous.append(s)
    # handle query
    if q == '1':
        s += p
    elif q == '2':
        s = s[:-int(p)]
    elif q == '3':
        print(s[int(p) - 1])
    else:
        s = previous.pop()