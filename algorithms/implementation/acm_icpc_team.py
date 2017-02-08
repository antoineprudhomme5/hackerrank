def count_topics(p1, p2, m):
    c = 0
    for i in range(m):
        if p1[i] == '1' or p2[i] == '1':
            c += 1
    return c

n, m = list(map(int, input().split()))

people = []

# read the inputs
for _ in range(n):
    people.append(input())

# brute force is ok here (small numbers)
max_topics = 0
counter = 0

for i in range(n-1):
    for j in range(i+1, n):
        nb_topics = count_topics(people[i], people[j], m)
        if nb_topics == max_topics:
            counter += 1
        elif nb_topics > max_topics:
            max_topics = nb_topics
            counter = 1

print(max_topics)
print(counter)