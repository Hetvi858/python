#Write a program to demonstrate iterators and iterables in Python.

numbers= [10,20,30,40]

print('iterables:',numbers)

#convert iterbles into iterators
it = iter(numbers)

print('iterables values:')
print(next(it))
print(next(it))
print(next(it))
print(next(it))




