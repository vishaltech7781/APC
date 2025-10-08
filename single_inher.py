class college:

    def __init__(self,clgname):
        self.clgname = clgname

    def display(self ):
        print("this is the base class")

class student(college):
    
    def __init__(self,clgname,name):
        self.name = name
        super().__init__(clgname)

    def display1(self):
        print("this is the student class which is the child class")

        print("college name is: ",self.clgname)
        print("my name is :",self.name)

obj1 = student("DYP","vishal")
obj1.display()
obj1.display1()