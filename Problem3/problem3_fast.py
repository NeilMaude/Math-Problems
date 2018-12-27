# Project Euler problem template

import sys
import math

prime_factors = []

def primeFactors(n):

    global prime_factors

    while n % 2 == 0:
        prime_factors += [2]
        print('Found prime factor: 2')
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):

        # while i divides n , print i ad divide n
        while n % i == 0:
            prime_factors += [i]
            print('Found prime factor: %s' % i)
            n = n / i

    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        print('%s is a prime' % n)
        prime_factors += [n]

def main(n):
    print('Main calculation...')

    # Main calculation code here...

    primeFactors(n)

    return int(prime_factors[len(prime_factors)-1])

def unit_tests():
    print('Running unit tests...')
    print('Hint: there are no unit tests...')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        # Run unit tests, if there are any...
        unit_tests()
    else:
        # Run main calculation with input parameter - change for more params...
        result = main(int(sys.argv[1]))
        print('Result for input %s is %s' % (sys.argv[1], result))