def calc_price():
    item=int(input("Number of items: "))
    #print(item)
    itemlist=[]
    for i in range(item):
        price = float(input("Price of item: "))
        itemlist.append(price)
        print(itemlist)
    total = sum(itemlist)
    if total>100:
        discount = total*0.10
        discount_price = total-discount
        print("Total price for", item,"is $",discount_price)
    else:
        print("Total price for", item, "is $", total)
calc_price()