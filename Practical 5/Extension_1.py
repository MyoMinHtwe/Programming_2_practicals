name_to_dob = {}
for i in range(2):
    key = input("Enter name: ")
    value = input("Enter date of birth (dd/mm/yyyy): ")
    name_to_dob[key] = value
for key, value in name_to_dob.items():
    print("{} date of birth is {:10}".format(key,value))