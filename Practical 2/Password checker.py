"""CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started"""


MIN_LENGTH = 6
MAX_LENGTH = 10
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    # Variable named password is passed to the function named is_valid_password
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))


def is_valid_password(passworder):
    """Determine if the provided password is valid."""
    # TODO: if length is wrong, return False
    if len(passworder)<MIN_LENGTH or len(passworder)>MAX_LENGTH:
        return False
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in passworder:
        # TODO: count each kind of character (use str methods like isdigit)
        if char.islower():
            count_lower+=1
        if char.isupper():
            count_upper+=1
        if char in SPECIAL_CHARACTERS:
            count_special+=1
        if char.isdigit():
            count_digit +=1
    print("lower =", count_lower, "upper= ", count_upper, "special= ", count_special, "number =", count_digit)
    if(count_lower==0 or count_upper==0 or count_special==0 or count_digit==0):
        return False
    # TODO: if any of the 'normal' counts are zero, return False

    # TODO: if special characters are required, then check the count of those
    # and return False if it's zero

    # if we get here (without returning False), then the password must be valid
    return True


main()