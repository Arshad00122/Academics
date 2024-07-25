# Q Create a list of five elements where the user enters the value of each element.
# Print the list created and reverse order of that list

i = 0

lst = []

while i<5:
    user = input("Enter a value:")
    lst.append(user)
    i+=1

print(lst)

print("Reverse Order:", end='')
lst.reverse()
print (lst)
