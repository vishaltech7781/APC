class vehicle:
    def __init__(self,wheel=None,capa=None):
        self.wheel= None
        self.capa = None

class bikes(vehicle):
    def __init__(self,type=None):
        super().__init__()
        self.type = None

    def set_details(self):
        self.wheel = input("enter the number of wheels :")
        self.capa = int(input("enter the capacity of the bike:"))
        self.type = input("enter the type of the bike :")

    def display(self):
        print(f"these is {self.wheel} wheeled {self.type} which has capacity of {self.capa}")
        
class cars(vehicle):
    def __init__(self,type=None):
        super().__init__()
        self.type = None

    def set_details(self):
        self.wheel = input("enter the number of wheels :")
        self.capa = int(input("enter the capacity of the bike:"))
        self.type = input("enter the type of the bike :")

    def display(self):
        print(f"these is {self.wheel} wheeled {self.type} which has capacity of {self.capa}")
    
class buses(vehicle):
    def __init__(self,type=None):
        super().__init__()
        self.type = None

    def set_details(self):
        self.wheel = input("enter the number of wheels :")
        self.capa = int(input("enter the capacity of the bike:"))
        self.type = input("enter the type of the bike :")

    def display(self):
        print(f"these is {self.wheel} wheeled {self.type} which has capacity of {self.capa}")

class trucks(vehicle):
    def __init__(self,type=None):
        super().__init__()
        self.type = None

    def set_details(self):
        self.wheel = input("enter the number of wheels :")
        self.capa = int(input("enter the capacity of the bike:"))
        self.type = input("enter the type of the bike :")

    def display(self):
        print(f"these is {self.wheel} wheeled {self.type} which has capacity of {self.capa}")


b = bikes()
c = cars()
bu = buses()
t = trucks()

b.set_details()
c.set_details()
bu.set_details()
t.set_details()

b.display()
c.display()
bu.display()
t.display()