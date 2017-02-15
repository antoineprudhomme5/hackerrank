# for each test case
for _ in range(int(input())):
    s = input()
    answ = -1
    len_s = len(s)

    for i in range(len_s // 2):
        mirror_i = len_s - i - 1
        # differents
        if s[i] != s[mirror_i]:
            # which one remove ? check neighbors
            answ = i if s[i+1] == s[mirror_i] and s[i+2] == s[mirror_i - 1] else mirror_i
            break

    print(answ)
