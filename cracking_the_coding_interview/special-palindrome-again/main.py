def compute_triangle_number(n):
    return (n * (n + 1)) / 2


def substr_count(n, s):
    count = 0
    current_char = s[0]
    current_char_count = 0

    for i in range(0, n):
        if s[i] != current_char:
            count += compute_triangle_number(current_char_count)
            current_char = s[i]
            current_char_count = 0
        current_char_count = current_char_count + 1

    count += compute_triangle_number(current_char_count)

    return count
