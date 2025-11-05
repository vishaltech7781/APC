f = open("file4.txt", "r+")
print("Before writing:", f.readlines())
f.write("\nAdding more text using r+ mode.")
f.close()
