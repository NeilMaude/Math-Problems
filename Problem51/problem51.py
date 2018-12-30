# Math problem template

import sys
import time

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


def unique_digits(n, verbose=False):
    str_n = str(n)
    digits = []
    for d in str_n:
        #print(d)
        unique = True
        for i in range(0,len(digits)):
            if digits[i] == d:
                unique = False
        if unique:
            digits += [d]
    if verbose:
        print('Unique digit list: ', digits)
    return digits


def permute_digit(num,digit_target, verbose=False):
  # get the list of permutations created by replacing digit_target in num
    permutations = []
    str_n = str(num)
    for i in range(0,10):
        perm = str_n.replace(str(digit_target),str(i))
        if verbose:
            print(perm, 'Replacing %s with %s' % (digit_target,i))
        if len(str(int(perm))) == len(str(num)):
            permutations += [int(perm)]
    if verbose:
        print('Permuations list:\n', permutations)
    return permutations


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


# get max value from an array of permutations
def max_perm_value(perms):
    n_max = 0
    for p in perms:
        if p > n_max:
            n_max = p
    return n_max

# check if value in primes
def check_in_primes(n):
    global primes
    fFound = False
    for p in primes:
        if p == n:
            fFound = True
            break
    return fFound


def main(required_count, verbose=False, n_start=2):
    print('Main calculation...')

    global primes

    # Main calculation code here...
    #required_count = 8
    #verbose = False

    max_prime = 2
    primes = []
    check_factors(2)

    # Loop over natural numbers
    N = n_start
    fSolution = False

    while not fSolution:

        # Basic progress indicator
        print_progress(N)

        # Make sure we have primes up to N
        if N > max_prime:
            print('Getting more primes up to N=%s' % N)
            for i in range(max_prime + 1, N + 1):
                check_factors(i)
            max_prime = N

        # Check if N is prime - no need to go any further if not
        if check_in_primes(N):
            if verbose:
                print('Found candidate prime N=%s' % N)

            # Get unique digits
            u_digits = unique_digits(N, verbose=verbose)
            for d in u_digits:
                # Get permutations
                perms = permute_digit(N, d, verbose=verbose)

                # Get the max permutation value and all primes up to that value
                max_perm = max_perm_value(perms)
                if max_perm > max_prime:
                    print('Getting more primes up to max_perm=%s' % max_perm)
                    for i in range(max_prime + 1, max_perm + 1):
                        check_factors(i)
                    max_prime = max_perm

                    # Get the prime permutations
                prime_perms = []
                for p in perms:
                    if check_in_primes(p):
                        prime_perms += [p]

                        # Check if we have enough prime values in the family - if so, we are done at N
                if len(prime_perms) == required_count:
                    fSolution = True
                    print('Solution found at %s' % N)
                    print('Prime permutations:\n', prime_perms)
                    break
                else:
                    if verbose:
                        print(prime_perms)

            # Did not find enough permutations, so increment N and proceed
            N += 1

        else:
            # N is not prime, just move on
            if verbose:
                print('%s is not prime, moving on...' % N)
            N += 1

    output = N

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
        print('Time taken was', time.strftime("%H:%M:%S", time.gmtime(end_time-start_time)))
