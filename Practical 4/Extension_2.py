numbers = []
num_format = "Number"
num_of_num = 1
number = float(input("{} {}: ".format(num_format, num_of_num)))
while number >= 0:
    numbers.append(number)
    num_of_num += 1
    number = float(input("{} {}: ".format(num_format, num_of_num)))
print("The first number is", numbers[0])
print("The last number is", numbers[-1])
print("The largest number is", max(numbers))
print("The smallest number is", min(numbers))
print("The average of the number is", sum(numbers)/len(numbers))


