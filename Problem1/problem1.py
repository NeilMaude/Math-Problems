# Math - problem #1
# Count values which are a multiple of 3 or 5 in natural numbers up to N

import sys

def isMultiple(n):
    if n % 3 == 0:
        #print('%s mod 3 is zero' % n)
        return True
    elif n % 5 == 0:
        #print('%s mod 5 is zero' % n)
        return True
    else:
        return False

def main(N):
    print('Main calculation')
    count = 0
    sum = 0
    for i in range(1,N):
        if isMultiple(i):
            count += 1
            sum += i
    return count, sum

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Running unit tests...')
        print('Hint: there are no unit tests...')
    else:
        print('Running main calculation')
        print('Counting multiples up to : %s' % sys.argv[1])
        count, sum = main(int(sys.argv[1]))
        print('Result for %s is %s, with count of %s' % (sys.argv[1], sum, count))