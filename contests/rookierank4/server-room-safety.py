n = int(input())

x = list(map(int, input().split()))
heights = list(map(int, input().split()))
racks = {}
for i in range(n):
    racks[x[i]] = heights[i]
left_most = x[0]
right_most = x[-1]

fallen_left = [False for _ in range(right_most+1)]
fallen_left[left_most] = True
left_unsafe = True
for i in range(left_most, len(fallen_left)):
    # base case
    if not fallen_left[i] and i in racks:
        left_unsafe = False
        break
    elif fallen_left[i] and i in racks:
        j = 0
        while (i+1+j) < len(fallen_left) and j < racks[i]:
            fallen_left[i+1+j] = True
            j += 1

fallen_right = [False for _ in range(right_most+1)]
fallen_right[right_most] = True
right_unsafe = True
for i in range(len(fallen_right)-1, 0, -1):
    # base case
    if not fallen_right[i] and i in racks:
        right_unsafe = False
        break
    elif fallen_right[i] and i in racks:
        j = 0
        while (i-1-j) > 0 and j < racks[i]:
            fallen_right[i-1-j] = True
            j += 1

if left_unsafe and right_unsafe:
    print("BOTH")
elif left_unsafe:
    print("LEFT")
elif right_unsafe:
    print("RIGHT")
else:
    print("NONE")
