#Write a program to create a dictionary and demonstrate dictionary methods and iteration.

student= {
    'id': 10,
    'name': 'diya',
    'age': 20,
    'course':'computer science'
    }
print(student)



print('\nkeys:')
print(student.keys())

print('\nvalues:')
print(student.values())


print('\nitems:')
print(student.items())


print("\nget value of 'name':")
print(student.get('name'))


print({'age':21,'id':3})
print('\ndictionary after update:')
print(student)


student_copy = student.copy()
print('\ncopied dictionary:')
print(student_copy)

print('\niteration through keys:')
for key in student:
    print(key)

print('\niteration through values:')
for values in student.values():
    print(values)

print('\niteration through key-values pair:')
for key,value in student.items():
    print(key ,':',value)

    
