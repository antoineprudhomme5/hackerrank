import math

def str_to_dic(s):
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d

# for each test case
for _ in range(int(input())):
    s = input()
    if len(s) % 2 == 0:
        s1, s2 = s[:len(s)//2], s[len(s)//2:]
        # make a dict for each string
        d1, d2 = str_to_dic(s1), str_to_dic(s2)
        # compare
        counter = 0
        for k, v in d1.items():
            if k in d2:
                if v > d2[k]:
                    counter += v - d2[k]
            else:
                counter += v
        # print the nb of letters to change
        print(int(counter))
    else:
        print('-1')
