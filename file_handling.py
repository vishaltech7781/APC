#write mode used
file = open("sample.txt","w")


file.write("hello guys kaise ho app loghh")
file.seek(0)

#in same file without closing the file read function used
file1 = open("sample.txt","r")
content = file1.read()
print(content)
file1.close()

#append mode
file2 = open("sample.txt","a")

file2.write("\nram ram")
file2.close()

#copying from one file to another
file3 = open("copy.txt","w")
file3.write(content)
file3.close

