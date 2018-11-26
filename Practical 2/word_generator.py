import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
ALPHABETS = "bcdfghjklmnpqrstvwxyzaeiou"

word_format = input("""Enter word format such as 'ccvcvvc'. 
c or % for consonants.
v or #for vowels. 
* for either"""+"\n")
word = ""
for kind in word_format:
    if kind == "c" or kind =="%":
        word += random.choice(CONSONANTS)
    elif kind == "#" or kind == "v":
        word += random.choice(VOWELS)
    elif kind == "*":
        word += random.choice (ALPHABETS)
    else:
        word += kind

print(word)