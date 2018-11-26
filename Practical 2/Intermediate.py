finished = False
result = 0
while not finished:
    try:
        num=int(input("Enter a number: "))
        print("You entered an integer.")
        finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", num)