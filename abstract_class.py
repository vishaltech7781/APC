from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    def wheel(self):
        pass

class car(vehicle):
    def wheel(self):
        print("the car has the 4 wheels")

class bike(vehicle):
    def wheel(self):
        print("bike has only 2 wheels")

b = bike()
c = car()

c.wheel()
b.wheel()