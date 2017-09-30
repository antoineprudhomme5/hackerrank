import re
# href=\"(.*)\">([\w\s\.]+)
[print(','.join(list(re.findall(r'href=\"(.*)\".*>([\w\s\.]+)<', input())[0]))) for _ in range(int(input()))]
