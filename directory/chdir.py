import os

os.mkdir("myyfolder")
print(" Directory 'myfolder' created successfully!")

# 2️⃣ Change Current Working Directory
os.chdir("directory")
print("Changed directory to:", os.getcwd())

# # 3️⃣ Move Back to Previous Directory
# os.chdir("..")
# print("↩ Back to:", os.getcwd())

# 4️⃣ Remove the Directory
os.rmdir("myfolder")
print("Directory 'myfolder' removed successfully!")
