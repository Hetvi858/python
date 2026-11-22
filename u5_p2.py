#Write a program to handle exceptions using try except else and finally blocks.

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter a valid number.")

else:
    print("Division =", result)
    print("No exception occurred.")

finally:
    print("Finally block executed.")

