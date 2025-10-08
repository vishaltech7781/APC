class Project:
    def __init__(self):
        self.projectid = None
        self.projectname = None

    def setproj_details(self):
        self.projectname = input("Enter the name of the project: ")
        self.projectid = int(input("Enter the ID of the project: "))

    def getproj_details(self):
        print(f"Name of the project is {self.projectname} and its ID is {self.projectid}")


class Module(Project):
    def __init__(self):
        super().__init__()   # call Project constructor
        self.modulename = None

    def setmodule_details(self):
        self.modulename = input("Enter the name of the module: ")

    def getmodule_details(self):
        print(f"Name of the module is {self.modulename}")


class Task(Module):
    def __init__(self):
        super().__init__()   # call Module constructor
        self.taskname = None

    def settask_details(self):
        self.taskname = input("Enter the name of the task: ")

    def gettask_details(self):
        print(f"Name of the task is {self.taskname}")


obj = Task()  



obj.setproj_details()
obj.setmodule_details()
obj.settask_details()

print("\n--- Project Information ---")

obj.getproj_details()
obj.getmodule_details()
obj.gettask_details()


