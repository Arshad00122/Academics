class Parent:
    def __init__(self, fname, lname): #This is a constructor
        fname+=" "+lname
        print(f"My name is {fname}")

fstnm = input("Enter first name: ")
lstnm = input("Enter last name:")



p1 = Parent(fstnm,lstnm)

print (p1)
