def primeornot(num):
    if num<2:
        print("Its a composite number")

    for i in range(2,int(num**0.5) + 1):

        if num%i==0:
            print ("Its a composite number")
            return # Using return instead of break because we need to get out of the function not only the loop

    print ("its a prime number")

a = 4

primeornot(a)