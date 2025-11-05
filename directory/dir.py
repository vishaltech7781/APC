import os

os.mkdir("example_dir")
print("Directory created.")
os.chdir("example_dir")
print("Changed working directory to:", os.getcwd())

os.mkdir("sub_dir")
print("Subdirectory created.")

print("Contents of current directory:", os.listdir())

os.rename("sub_dir", "renamed_dir")
print("Subdirectory renamed to 'renamed_dir'.")

os.rmdir("renamed_dir")
print("Directory  deleted.")

os.chdir("..")
os.rmdir("example_dir")
print("Directory  deleted.")