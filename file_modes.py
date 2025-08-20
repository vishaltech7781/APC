with open("hello.txt", "r+") as f:
    content = f.read()
    f.write("\nAdded using r+")


#use of the w+ mode these will delete all the existing data earlier and write again the new content 
with open("hello1.txt", "w+") as f:
    f.write("New content added using the w+")
    # f.seek(0)  # move cursor to beginning
    print(f.read())

#use of the a+ mode
with open("hello2.txt", "a+") as f:

    f.write("Appended with a+")
    print(f.read())
    f.close()


