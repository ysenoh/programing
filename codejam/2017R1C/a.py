#  --*-coding:utf-8-*--

import sys
import time
import math


def f(N, K, RH):
    SR = sorted(((2*r*h, r) for r, h in RH), reverse=True)

    maxOfR = max((r for _,r in SR[:K-1]), default=0)
    return math.pi*(sum(s for s,_ in SR[:K-1]) + 
                    max(max(maxOfR, r)**2 + s for s, r in SR[K-1:]))


def main():
    numOfTestCase = int(input())
    t0 = time.time()

    for testCase in range(numOfTestCase):
        N, K = map(int, input().split())
        RH = [tuple(map(int, input().split())) for i in range(N)]

        t1 = time.time()
        print('Case #' + str(testCase+1) + ':',
              '{0:.6f}'.format(f(N, K,  RH)))

        if numOfTestCase >= 10:
            t2 = time.time()

            print('... #' + str(testCase+1) + '/' + str(numOfTestCase),
                  '{0:.2f}'.format(t2 - t1),
                  '{0:.2f}'.format(t2 - t0),
                  file=sys.stderr)
    
if __name__ == '__main__':
    main()
