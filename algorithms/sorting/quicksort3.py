n = int(input())
a = list(map(int, input().split()))

def quicksort(a, lo, hi):
    if lo < hi:
        p = partition(a, lo, hi)
        print(' '.join([str(x) for x in a]))
        quicksort(a, lo, p-1)
        quicksort(a, p+1, hi)

def partition(a, lo, hi):
    pivot = a[hi]
    i = lo - 1
    for j in range(lo, hi):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[hi] = a[hi], a[i+1]
    return i + 1

quicksort(a, 0, n-1)
