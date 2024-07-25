# Q Display the fibonacci sequence up to nth terms

#Fibonacci Sequence means each number is equal to the sum of preceding two number

def fibonacci_Seq(n):

    fibonacci_Sequence = [0,1]

    while len(fibonacci_Sequence)<n:
        fibonacci_Sequence.append(fibonacci_Sequence[-1] + fibonacci_Sequence[-2])
    return fibonacci_Sequence

n = int(input("Enter a number:"))

for i in fibonacci_Seq(n):
    print (i,end=' ')
