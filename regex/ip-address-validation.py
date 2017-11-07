import re
rIPv4 = re.compile('^((25[0-5]|2[0-4][0-9]|[0-1]?[0-9]?[0-9]).){3}(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]?[0-9])$', re.IGNORECASE)
rIPv6 = re.compile('^(([\da-f]{1,4}):){7}([\da-f]{1,4})$', re.IGNORECASE)
for _ in range(int(input())):
    s = input()
    if rIPv4.match(s):
        print('IPv4')
    elif rIPv6.match(s):
        print('IPv6')
    else:
        print('Neither')
