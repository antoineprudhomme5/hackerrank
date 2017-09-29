import re
rgx = re.compile(r"^[_.]\d+[a-z]*_?$", re.IGNORECASE)
for _ in range(int(input())):
    print("VALID" if rgx.match(input()) else "INVALID")
