import re
print(';'.join(sorted(set.union(*[set(re.findall(r'<\s*(\w+)', input())) for _ in range((int(input())))]))))
