ALPHABETS = "bcdfghjklmnpqrstvwxyzaeiou"
NUMBERS = "1234567890"
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
import random

def get_length():
    while True:
        try:
            length = int(input("Password length (6-10): "))
            return length
        except ValueError:
            print("Entry must be a number.")
def get_upper_case():
    while True:
        upper = input("Do you want upper case? ").lower()
        if upper[0] == "y":
            return upper
        elif upper[0] == "n":
            break
def get_lower_case():
    while True:
        lower = input("Do you want lower case? ").lower()
        if lower[0] == "y":
            return lower
        elif lower [0] == "n":
            break
def get_num():
    while True:
        num = input("Do you want numbers? ").lower()
        if num[0] == "y":
            return num
        elif num[0] == "n":
            break
def get_spcial_char():
    while True:
        special_char = input("Do you want special characters? ").lower()
        if special_char[0] == "y":
            return special_char
        elif special_char [0] == "n":
            break
def main(length, upper, lower,num, special_char):
    password =""
    pool = ""
    if upper == "y":
        pool = ALPHABETS.upper()
    if lower == "y":
        pool = pool+ALPHABETS
    if num == "y":
        pool = pool+NUMBERS
    if special_char == "y":
        pool = pool+SPECIAL_CHARACTERS
    for i in range(length):
        password += random.choice(pool)
    print("Here is your password:", password)
length = get_length()
upper = get_upper_case()
lower = get_lower_case()
num = get_num()
special_char = get_spcial_char()
main(length, upper, lower, num, special_char)