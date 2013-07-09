import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    x,n = [int(x) for x in test.split(',')]

    multiple = 1
    while n*multiple < x:
        multiple = multiple + 1
    
    print multiple * n
test_cases.close()
