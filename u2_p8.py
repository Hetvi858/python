
# Write a program to illustrate variable scope using local global and nonlocal variables. 

x = 10          #global variable

def outer():
    y = 20      # Local variable of outer()

    def inner():
        nonlocal y
        y = 30  # Nonlocal variable
        z = 40  # Local variable of inner()

        print("Global:", x)
        print("Nonlocal:", y)
        print("Local:", z)

    inner()

outer()
