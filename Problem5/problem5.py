# Project Euler problem #5
# Smallest number which is evenly divisible by all numbers up to N

import sys


def allDivisible(i, N):
    divisible = True
    for j in range(1,N+1):
        if i % j != 0:
            divisible = False
    return divisible


def main(N):
    print('Main calculation')

    found_result = False
    i = N

    while not found_result:
        if allDivisible(i, N):
            found_result = True
        else:
            i += 1

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
    return i


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Running unit tests...')
        print('Hint: there are no unit tests...')
    else:
        print('Running main calculation')
        print('Finding smallest value evenly divisible by integers up to %s' % sys.argv[1])
        result = main(int(sys.argv[1]))
        print('Result for %s is %s' % (sys.argv[1], result))