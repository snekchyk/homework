class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Vehicle: {self.make} {self.model}")

class Car(Vehicle):
    def drive(self):
        print(f"The car {self.make} {self.model} is driving.")

class Motorcycle(Vehicle):
    def drive(self):
        print(f"The motorcycle {self.make} {self.model} is driving.")

class Bicycle(Vehicle):
    def drive(self):
        print(f"The bicycle {self.make} {self.model} is riding.")

car = Car("Toyota", "Corolla")
motorcycle = Motorcycle("Yamaha", "MT-07")
bicycle = Bicycle("Giant", "Escape 3")

car.display_info()
car.drive()

motorcycle.display_info()
motorcycle.drive()

bicycle.display_info()
bicycle.drive()
