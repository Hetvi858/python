#Write a program to demonstrate the use of assert statement. 

age = int(input("Enter your age: "))

try:
    assert age >= 18, "Age must be 18 or above."
    print("You are eligible to vote.")

except AssertionError as e:
    print("Assertion Error:", e)
