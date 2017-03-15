vowels = "aeiou"
consonants = "zrtpmlkjhgfdsqwxcvbn"

password_length = int(input())
elements = list(vowels) + list(consonants)

if password_length == 1:
    [print(v) for v in elements]    
else:
    i = 1
    while password_length > i:
        new_elements = []
        if i == 1:
            for e in elements:
                if e in vowels:
                    for c in consonants:
                        new_elements.append(e + c)
                else:
                    for v in vowels:
                        new_elements.append(e + v)
        else:
            for e in elements:
                # check first char
                if e[0] in vowels:
                    for c in consonants:
                        new_elements.append(c + e)
                else:
                    for v in vowels:
                        new_elements.append(v + e)
                # check last char
                if e[-1] in vowels:
                    for c in consonants:
                        new_elements.append(e + c)
                else:
                    for v in vowels:
                        new_elements.append(e + v)
        elements = new_elements
        i += 1
    
    [print(e) for e in set(elements)]