def find_in_list(l, v):
    for i in range(len(l)):
        if l[i] == v:
            return True
    return False

n, d = list(map(int, input().split()))
counter = 0
numbers = list(map(int, input().split()))
for i in range(n-2):
    if find_in_list(numbers, numbers[i] + d) and find_in_list(numbers, numbers[i] + 2*d):
        counter += 1
print(counter)