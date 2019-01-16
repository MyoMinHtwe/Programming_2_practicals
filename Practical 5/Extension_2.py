names = []
dobs = []
for i in range (3):
    name = input("Enter your name: ")
    names.append(name)
    dob = input("Enter your date of birth (dd/mm/yy): ")
    dobs.append(dob)
name_to_dob = dict(zip(names, dobs))
print(name_to_dob)