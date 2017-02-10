h = int(input())
m = int(input())

dic = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty"
}

def integer_to_word(n):
    if n == 1:
        return "one minute"
    elif n == 15:
        return "quarter"
    elif n < 20:
        return dic[n] + " minutes"
    
    return dic[20] + " " + dic[n - 20] + " minutes"

if m == 0:
    time = dic[h] + " o' clock"
elif m == 30:
    time = "half past " + dic[h]
elif m > 30:
    time = integer_to_word(60 - m) + " to " + dic[h+1]
elif m < 30:
    time = integer_to_word(m) + " past " + dic[h]

print(time)