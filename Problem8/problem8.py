# Math problem #8
# Find sequence of numbers with greatest product

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

# read in a file line by line
def read_data(filename, show=True, singleline=True):
    data = ''
    with open(filename) as fp:
        count = 0
        for line in fp:
            if show:
                print("line {} contents {}".format(count, line))
            if singleline:
                data += line.rstrip()
            else:
                data += line
            count += 1
    return data

def getmultiple(digits):
    multiple = 1
    for c in digits:
        multiple *= int(c)
    return multiple

def main(filename, n):
    print('Main calculation...')

    # Main calculation code here...
    data = read_data(filename, show=False)
    maxmultiple = 0
    maxstart = 0
    maxsequence = ''

    # loop through the data, taking each sequence of n-digits
    start = 1
    while start <= len(data) - n + 1:
        sequence = data[start-1:start-1+n]
        multiple = getmultiple(sequence)
        print('Checking sequence %s, starting at %s, multiple %s' % (sequence, start, multiple))

        # check for the multiple value being best so far
        if multiple > maxmultiple:
            maxmultiple = multiple
            maxstart = start
            maxsequence = sequence
            print('New maximum found...')

        start += 1

    return maxmultiple, maxstart, maxsequence

def unit_tests():
    print('Running unit tests...')
    data = read_data('input.dat')
    print('Unit test #1: read data')
    print('Data: %s', data)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        # Run unit tests, if there are any...
        unit_tests()
    else:
        # Run main calculation with input parameter - change for more params...
        start_time = time.time()
        maxmultiple, maxstart, maxsequence = main(sys.argv[1], int(sys.argv[2]))
        end_time = time.time()
        print('Result for input %s / %s is %s at %s (%s)' % (sys.argv[1], sys.argv[2], maxmultiple, maxstart, maxsequence))
        print('Time taken was', time.strftime("%H:%M:%S", time.gmtime(end_time-start_time)))
