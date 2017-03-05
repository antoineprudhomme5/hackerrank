def is_balanced(s):
    brackets = {
        '}': '{',
        ']': '[',
        ')': '('
    }
    opening_brackets = list(brackets.values())
    opened = []
    nb_opened = 0
    # go throught the string
    for c in s:
        # if the charaters is an opening bracket, push it on the stack
        if c in opening_brackets:
            opened.append(c)
            nb_opened += 1
        # if the character is a closing bracket, check the last opened bracket
        elif c in brackets:
            if nb_opened == 0 or opened.pop() != brackets[c]:
                return False
            nb_opened -= 1
    # True if all the opened bracket has been closed
    return not nb_opened

# for each string
for _ in range(int(input())):
    print("YES" if is_balanced(input()) else "NO")