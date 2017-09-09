def calculate_max_size(max_side_size, blocks):
    current_size = 1
    used_blocks = 1
    while current_size + 2 <= max_side_size and blocks <= (used_blocks + (current_size + 2)**2):
        current_size += 2
        used_blocks += current_size**2
    return current_size // 2 + 1

for _ in range(int(input())):
    n, m, k = list(map(int, input().split()))

    min_side = min([n, m])

    # if min is even, make it odd
    if min_side % 2 == 0:
        min_side -= 1

    # find the biggest square pyramid we can make
    print(calculate_max_size(min_side, k))
