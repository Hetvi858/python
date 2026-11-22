#Write a program to demonstrate different types of errors and exceptions in Python

try:
    print(x)
except NameError:
    print("Name Error: Variable is not defined")

try:
    a = 10 / 0
except ZeroDivisionError:
    print("Zero Division Error: Cannot divide by zero")

try:
    num = int("Hello")
except ValueError:
    print("Value Error: Invalid value")

try:
    result = 10 + "Hello"
except TypeError:
    print("Type Error: Cannot add number and string")

try:
    list1 = [10, 20, 30]
    print(list1[5])
except IndexError:
    print("Index Error: List index out of range")

try:
    d = {"name": "Hetvi"}
    print(d["age"])
except KeyError:
    print("Key Error: Key not found")
