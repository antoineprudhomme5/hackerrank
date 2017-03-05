# read the number of queries
n = int(input())
stack = []
current_max = 0
for _ in range(n):
    query = input().split()
    # push the element on the stack
    if query[0] == '1':
        t = int(query[1])
        if t > current_max:
            current_max = t
        stack.append(t)
    # delete the element at the top
    elif query[0] == '2':
        r = stack.pop()
        if r == current_max:
            current_max = max(stack) if len(stack) else 0
    # print the top element
    else:
        print(current_max)