import sys, math

def prime(number):
    if number == 1:
        return False
    else:
        i = 2
        while i < math.ceil(number/2):
            if(number % i == 0):
                return False
            i += 1
    return True
