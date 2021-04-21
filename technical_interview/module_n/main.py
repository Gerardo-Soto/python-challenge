"""
Write a Python program which prints the integers from 1 to a specific number 15.
For multiples of three print "Fizz" instead of the number and for
the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".
"""

import sys

if __name__ == '__main__':
    print(f'Hola: {sys.argv[1]}')
    lim = int(sys.argv[1])
    for x in range(1, lim):
        if x%3 == 0:
            print("Fizz")
        elif x%5 == 0:
            print("Buzz")
        elif x%3 == 0 and x%5 == 0:
            print("FizzBuzz")
        else:
            print(x)

