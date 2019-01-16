from Practical_8.car import Car
import random

class UnreliableCar(Car):
    def __init__(self, name, fuel):
        super().__init__(name, fuel)
        self.reliability = 50.3



    def drive(self, distance):
        random_number = random.uniform(0,100)
        if random_number > self.reliability:
            print("Not Ok")
            distance = 0
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance

volvo = UnreliableCar("Volvo", 100)


volvo.drive(1)

print(volvo)