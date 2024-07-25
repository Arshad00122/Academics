# Check if a cerrtain year is leap year or not

yrs = int(input("Enter an year:"))

if yrs<=0:
  print("Invalid year")
elif (yrs%4==0 and yrs%100!=0) or (yrs%400==0 and yrs%100==0):
  print ("Its a leap")
else:
  print("Its not a leap")
