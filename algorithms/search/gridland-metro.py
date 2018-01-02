class Interval(object):
    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2

def merge_intervals(intervals):
    intervals = sorted(intervals, key = lambda x: x.c1)
    stack = [intervals[0]]
    for i in range(1, len(intervals)):
        if stack[len(stack)-1].c2 < intervals[i].c1:
            # if not conflict, push it
            stack.append(intervals[i])
            # else if conflict and intervals[i] end later, merge
        elif stack[len(stack)-1].c2 < intervals[i].c2:
            stack[len(stack)-1].c2 = intervals[i].c2
    return stack

n, m, k = map(int, input().split())
rows = {}
# read tracks
for _ in range(k):
    r, c1, c2 = map(int, input().split())
    if r not in rows:
        rows[r] = []
    rows[r].append(Interval(c1, c2))

import sys

total = n * m
for _, row in rows.items():
    for interval in merge_intervals(row):
        total -= interval.c2 - interval.c1 + 1
print(total)
