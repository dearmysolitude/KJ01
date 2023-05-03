import sys, math
def prime(number):
    if number == 1:
        return False
    else:
        i = 2
        while i <= math.ceil(number/2): #2 , 짝수!
            if(number % i == 0):
                return False
            i += 1
        return True
def sol18(numbers):
    n = 0
    for number in numbers:
        if (prime(number) == True):
            n += 1
    print(n)
