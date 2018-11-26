MIN_NUMBER = 33
MAX_NUMBER = 127
def ascii_finder():
    character = input("Enter a character: ")
    print("The ASCII code for {} is {}".format(character, ord(character)))
    num = int(input("Enter a number between {} and {}: ".format(MIN_NUMBER,MAX_NUMBER)))
    print("The character for {} is {}".format(num, chr(num)))
    ask = input("Do you want to print ASCII table? Yes or No. ").lower()
    if ask[0]=="y":
        print("\nASCII Table")
        for i in range (33,127):
            print("{:>3}    {}".format(i,chr(i)))
ascii_finder()