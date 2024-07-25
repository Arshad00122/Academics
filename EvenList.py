# Q Ask the user to provide the integer inputs to make a list. Store only the even values given and print the list

print("Even List\n")

lstsize = int(input("Enter the length of the list:"))

lst = []

for i in range(0,lstsize):
    val = int(input("Enter an integer:"))
    if val%2==0:
        lst.append(val)

print(lst)