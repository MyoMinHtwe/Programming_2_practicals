import random
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
ALPHABETS = "bcdfghjklmnpqrstvwxyzaeiou"

word_format = input("""Enter word format such as 'ccvcvvc'.
c for consonants.
v for vowels."""+"\n").lower()

def main(word_format):
    while not is_valid_format(word_format):
        print("Format is invalid.")
        word_format = input("""Enter word format such as 'ccvcvvc'.
c for consonants.
v for vowels."""+"\n")

    print("Format is valid.")

    if create_word(word_format):
        print("Generated word: ", create_word(word_format))

def is_valid_format(word_format):
    word=""
    for kind in word_format:
        if kind =="c":
            word += kind
        elif kind =="v":
            word += kind
    if word_format == word:
        return True
    else:
        return False

def create_word(word_format):
    word = ""
    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        elif kind == "v":
            word += random.choice(VOWELS)
    return word

main(word_format)



