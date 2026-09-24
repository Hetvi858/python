#Write a program to demonstrate constructor and destructor usage.

class Demo:
    def __init__(self):
        print("constructor called:object created")
    def __del__(self):
        print("Destructor called:object destoryed")

obj = Demo()
del obj
