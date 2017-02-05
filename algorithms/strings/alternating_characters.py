for _ in range(int(input())):
    s = input()
    current = s[0]
    count = 0
    for i in range(1, len(s)):
        if s[i] == current:
            count += 1
        else:
            current = s[i]
    print(count)