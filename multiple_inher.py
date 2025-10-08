class wheel:
    def __init__(self):
        self.shape = None

class rubber:
    def __init__(self):
        self.material = None

class tyre(wheel,rubber):
    def __init__(self):
        super().__init__()
        self.brand = None

    def setdetails(self):
        self.brand = input("enter the name of the brand :")
        self.shape = input("the shape of the tyre: ")
        self.material = input("enter the material :")

    def getdetails(self):
        print (f"name of the brand {self.brand}  the shape of the tyre is {self.shape} and material of the tyre is {self.material}")

obj = tyre()

obj.setdetails()
obj.getdetails()