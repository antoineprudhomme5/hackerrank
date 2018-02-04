import sys

n = int(input())
arr = list(map(int, input().split()))


def insertion_sort(arr, n):
    global insertion_sort_shifts
    for i in range(n):
        v = arr[i]
        j = i

        while j > 0 and arr[j-1] > v:
            arr[j] = arr[j-1]
            j -= 1
            insertion_sort_shifts += 1

        insertion_sort_shifts += 1
        arr[j] = v

    return arr

class Insertion:
    def __init__(self):
        self.count = 0
    def sort(self, arr, n):
        for i in range(n):
            v = arr[i]
            j = i
            while j > 0 and arr[j-1] > v:
                self.count += 1
                arr[j] = arr[j-1]
                j -= 1
            arr[j] = v
        return arr

class Quicksort:
    def __init__(self):
        self.count=0
    def swap(self,b,c,d):
        temp=b[c]
        b[c]=b[d]
        b[d]=temp
        return b
    def partition(self,a,s,e):
        pivot=e
        pindex=s
        for i in range(s,e):
            if a[i]<=a[pivot]:
                self.swap(a,i,pindex)
                self.count+=1
                pindex+=1
        self.count+=1
        self.swap(a,pindex,pivot)
        return pindex
    def sort(self,a,s,e):
        if s<e:
            pIndex=self.partition(a,s,e)
            self.sort(a, s, pIndex-1)
            self.sort(a, pIndex+1, e)
        return self.count

quicksort = Quicksort()
quicksort.sort(arr[:], 0, n-1)

insertion = Insertion()
insertion.sort(arr[:], n)

print("%d %d" % (insertion.count, quicksort.count), file=sys.stderr)
print(insertion.count - quicksort.count)
