#Write a program to perform file pointer operations using seek and tell methods.

f = open("demo.txt", "w")
f.write("Hello Python Programming")
f.close()

f = open("demo.txt", "r")

print("Initial Position:", f.tell())

print("Data:", f.read(5))

# Display current position
print("Position after reading:", f.tell())

# Move file pointer to position 6
f.seek(6)

# Display current position
print("Position after seek:", f.tell())

# Read remaining data
print("Remaining Data:", f.read())

f.close()

