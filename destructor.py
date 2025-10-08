class car:
    def __init__(self):
        self.owner = "Vishal"
        self.name = "virtus"
       
    
    def display(self):
        print("name of the owner :",self.owner)
        print("car name: ",self.name)
    
    def __del__(self):
        print ("the destructor is the successfully detroyed.")

c = car()
c.display()


    