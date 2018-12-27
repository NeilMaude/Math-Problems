# Math problem #2
# Sum of all even Fibonacci numbers less than or equal to a maxumum value (4 million)

import sys

def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False

def main(maxvalue):
    print('Main calculation')
    next_last_value = 1
    last_value = 2
    count = 0
    sum = 0

    while last_value <= maxvalue:

        if isEven(last_value):
            print('Found an even fibonacci number: %s' % last_value)
            count += 1
            sum += last_value
        new_value = next_last_value + last_value
        next_last_value = last_value
        last_value = new_value

    return count, sum

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Running unit tests...')
        print('Hint: there are no unit tests...')
    else:
        print('Running main calculation')
        print('Counting even fibonacci numbers up to : %s' % sys.argv[1])
        count, sum = main(int(sys.argv[1]))
        print('Result for %s is %s, with count of %s' % (sys.argv[1], sum, count))