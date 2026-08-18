#Write a program to demonstrate list dictionary and set comprehensions.

# 1. List 
numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]

print("List Comprehension:")
print("Original List:", numbers)
print("Squares:", squares)


# 2. Dictionary 
numbers = [1, 2, 3, 4, 5]
square_dict = {n: n ** 2 for n in numbers}

print("\nDictionary Comprehension:")
print("Dictionary:", square_dict)


# 3. Set 
numbers = [1, 2, 2, 3, 3, 4, 5]
square_set = [n ** 2 for n in numbers]
print("\nSet Comprehension:")
print("Original List:", numbers)
print("set:", square_set)




