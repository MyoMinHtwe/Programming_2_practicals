def add_column():
    column = int(input("How many columns do you want to print? "))
    print("\nASCII table ({} columns)".format(column))
    for i in range (33, 127):
        print(("{:3}{:>2s}   ".format(i, chr(i)))* column)
add_column()