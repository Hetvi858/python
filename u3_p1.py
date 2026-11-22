
# Create a user-defined module
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# Import the module
import mymodule

a = 10
b = 5

print("Addition =", mymodule.add(a, b))
print("Multiplication =", mymodule.multiply(a, b))
