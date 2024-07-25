# Q WAP to find the sum of the digits of a number

def SumOfDigits(n):
    
    StrDigits = str(n)

    length_digits = len(StrDigits)

    sumofdigits = sum(int(digit) for digit in StrDigits)

    return sumofdigits

user = int(input('Enter a number:'))

print (SumOfDigits(user))
