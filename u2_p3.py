#Write a program to generate a multiplication table using a for loop.

num= int(input('enter a number:'))

print('multipliaction table of',num)
         
for i in range(1,11):
         print(f'{num*1} * {i} = {num*i}')
         
