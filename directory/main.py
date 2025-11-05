import os

print("current dir:",os.getcwd())

os.mkdir("newdir")
print("create successfully")

os.rmdir("newdir")
print("remove successfully")


filenames=os.listdir("..")
print(filenames)

print(os.path.isdir("abc"))
print(os.path.exists("/etc"))

