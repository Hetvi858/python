#Write a program to illustrate instance variables and class variables.

class student:
    school = "Mother's school"

    def __init__(self,name):
        self.name = name

s1= student("milan")
s2= student("hardik")

print(s1.name,"goes to",s1.school)
print(s2.name,"goes to",s2.school)
