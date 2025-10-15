class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    def start(self):   
        print("Car starts")

c = Car()
c.start()  
