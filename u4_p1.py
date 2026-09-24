#Write a program to create a class and object in Python. 

class student:
    
    def __init__(self,roll_num,name):
        self.roll_num= roll_num
        self.name= name
    
obj = student(1,"raj")
print(obj.roll_num)
print(obj.name)
