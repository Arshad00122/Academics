#Q Check whether the number entered is an armstrong number or not



def armstrong(n):
    list_of_digits = [int(digit) for digit in str(n)]

    # Creating a dictionary of list
    variable = {}
    for i, digit in enumerate(list_of_digits):
        variable[f'digit_{i}'] = digit

    """
    list stored in the form of a dictionary
    variable = {
        digit_1 = digit
        digit_2 = digit
    } """
    
    valsize = len(list_of_digits)
    cube_variable = {}
    for i in range(len(list_of_digits)):
        cube_variable[f'CubeDigit_{i}'] = (variable[f'digit_{i}'])**valsize

    val = list(cube_variable.values())

    valsum = sum(val)

    if valsum == n:
        print(f"{n} is an Armstrong number")
    else:
        print (f"{n} is not an Armstrong number")
        

n = int(input("Enter a number:"))

armstrong(n)

# Improved Version

def is_armstrong_number(number):

    # Convert number to string to easily iterate over digits
    num_str = str(number)

    # Get the number of digits
    num_digits = len(num_str)

    # Calculate the sum of digits each raised to the power of num_digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)

    # Check if the sum is equal to the original number
    return armstrong_sum == number

# Example usage
number = int(input("Enter a number to check if it's an Armstrong number: "))
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
