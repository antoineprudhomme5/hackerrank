def are_balanced_brackets(expression):
    match_table = {'(': ')', '[': ']', '{': '}'}
    open_brackets = match_table.keys()
    stack = []
    for b in expression:
        if b in open_brackets:
            stack.append(b)
        elif len(stack) == 0 or match_table[stack.pop()] != b:
            return False

    return True if len(stack) == 0 else False

for _ in range(int(input().strip())):
    print("YES" if are_balanced_brackets(input().strip()) else "NO")
