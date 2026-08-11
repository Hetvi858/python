#Write a program to create and manipulate lists using indexing slicing and list comprehensions.

print(' 1.creating list & indexing ')

fruits = ['apple','banana','orange']
print(fruits)

# Accessing items using their position (index starts at 0)
print('first fruit:',fruits[0])
print('last fruit:',fruits[2])

# 2. List Slicing
print("\n 2. List Slicing ")

numbers=[10,20,30,40]
print(numbers)

# Grabbing a portion of the list [start:end]

print('first three number:[0:3]:',numbers[0:3])

# Reversing the list

print('reversed list [::-1]:', numbers[::-1])


# 3. List Comprehensions
print("\n 3. List Comprehensions")

# Converting fruits into uppercase
uppercase_fruits = [fruit.upper() for fruit in fruits]
print('Uppercase fruits:', uppercase_fruits)

# Creating a list of even numbers
even_numbers = [number for number in numbers if number % 2 == 0]
print('Even numbers:', even_numbers)

# Creating a list of squared numbers
squared_numbers = [number * number for number in numbers]
print('Squared numbers:', squared_numbers)


