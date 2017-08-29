"""
Solution using heapq module
Store negative values in lower to do a min heap
"""

from heapq import heappush, heappop

# create the 2 heaps
higher = []
lower = []

median = 0

# foreach number to insert
for i in range(int(input())):

    # read the new value
    v = int(input())

    # insert the new value in one of the heap (depending of the median)
    if v < median:
        # the value is lower than the median
        heappush(lower, -1 * v)
    else:
        # the value is greater than the median
        heappush(higher, v)

    # balancing
    if len(higher) - len(lower) > 1:
        # if there are more values bigger than the median, put the first value
        # after the median in the lower values
        heappush(lower, -1 * heappop(higher))

    if len(lower) - len(higher) > 1:
        # if there are more values lower than the median, put the first values
        # before the median in the bigger values
        heappush(higher, -1 * heappop(lower))

    # calculate the new median
    if i % 2 == 0:
        # if an odd number of elements has been added, one heap should have more elements than the other
        # print the value of the root of the longest heap
        median = higher[0] if len(higher) > len(lower) else -1 * lower[0]
    else:
        # if an even number of elements has been added, the number of elements of each
        # heap must be equivalent. Take the average of the 2 closest to the median (average of the roots of each heap)
        median = (higher[0] + (-1 * lower[0])) / 2

    print(float(median))
