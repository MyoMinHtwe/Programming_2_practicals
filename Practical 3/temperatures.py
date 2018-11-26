MENU = """C - Convert Celsius to Fahreneit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input("Input your choice: ").lower()
def main(choice):
    #choice = input("Input your choice: ").lower()
    print(choice)
    i = True
    while i==True:
        if choice == "c":
            celsius = float(input("Celsius: "))
            result = calc_celsius(celsius)
            print("Result: {:.2f} Fahrenheit".format(result))
            i = False
        elif choice == "f":
            fahrenheit = float(input("Fahrenheit: "))
            result = calc_fahrenheit(fahrenheit)
            print("Result: {:.2f} Celsius".format(result))
            i = False
        elif choice == "q":
            i = False
        else:
            print("Invalid entry: ")
            choice = input("Input your choice: ")
    print("Thank you")

def calc_celsius(celsius):
    result = celsius * 9.0 / 5 + 32
    return result

def calc_fahrenheit(fahrenheit):
    result = 5 / 9 * (fahrenheit - 32)
    return result


main(choice)




