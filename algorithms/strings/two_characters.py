import math

n = int(input())
s = input()

d = {}
for c in s:
    if c in d:
        d[c] += 1
    else:
        d[c] = 1

letters = list(d)

# check each pair

len_t = 0
for i in range(len(letters)):
    for j in range(i+1, len(letters)):
        curr_l = 0
        
        # get the letters order, to check if the result string is ok (it alternate)
        idx_i = s.index(letters[i])
        idx_j = s.index(letters[j])
        if idx_i > idx_j:
            first_c = letters[j]
            second_c = letters[i]
            start = idx_j
        else:
            first_c = letters[i]
            second_c = letters[j]
            start = idx_i

        for c in range(start, len(s)):
            # check if the order is correct
            if s[c] == first_c or s[c] == second_c:
                if (curr_l % 2 == 1 and s[c] == second_c) or (curr_l % 2 == 0 and s[c] == first_c):
                    curr_l += 1
                else:
                    curr_l = 0
                    break

        # if the length of 't' with these letter if the best score, save it
        if curr_l > len_t:
            len_t = curr_l

print(len_t)