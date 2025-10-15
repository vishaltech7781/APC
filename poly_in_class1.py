# Parent class
class Vehicle:
    def start(self):
        print("Vehicle is starting")

# Child class Car
class Car(Vehicle):
    def start(self):
        print("Car is starting")

# Child class Bike
class Bike(Vehicle):
    def start(self):
        print("Bike is starting")
# different method for creating the object and running the method using the objects
# # Using polymorphism
# vehicles = [Vehicle(), Car(), Bike()]

# for v in vehicles:
#     v.start()

c = Car()
b = Bike()

c.start()
b.start()
