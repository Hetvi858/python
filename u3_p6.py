#Write a program to perform file and directory operations using os and sys modules.

import os
import sys

print("Current Directory:", os.getcwd())


os.mkdir("MyFolder")
print("Directory created successfully.")

# Create a file inside the directory
file_path = os.path.join("MyFolder", "sample.txt")

with open(file_path, "w") as file:
    file.write("Hello, Python!")

print("File created successfully.")

# Display files and directories
print("Contents of current directory:")
print(os.listdir())

# Display command-line arguments
print("Command-line arguments:", sys.argv)

os.remove(file_path)
print("File deleted successfully.")


os.rmdir("MyFolder")
print("Directory deleted successfully.")
