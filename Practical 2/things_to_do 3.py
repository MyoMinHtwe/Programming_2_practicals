MAX_INCREASE = 0.175 # 10%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0

price = INITIAL_PRICE
print("Startin price: ${:,.2f}".format(price))
counter=[]

import random

while price >= MIN_PRICE and price <= MAX_PRICE:
    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    counter.append(price)
    #print("${:.2f}".format(price))

for i in range(len(counter)):
   print("On day {0} price is ${1:.2f}".format(i+1,counter[i]))
print(price)

# out_file=open("OUTPUT_FILE.txt", "a")
# print("${:,.2f}".format(price), file = out_file)
#
# out_file.close()