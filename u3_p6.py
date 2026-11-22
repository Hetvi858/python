#Write a program to perform file and directory operations using os and sys modules.

import os
import sys

print("Current Directory:", os.getcwd())

os.mkdir("MyFolder")
print("Directory created successfully.")

file = open("MyFolder/sample.txt", "w")
file.write("Hello Python")
file.close()
print("File created successfully.")

print("Files:", os.listdir("MyFolder"))

os.rename("MyFolder/sample.txt", "MyFolder/newfile.txt")
print("File renamed successfully.")

os.remove("MyFolder/newfile.txt")
print("File deleted successfully.")

os.rmdir("MyFolder")
print("Directory removed successfully.")

print("Python Version:", sys.version)
