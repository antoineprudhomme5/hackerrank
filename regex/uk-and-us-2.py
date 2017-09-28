import re

text = ' '.join([input() for _ in range(int(input()))])
for _ in range(int(input())):
    s = input().replace('our', '(our|or)') + '(?!\S)'
    print(len(re.findall(s, text)))
