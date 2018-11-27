MIN_NUMBER = 33
MAX_NUMBER = 127

def get_number (MIN_NUMBER, MAX_NUMBER):
    while True:
        try:
            num = int(input("Enter a number {}-{}: ".format(MIN_NUMBER,MAX_NUMBER)))
            if num >= MIN_NUMBER and num<= MAX_NUMBER:
                return num
        except ValueError:
            print("Please enter a number: ")

def main():
    character = input("Enter a character: ")
    print("The ASCII code for {} is {}".format(character, ord(character)))
    num = get_number(MIN_NUMBER, MAX_NUMBER)
    print("The character for {} is {}".format(num, chr(num)))
    ask = input("Do you want to print ASCII table? Yes or No. ").lower()
    if ask[0]=="y":
        print("\nASCII Table")
        for i in range (33,127):
            print("{:>3}    {}".format(i,chr(i)))
main()

