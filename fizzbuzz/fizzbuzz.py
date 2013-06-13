#!/usr/bin/env python
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    (a,b,n) = map(int, test.split(' '))
    i = 0

    while i < n:
        i += 1
        if i % a == 0 and i % b == 0:
            print 'FB',
        elif i % a == 0:
            print 'F',
        elif i % b == 0:
            print 'B',
        else:
            print i,

    print

test_cases.close()
