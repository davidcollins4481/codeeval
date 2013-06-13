#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')
lines = test_cases.read().splitlines()

for test in lines:
    words = test.split(' ')
    words.reverse()

    print ' '.join(words)
    


test_cases.close()


