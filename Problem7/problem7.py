# Math problem #7
# Find n-th prime

import sys
import time

primes = []

# Define helper functions here

def check_factors(n):
    # Check the list of primes found so far - are any a factor of the target
    global primes
    prime_target = True
    for p in primes:
        if n % p == 0:
            prime_target = False
            break
    if prime_target == True:
        # the input value is a prime number
        print('Found prime number %s' % n)
        primes += [n]
    return prime_target

# Useful progress indicator
def print_progress(i):
    # Show some progress in a reasonably neat fashion...
    if i < 10:
        print('Testing %s' % i)
    elif i < 100 and i % 10 == 0:
        print('Testing %s' % i)
    elif i < 1000 and i % 100 == 0:
        print('Testing %s' % i)
    elif i < 10000 and i % 1000 == 0:
        print('Testing %s' % i)
    elif i < 100000 and i % 10000 == 0:
        print('Testing %s' % i)
    elif i < 1000000 and i % 100000 == 0:
        print('Testing %s' % i)
    elif i % 1000000 == 0:
        print('Testing %s' % i)


def main(n):
    print('Main calculation...')

    print('Finding %s-th prime' % n)
    # Main calculation code here...

    # Find all primes until we are done...
    next_value = 2
    while len(primes) < n:
        print_progress(next_value)
        check_factors(next_value)
        next_value += 1

    output = primes[len(primes)-1]

    return output

def unit_tests():
    print('Running unit tests...')
    print('Hint: there are no unit tests...')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        # Run unit tests, if there are any...
        unit_tests()
    else:
        # Run main calculation with input parameter - change for more params...
        start_time = time.time()
        result = main(int(sys.argv[1]))
        end_time = time.time()
        print('Result for input %s is %s' % (sys.argv[1], result))
        print('Time taken was', time.strftime("%H:%M:%S", time.gmtime(end_time - start_time)))