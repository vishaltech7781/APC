class exam():
    def result(self,m1=None,m2=None):

        self.res = res
        res = m1+m2

class student1(exam):
    def result(self,name=None,roll=None):
        self.name = name
        self.roll = roll
        self.name = input("enter the name:")
        self.roll = input("enter the roll:")
        super().result()
        self.m1 = int(input("enter the exam 1 marks:"))
        self.m2 = int(input("enter the exam 2 marks:"))
        
        print(f"name of the student {self.name} and roll no. is {self.roll} result of the paper {self.res}")

class student2(exam):
    def result(self,name=None,roll=None):
        self.name = name
        self.roll = roll
        self.name = input("enter the name:")
        self.roll = input("enter the roll:")
        super().result()
        self.m1 = int(input("enter the exam 1 marks:"))
        self.m2 = int(input("enter the exam 2 marks:"))
        
        print(f"name of the student {self.name} and roll no. is {self.roll} result of the paper {self.res}")


s1 = student1()
s2 = student2()

s1.result()
s2.result()