from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    def wheel(self):
        pass
    @abstractmethod
    def type(self):
        pass

class car(vehicle):
    def wheel(self):
        print("the car has the 4 wheels")
    def type(self):
        print("type of the vehicle is car")

class bike(vehicle):
    def wheel(self):
        print("bike has only 2 wheels")
    def type(self):
        print("type of the vehicle is bike")

b = bike()
c = car()

c.wheel()
c.type()
b.wheel()
b.type()