cents=int(input("Enter cents per kWh: "))
use=float(input("Enter daily use in kWh: "))
days=int(input("Enter number of billing days: "))
estimated=(cents*use*days)/100
print("Estimated bill is $", estimated)