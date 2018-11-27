import random
STARTING_POPULATION = 1000
print("Welcome to the Gopher Population Simulator")
print("Starting population: {}".format(STARTING_POPULATION))

def birth_rate():
    for i in range(1, 11):
        born = round(random.uniform(0.1, 0.2), 3)*1000
        return born

def death_rate():
    for i in range(1, 11):
        died = round(random.uniform(0.05, 0.25), 3)*1000
        return died

def main():
    population = STARTING_POPULATION
    for i in range(1, 11):
        print("\n")
        print("Year", i,"\n"+"*"*5)
        born = int(birth_rate())
        died = int(death_rate())
        print("{} gophers were born. {} died.".format(born, died))
        remain = born - died
        population = population + remain
        print("Population: {}".format(population))

main()






