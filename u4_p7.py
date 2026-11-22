# Write a program to illustrate method resolution order and magic methods.

class A:
    def show(self):
        print("Class A")

class B:
    def show(self):
        print("Class B")

class C(A, B):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Student Name: " + self.name

obj = C("Hetvi")

obj.show()

print("MRO:", C.mro())

print(obj)

