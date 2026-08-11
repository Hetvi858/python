
# Write a program to demonstrate recursion using factorial or Fibonacci series.

def factorial(n): #(3)(2)(1)
    if n == 0 or n == 1: #third time it will becomes true
        return 1
    else:
        return n * factorial(n - 1) #3*f(3-1)  #2*f(2-1)

num = int(input("Enter a number: "))#3

result = factorial(num)

print("Factorial of", num, "=", result)
