from operator import itemgetter

queue = []
for i in range(int(input())):
    ti, di = map(int, input().split())
    queue.append((i+1, ti+di))
queue = sorted(queue, key=itemgetter(1))

print(' '.join([str(item[0]) for item in queue]))
