# Define what a prime is

def primecheck(num):
    if num == 2:
        return True
    elif num == 1 or 0:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True


# Make a prime number generator

def primegen(start):
    for i in range(start, 9999999):
        if primecheck(i) == True:
            yield i
        else:
            pass


prime = primegen(0)  # Setting a starting prime number

nextprime = str(input("Would you like to see the next prime number?(Yes/No) "))  # User input: continue or not

while nextprime == 'Yes':  # Continue the program
    print(next(prime))
    nextprime = input("Would you like to see the next prime number?(Yes/No) ")

if nextprime == 'No':
    print('Ok it was nice seeing you!')

