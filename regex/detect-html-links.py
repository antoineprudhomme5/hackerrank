import re

for _ in range(int(input())):
    matches = re.findall(r'<a href="(.*?)".*?>([\w ,./]*)(?=</)', input().strip())
    # print only if a link has been find in this row
    if matches:
        for link, title in matches:
            print("{},{}".format(link, title.strip()))
