vowels = "aeiou"
consonants = "zrtpmlkjhgfdsqwxcvbn"

end_with_vowel = list(vowels)
end_with_consonant = list(consonants)

password_length = int(input())

while password_length > 1:

    new_end_with_vowel = []
    new_end_with_consonant = []

    if password_length > 1 and password_length % 2 == 1:

        for v in vowels:
            for i in range(len(end_with_consonant)):
                new_end_with_vowel.append(end_with_consonant[i] + v)
                new_end_with_consonant.append(v + end_with_consonant[i])
        
        for c in consonants:
            for i in range(len(end_with_vowel)):
                new_end_with_consonant.append(end_with_vowel[i] + c)
                new_end_with_vowel.append(c + end_with_vowel[i])

    else :

        for v in vowels:
            for i in range(len(end_with_consonant)):
                new_end_with_vowel.append(end_with_consonant[i] + v)
        
        for c in consonants:
            for i in range(len(end_with_vowel)):
                new_end_with_consonant.append(end_with_vowel[i] + c)

    end_with_consonant = new_end_with_consonant
    end_with_vowel = new_end_with_consonant
    password_length -= 1

all = set(end_with_consonant + end_with_vowel)
[print(w) for w in all]