# Base class
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

# Inherits from Student
class Exam(Student):
    def __init__(self, name, roll, m1, m2):
        super().__init__(name, roll)  # Initialize Student
        self.m1 = m1
        self.m2 = m2
        self.res = m1 + m2            # calculate result

# Independent class
class Project:
    def __init__(self, prjname):
        self.prjname = prjname

class Result(Exam, Project):
    def __init__(self, name, roll, m1, m2, prjname):
        Exam.__init__(self, name, roll, m1, m2)
        Project.__init__(self, prjname)

    def display(self):
        print(f"Name of the student: {self.name}, Roll No.: {self.roll}")
        print(f"Result of the sum: {self.res}")
        print(f"Project name: {self.prjname}")



r = Result("Vishal", 48, 40, 20, "Virtual Assistant")
r.display()
