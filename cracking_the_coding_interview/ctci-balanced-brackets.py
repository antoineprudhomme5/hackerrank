def are_balanced_brackets(expression):
    match_table = {'(': ')', '[': ']', '{': '}'}
    open_brackets = match_table.keys()
    stack = []
    for b in expression:
        if b in open_brackets:
            stack.append(b)
        else if stack.pop() != match_table[b]:
            return False

    return True

for _ in range(int(input().strip())):
    print("YES" if are_balanced_brackets(input().strip()) else "NO")
