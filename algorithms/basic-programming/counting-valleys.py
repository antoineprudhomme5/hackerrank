n = int(input())
sequence = input()

valley_counter = 0
# start at see level
curr_level = 1 if sequence[0] == 'U' else -1

for i in range(1, n):
    curr_level += 1 if sequence[i] == 'U' else -1

    if curr_level == 0 and sequence[i] == 'U':
        valley_counter += 1

print(valley_counter)
