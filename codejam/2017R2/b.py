#  --*-coding:utf-8-*--

import sys
import time
import collections
import math


# Each test case starts with a single line with three integers 
# N, the number of seats in the roller coaster, 
# C, the number of potential customers, and 
# M, the number of tickets sold. 

# The customers are identified with numbers between 1 and C. 
# Then, M lines follow, each containing two integers: 
# Pi, the position in the roller coaster assigned to the i-th ticket, and 
# Bi, the identifier of the buyer of that ticket. 

def f(N, C, PBs):
    pCounter = collections.Counter(pb[0] for pb in PBs)
    bCounter = collections.Counter(pb[1] for pb in PBs)
    amount = 0
    numOfRides = 0

    for p, x in sorted(pCounter.items()):
        amount += x
        numOfRides = max(
            numOfRides, 
            int(math.ceil(amount/p)))

    numOfRides = max(
        numOfRides,
        max(bCounter.values()))

    numOfHonors = sum(
        max(0, x - numOfRides) for x in pCounter.values())

    return numOfRides, numOfHonors

    


def main():
    numOfTestCase = int(input())
    t0 = time.time()

    for testCase in range(numOfTestCase):
        N, C, M = map(int, input().split())
        PBs = [tuple(map(int, input().split())) for i in range(M)]

        t1 = time.time()
        y, z = f(N, C, PBs)
        print('Case #' + str(testCase+1) + ':', y, z)

        if numOfTestCase >= 10:
            t2 = time.time()

            print('... #' + str(testCase+1) + '/' + str(numOfTestCase),
                  '{0:.2f}'.format(t2 - t1),
                  '{0:.2f}'.format(t2 - t0),
                  file=sys.stderr)
    
if __name__ == '__main__':
    main()


