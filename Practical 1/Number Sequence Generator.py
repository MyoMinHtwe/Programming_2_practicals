num1=int(input("Enter a number: "))
num2=int(input("Enter another number: "))
num3=num2+1
menu="""1 - Show the even numbers from x to y
2 - Show the odd numbers from x to y
3 - Show the squares from x to y
4 - Exit the program"""
print(menu)
choice=input(">>> ")
while choice!="4":
    if choice=="1":
        for i in range(num1, num3):
            if i%2 ==0:
                print(i, end=" ")
    elif choice=="2":
        for i in range(num1, num3):
            if i%2==1:
                print(i, end=" ")
    elif choice=="3":
        for i in range(num1, num3):
            print(i**2, end=" ")
    else:
        print("Invalid choice")
    print("\n")
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    num3 = num2+1
    print(menu)
    choice=input(">>> ")
print("Thank you")