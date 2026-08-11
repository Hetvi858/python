
# Write a program to define and use user-defined functions with different types of arguments.

#define user-defined functions

def greetings():
    print("Welcome to java")

# 1.Positional Arguments

def add(a,b):
    print("Sum:",a+b)
add(1,2)

# 2.Keyword Arguments

def student(name,surname):
    print("Your name is ",name,surname)
student(name="hetvi",surname="chotara")

# 3.Default Arguments

def details(name,subject="python"):
    print("welcome to ",subject,name,"!!")
details(name="hetvi")

# 4.Variable-Length Arguments

def total(*numbers):
    print(numbers)

total("hetvi","chotara")
total(1, 2, 3, 4)
    



    
