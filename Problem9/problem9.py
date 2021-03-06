# Math problem #9
# Find special Pythagorean triplet
# a < b < c
# a^2 + b^2 = c^2
# Find abc where a + b + c = 1000

import sys
import time

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


def main(n):
    print('Main calculation...')

    # Main calculation code here...



    output = 0

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
