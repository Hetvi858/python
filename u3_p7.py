#Write a program to copy move and delete files using shut il module.


import shutil
import os

with open("file1.txt", "w") as f:
    f.write("Hello Python")

shutil.copy("file1.txt", "copy.txt")
print("File copied successfully.")

shutil.move("copy.txt", "moved.txt")
print("File moved successfully.")

os.remove("moved.txt")
print("File deleted successfully.")


