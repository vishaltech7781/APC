class car:
    def __init__(self):
        self.owner = "Vishal"
        self.name = "virtus"
        self.regis_no = 12344
        self.brand = "TOYOTA"
        self.deli_addr = "Solapur"
    
    def display(self):
        print("name of the owner :",self.owner)
        print("car name: ",self.name)
        print("its registration number :",self.regis_no)
        print("owned by the brand :",self.brand)
        print("car is to be delivered at the address :",self.deli_addr)

c = car()
c.display()


    