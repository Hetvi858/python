num = input("Enter a Number: ")          

if num.isdigit():
    num = int(num)

    sum = 0

    while num > 0:                      
        digit = num % 10                
        sum = sum + digit       
        num = num // 10         

    print("Sum of Digits =", sum)

else:
    print("Warning! Entered number must be an integer.")
