#!/usr/bin/env python

def isPrime(n):
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

# get all prime numbers
for n in [i+1 for i in range(1000)][::-1]:
    if isPrime(n) and n == int(str(n)[::-1]):
        print n
        exit(0)

