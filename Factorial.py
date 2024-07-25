# Find the factorial of a number provided by the user

def factorial(num):
    sum = 1

    for i in range(1,num+1):
        sum *= i
        
    return f"factorial of {num} is {sum}"

user = int(input("Enter a number:"))

print(factorial(user))