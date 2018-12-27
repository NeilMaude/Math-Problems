# Math problem #4
# Largest palindromic product of two N-digit numbers

import sys

# Define helper functions here

def reverse_string(s):
    new = ''
    for c in s:
        new = c + new
    return new

def palindrome(n):
    # Is n a palindrome?
    # I.e. reads same each way
    # Need to consider this as a string

    s = str(n)
    #print(s, len(s))
    if len(s) % 2 == 0:
        # even length
        s1 = s[0:int(len(s)/2)]
        #print(s1)
        s2 = s[int(len(s)/2):len(s)]
        #print(s2)
    else:
        # odd length - can ignore the middle digit
        s1 = s[0:int((len(s)-1) / 2)]
        s2 = s[int((len(s)-1)/2)+1:]

    if s1 == reverse_string(s2):
        return True
    else:
        return False

def start_value(n):
    # create the first n-digit number, non-zero
    return int('1'.ljust(n,'0'))

def end_value(n):
    # create the max value
    return int(''.ljust(n,'9'))

def main(n):
    print('Main calculation...')

    # Main calculation code here...

    # Looking to loop over all multiples of n-digit numbers
    largest = 0
    x = start_value(n)
    y = end_value(n)
    for i in range(x,y+1):
        for j in range(x,y+1):
            if palindrome(i*j):
                print('Found palindrome %s, from %s x %s' % (i*j,i,j))
                if i * j > largest:
                    print('Largest so far...')
                    largest = i * j

    output = largest

    return output

def unit_tests():
    print('Running unit tests...')

    print('Unit test #1, reverse 1234 is %s' % reverse_string('1234'))
    print('Unit test #2, palindrome 1234 is %s' % palindrome(1234))
    print('Unit test #3, palindrome 1221 is %s' % palindrome(1221))
    print('Unit test #4, palindrome 123 is %s' % palindrome(123))
    print('Unit test #4, palindrome 121 is %s' % palindrome(121))
    print('Unit test #5, 3-digit start value is %s' % start_value(3))
    print('Unit test #6, 3-digit end value is %s' % end_value(3))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        # Run unit tests, if there are any...
        unit_tests()
    else:
        # Run main calculation with input parameter - change for more params...
        result = main(int(sys.argv[1]))
        print('Result for input %s is %s' % (sys.argv[1], result))