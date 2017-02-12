# for each game of ladybugs
for _ in range(int(input())):
    n = int(input())
    b = input()
    correct = True
    # if b has only one char, it's wrong if this char is not underscore
    if n == 1:
        if b[0] != '_':
            correct = False
    else:
        d = {}
        # put last and first value in the dict
        d[b[0]] = 1
        if b[n-1] == b[0]:
            d[b[0]] += 1
        else:
            d[b[n-1]] = 1
        # check if the first and last indexes are correct
        if b[0] != b[1] or b[n-2] != b[n-1]:
            correct = False
        # loop on the other values
        for i in range(1, n-1):
            # put it in the dict
            if b[i] in d:
                d[b[i]] += 1
            else:
                d[b[i]] = 1
            # check if correct
            if b[i] != '_':
                if b[i-1] != b[i] and b[i+1] != b[i]:
                    correct = False
        
        # if false but it's possible to switch letters
        if correct == False and '_' in d and d['_'] >= 1:
            correct = True
            for k, v in d.items():
                if k != '_' and v == 1:
                    correct = False
                    break

    print('YES' if correct else 'NO')