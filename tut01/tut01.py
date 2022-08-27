def factorial(x):
    if x < 0:
        return 0
    elif x == 0 or x == 1:
        return 1
    else:
        facto = 1
        while(x > 1):
            facto *= x
            x -= 1
        return facto
 
num = int(input("Enter the number whose factorial is to be found "))
print("Factorial of",num,"is",factorial(num))