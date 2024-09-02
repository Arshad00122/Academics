#WHOLE CALCULATOR IN HERE
#Without module


print ("""This is a program which is made for calculation
please type help to know all the commands""")
while True:
    command=input(">").lower()
    if command=='help':
        print ("""*Commands
        Type add for addition
        Type substract for substration
        Type divide for division
        Type multiply for multiplication
        Type quit to quit this application""")
    elif command=="add":
        a=int(input("Enter the first number: "))
        b=int(input("Enter the second number: "))
        soln=a+b
        print (soln)
    elif command=="substract":
        a=int(input("Enter the first number: "))
        b=int(input("Enter the second number: "))
        soln=a-b
        print (soln)
    elif command=='divide':
        a=int(input('Enter the numerator number: '))
        b=int(input("Enter the denominator number: "))
        soln=a//b
        print (soln)
    elif command=="multiply":
        a=int(input("Enter the first number: "))
        b=int(input("Enter the second number: "))
        soln=a*b
        print (soln)
    elif command=="quit":
        break
    else:
        print("Please enter only those commands given in the help section")
    
