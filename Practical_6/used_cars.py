from Practical_6.car import Car
def main():
    my_car = Car("Mercedes", 180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)
    limo = Car("BMW",100)
    print ("fuel =", limo.fuel)
    limo.drive(115)
    print("odo =", limo.odometer)
    print(limo)
main()
