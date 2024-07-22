def GreatestAmongThree(a,b,c):
    if a>=b and a>=c:
        return f"{a} is greater"
    elif b>=a and b>=c:
        return f"{b} is greater"
    else:
        return f"{c} is greater"
    
a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
c = int(input("Enter a number:"))

print (GreatestAmongThree(a,b,c))