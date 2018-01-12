#  --*-coding:utf-8-*--

import sys
import time
import math


def f(N, K, U, P):
    P = sorted(P)
    
    for i, p in enumerate(P):
        nextP = P[i+1] if i+1 < len(P) else 1
        dU = (nextP - p)*(i+1)
        
        if dU >= U:
            p2 = (p + U/(i+1))**(i+1)
            for j in range(i+1, len(P)):
                p2 *= P[j]
            
            return p2
        
        U -= dU

    return 1

        
def test():
    print(f(4, 4, 1.4000, [0.5000, 0.7000, 0.8000, 0.6000]))
    print(f(2, 2, 1.0000, [0.0000, 0.0000]))
    


def main():
    numOfTestCase = int(input())
    t0 = time.time()

    for testCase in range(numOfTestCase):
        N, K = map(int, input().split())
        U = float(input())
        P = list(map(float, input().split()))

        t1 = time.time()
        print('Case #' + str(testCase+1) + ':',
              '{0:.6f}'.format(f(N, K, U, P)))

        if numOfTestCase >= 10:
            t2 = time.time()

            print('... #' + str(testCase+1) + '/' + str(numOfTestCase),
                  '{0:.2f}'.format(t2 - t1),
                  '{0:.2f}'.format(t2 - t0),
                  file=sys.stderr)
    
if __name__ == '__main__':
    main()
