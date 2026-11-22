#Write a program to read and write data into a file using different file modes.


# Write data into a file
f = open("demo.txt", "w")
f.write("Hello Python\n")
f.write("Welcome to File Handling")
f.close()
print("Data written successfully.")

# Read data from file
f = open("demo.txt", "r")
print("\nFile Content:")
print(f.read())
f.close()

# Append data into file
f = open("demo.txt", "a")
f.write("\nLearning Python Programming")
f.close()
print("\nData appended successfully.")

# Read updated data
f = open("demo.txt", "r")
print("\nUpdated File Content:")
print(f.read())
f.close()

