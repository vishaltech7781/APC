from filehandling import fileread, filewrite, fileupdate  

f1 = fileread.read("file1.txt")
f2 = fileread.read("file2.txt")

filewrite.write("file3.txt",f1+f2)

f4 = fileread.read("file4.txt")

fileupdate.insert_after_n("file3.txt")
