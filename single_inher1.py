class animal:
    def __init__(self,name):
        self.name = name

    def display(self):
        print(f"Dog is also the animal enlike {self.name} ")

class dog(animal):
    def __init__(self,name,habit,eat):
        self.habit = habit
        self.eat = eat
        super().__init__(name)
    
    def getname(self):
        print("name of the dog:",self.name)
        print("dog has the habit of :",self.habit)
        print("it loves eating :",self.eat)

obj = dog("snoopie","barking","bones")

obj.display()
obj.getname()
