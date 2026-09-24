#Write a program to demonstrate instance methods class methods and static methods. 

class calculator:
    def add(self,a,b):
        return a+b

    @classmethod
    def info (cls):
        return "calculator class"

    @staticmethod
    def square(x):
        return x*x

c = calculator()
print(c.add(2,3))
print(calculator.info())
print(calculator.square(4))
    
