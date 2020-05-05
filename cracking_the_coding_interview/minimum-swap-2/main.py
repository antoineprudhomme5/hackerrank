def minimum_swaps(arr):
    positions = [0] * (len(arr) + 1)
    for i, v in enumerate(arr):
        positions[v] = i

    nb_swaps = 0
    for i in range(len(arr)):
        pos_of_val_that_should_be_at_i = positions[i+1]
        if pos_of_val_that_should_be_at_i != i:
            v1 = arr[i]
            v2 = arr[pos_of_val_that_should_be_at_i]

            arr[i] = v2
            arr[pos_of_val_that_should_be_at_i] = v1

            positions[v1] = pos_of_val_that_should_be_at_i
            positions[v2] = i

            nb_swaps = nb_swaps + 1

    return nb_swaps
