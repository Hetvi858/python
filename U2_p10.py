#Write a program to generate a sequence of numbers using generator functions and yield keyword.

def generate_numbers(n):
    
    for i in range(1,n+1):
        yield i

n = int(input('enter limit:'))

numbers= generate_numbers(n)

print('Generated sequence:')

for num in numbers:
        print(num)



