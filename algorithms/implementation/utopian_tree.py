# n cycle, 2 cycles in a year :
# 1: spring : *2
# 2: summer : +1
def tree_height(n):
    h = 1
    for _ in range(n // 2):
        h = h*2 + 1
    return h if n % 2 == 0 else h*2

for _ in range(int(input())):
    print(tree_height(int(input())))