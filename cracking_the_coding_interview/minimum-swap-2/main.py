def find_next_misplaced_index(arr):
    for i, v in enumerate(arr):
        if (v-1) != i:
            return i
    return None

# fail last test case because timeout
# find_next_misplaced_index go through arr too many times ?


def minimum_swaps(arr):
    nb_swaps = 0

    misplaced_index = find_next_misplaced_index(arr)
    while misplaced_index != None:
        v_misplaced = arr[misplaced_index]
        v_to_swap_with = arr[v_misplaced - 1]

        arr[misplaced_index] = v_to_swap_with
        arr[v_misplaced - 1] = v_misplaced

        nb_swaps = nb_swaps + 1
        misplaced_index = find_next_misplaced_index(
            arr) if v_to_swap_with - 1 == misplaced_index else v_to_swap_with - 1

    return nb_swaps
