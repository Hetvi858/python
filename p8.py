#Write a program to explain mutable and immutable objects in Python.

print("===== MUTABLE OBJECTS =====")

# List
list1 = [1, 2, 3]
list1.append(4)
print("List:", list1)

# Dictionary
dict1 = {"Name": "hetvi", "Age": 20}
dict1["City"] = "anjar"
print("Dictionary:", dict1)

# Set
set1 = {1, 2, 3}
set1.add(4)
print("Set:", set1)


print("\n===== IMMUTABLE OBJECTS =====")

# Integer
num = 10
num = num + 5
print("Integer:", num)

# Float
f = 12.5
f = f + 2.5
print("Float:", f)

# String
str1 = "java"
str2 = str1 + " Programming"
print("Original String:", str1)
print("New String:", str2)

# Tuple
tuple1 = (10, 20, 30)
print("Tuple:", tuple1)

# Boolean
flag = True
flag = False
print("Boolean:", flag)

# Complex Number
c = 2 + 3j
c = c + 1
print("Complex:", c)

