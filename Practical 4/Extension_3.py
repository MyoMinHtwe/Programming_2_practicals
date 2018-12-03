def main():
    string = input("Enter a string: ")
    list_of_string = list()
    while string != "":
        list_of_string.append(string)
        string = input("Enter a string: ")
    repeated_string = set(i for i in list_of_string if list_of_string.count(i)>1)
    if len(repeated_string) >= 1:
        for i in repeated_string:
            print("\"{}: {}\"".format("Strings repeated", i))
    else:
        print("\"No repeated strings entered.\"")

main()