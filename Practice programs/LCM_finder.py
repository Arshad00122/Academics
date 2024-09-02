#LCM finder

def LCM(x,y):
    if x>y:
        if x%y==0:
            print ("LCM of ",x, " and ",y, " is ",x/y)
        else:
            print ("LCM of ",x, " and ",y, " is ",x*y)
    elif y>x:
        if y%x==0:
            print ("LCM of ",x, " and ",y, " is ",y/x)
        else:
            print ("LCM of ",x, " and ",y, " is ",x*y)
    else:
        print ("invalid")
    

num1 = int(input("Enter a number:"))

num2 = int(input("Enter a number:"))

LCM(num1,num2)
