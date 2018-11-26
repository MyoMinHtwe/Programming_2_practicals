DISCOUNT=0.9
num=int(input("Enter number of items: "))
while(num<=0):
    print("Enter a positive number")
    num=int(input("Enter number of items: "))
total=0.0
for i in range(num):
    price=float(input("Enter price of item: "))
    total+=price
    #print("Price= ", price,"Total= ", total)
if total>100:
    total=DISCOUNT*total
print("Total price for",num,"item is $",total)