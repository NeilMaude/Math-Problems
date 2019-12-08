# Solve Euler Problem 35, circular primes

import time
import sys

primes = []

# Define helper functions here

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
        #print('Found prime number %s' % n)
        primes += [n]
    return prime_target

def get_circular_list(n):
    # n is an input number
    # there will be n rotations of the digits
    n_str = str(n)
    rotations = []
    rotations.append(n_str)
    for x in range(1,len(n_str)):
        #print(n_str[len(n_str)-1], n_str[:len(n_str)-1])
        n_str = n_str[len(n_str)-1] + n_str[:len(n_str)-1]
        rotations.append(n_str)

    return rotations

def main(n):
    print('Main calculation...')

    print('Finding circular primes up to %s' % n)
    # Main calculation code here...

    print('Step 1: find all primes up to %s' % n)

    # Find all primes until we are done...
    next_value = 2
    while next_value < n:
        print_progress(next_value)
        check_factors(next_value)
        next_value += 1

    print('Step 2: check each prime for circular-ness...')
    print('Number of primes is %s' % len(primes))

    # Have all of our primes, so loop through checking which are also circular
    prime_count = 1
    circles_count = 0
    for p in primes:
        print_progress(prime_count)
        rotations = get_circular_list(p)
        f_circular = True
        for r in rotations:
            if not (int(r) in primes):
                f_circular = False
        if f_circular:
            circles_count += 1
        prime_count += 1
    output = circles_count

    return output

if __name__ == "__main__":
    # Run main calculation with input parameter - change for more params...
    start_time = time.time()
    result = main(int(sys.argv[1]))
    end_time = time.time()
    print('Result for input %s is %s' % (sys.argv[1], result))
    print('Time taken was', time.strftime("%H:%M:%S", time.gmtime(end_time - start_time)))

