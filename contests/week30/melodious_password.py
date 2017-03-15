vowels = "aeiou"
consonants = "zrtpmlkjhgfdsqwxcvbn"

end_with_vowel = list(vowels)
end_with_consonant = list(consonants)

password_length = int(input())

# probleme :
# exemple avec "hah" => termine par consonne donc peut recevoir voyelle à la fin. Mais peut aussi recevoir devant !!

while password_length > 1:

    new_end_with_vowel = []
    new_end_with_consonant = []

    for v in vowels:
        for i in range(len(end_with_consonant)):
            new_end_with_vowel.append(end_with_consonant[i] + v)
    
    for c in consonants:
        for i in range(len(end_with_vowel)):
            new_end_with_consonant.append(end_with_vowel[i] + c)

    end_with_consonant = new_end_with_consonant
    end_with_vowel = new_end_with_consonant
    password_length -= 1

[print(w) for w in end_with_consonant]
[print(w) for w in end_with_vowel]