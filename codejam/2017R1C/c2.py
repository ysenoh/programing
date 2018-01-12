#  --*-coding:utf-8-*--

import sys
import time
import math


def f(N, K, U, P):
    P = sorted(P)
    P2 = P[-K:]

    for i, p in enumerate(P2):
        nextP = P2[i+1] if i+1 < len(P2) else 1
        dU = (nextP - p)*(i+1)
        
        if dU >= U:
            p2 = (p + U/(i+1))
            for j in range(i+1):
                P[-K+j] = p2
            
            return g(P, K)
        
        U -= dU

    return 1



def g(P, K):
    X = [0]*(K+1)
    X[0] = 1

    for p in P:
        X = [X[i] + (X[i-1]-X[i])*p if i>0 else 1 for i in range(K+1)]

    return X[-1]
            
            
        
def test():
    print(f(4, 4, 1.4000, [0.5000, 0.7000, 0.8000, 0.6000]))
    print(f(2, 2, 1.0000, [0.0000, 0.0000]))
    print(f(2, 1, 0.0000, [0.9000, 0.8000]))
    print(f(2, 1, 0.1000, [0.4000, 0.5000]))


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
