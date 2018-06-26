numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

req_num = 1
req_low = 1
req_up = 1
req_special = 1

n = int(input())
s = input()

i = 0
while i < len(s) and (req_num or req_low or req_up or req_special):
	if req_num and s[i] in numbers: 
		req_num -= 1
	elif req_low and s[i] in lower_case: 
		req_low -= 1
	elif req_up and s[i] in upper_case: 
		req_up -= 1
	elif req_special and s[i] in special_characters: 
		req_special -= 1
	i += 1

missing = max(req_num + req_low + req_up + req_special, 6 - n)
print(missing)