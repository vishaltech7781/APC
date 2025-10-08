class car:
    def __init__(self,owner,name,regis_no,brand,deli_addr):
        self.owner = owner
        self.name = name
        self.regis_no = regis_no
        self.brand = brand
        self.deli_addr = deli_addr
    
    def display(self):
        print("name of the owner :",self.owner )
        print("car name: ",self.name)
        print("its registration number :",self.regis_no)
        print("owned by the brand :",self.brand)
        print("car is to be delivered at the address :",self.deli_addr)

o = input("enter the owner name :")
n = input("enter the name of the car :") 
r = int(input("enter the registration number :"))
b  = input("enter the brand name :")
d = input("enter the delivery address :")
c = car(o,n,r,b,d)
c.display()


    