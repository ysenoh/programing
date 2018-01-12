#  --*-coding:utf-8-*--

import sys
import time

def f(D, N, KS):
    return D/max((D-k)/s for k,s in KS)


def main():
    numOfTestCase = int(input())
    t0 = time.time()

    for testCase in range(numOfTestCase):
        D, N = map(int, input().split())
        KS = [tuple(map(int, input().split())) for i in range(N)]

        t1 = time.time()
        print('Case #' + str(testCase+1) + ':',
              '{0:.6f}'.format(f(D, N, KS)))

        if numOfTestCase >= 10:
            t2 = time.time()

            print('... #' + str(testCase+1) + '/' + str(numOfTestCase),
                  '{0:.2f}'.format(t2 - t1),
                  '{0:.2f}'.format(t2 - t0),
                  file=sys.stderr)
    
if __name__ == '__main__':
    main()

