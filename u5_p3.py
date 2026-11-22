#Write a program to define and raise userdefined exceptions.

# Define user-defined exception
class AgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise AgeError("Age must be 18 or above.")

    print("You are eligible.")

except AgeError as e:
    print("User Defined Exception:", e)

except ValueError:
    print("Please enter a valid age.")
