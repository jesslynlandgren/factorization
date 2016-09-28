import math
import numpy

# Get number to be factored from user & type cast as int
num = int(raw_input('Enter an integer number: '))

# Assign starting factors applicable to all real numbers
factors = [0,1]
primefactors = []
primes = [2,3,5,7,11,13,17,19,23,29,31]
counts = {}


#Function to remove factor from possibilities and append to factors[]
def yesFactor(num,factor):

    global primefactors

    if num % factor == 0:
        primefactors.append(factor)
        num = num/factor
        yesFactor(num,factor)
    else:
        pass


for prime in reversed(primes):
    yesFactor(num,prime)
for pf in set(primefactors):
    counts[pf] = primefactors.count(pf)
for
print counts
