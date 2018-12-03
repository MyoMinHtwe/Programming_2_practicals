print("""Enter numbers to make a list.
Press a character and enter to make another list""")
print()
def get_list1():
    list1 = []
    while True:
        try:
            num = int(input("Enter a number for the first list: "))
            list1.append(num)
        except ValueError:
            break
    return list1

def get_list2():
    list2 = []
    while True:
        try:
            num = int(input("Enter a number for the second list: "))
            list2.append(num)
        except ValueError:
            break
    return list2

def main():
    list1 = get_list1()
    list2 = get_list2()
    list3 = []
    if len(list2)> len(list1):
        for i in range(len(list2)-len(list1)):
            num = 0
            list3.append(num)
        list1 += list3
    elif len(list1)>len(list2):
        for i in range(len(list1)-len(list2)):
            num = 0
            list3.append(num)
        list2 += list3
    added_list = [x+y for x,y in zip(list1, list2)]
    print("New list:",added_list)
main()
