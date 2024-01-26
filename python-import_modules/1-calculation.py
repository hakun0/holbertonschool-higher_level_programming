#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    a = 10
    b = 5
    d = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div,
    }
    for k, v in d.items():
        print('%s %s %s = %s' % (a, k, b, v(a, b)) + 0 * '{}'.format(0))
