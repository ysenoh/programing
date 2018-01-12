#  --*-coding:utf-8-*--

import sys
import math
import time

def f(N,P,R,Q):
    # S[i][j] .. i番目の成分のj番目のパッケージ (最小皿数、最大皿数)

    S = [[(int(math.ceil(10*q/(11*r))),
           int(math.floor(10*q/(9*r))))
          for q in sorted(Qi)] for r, Qi in zip(R, Q)]

    cnt = 0
    while True:
        minOfMax, maxOfMin = math.inf, 0

        for Si in S:
            if len(Si) == 0:
                return cnt
            
            s = Si[0]
            maxOfMin = max(maxOfMin, s[0])
            minOfMax = min(minOfMax, s[1])

        if maxOfMin <= minOfMax:
            cnt += 1
            for Si in S:
                Si.pop(0)
        else:
            for Si in S:
                if Si[0][1] < maxOfMin:
                    Si.pop(0) 
                

def test():
    print('test mode')
    assert f(2, 1,[500, 300], [[900],[660]]) == 1
    assert f(2, 1,[500, 300],[[1500],[809]]) == 0
    assert f(2, 2,[50, 100],[[450, 449],[1100, 1101]]) == 1
    assert f(2, 1, [500, 300],[[300],[500]]) == 0 
    assert f(1, 8, [10], [[11, 13, 17, 11, 16, 14, 12, 18]]) == 3
    assert f(3, 3, [70, 80, 90],
             [[1260, 1500, 700],
              [800, 1440, 1600],[1700, 1620, 900]]) == 3

def main():
    numOfTestCase = int(input())
    t0 = time.time()

    for testCase in range(numOfTestCase):
        N, P = map(int, input().split())
        R = list(map(int, input().split()))
        Q = [list(map(int, input().split())) for i in range(N)]

        t1 = time.time()
        print('Case #' + str(testCase+1) + ':', f(N,P,R,Q))

        if numOfTestCase >= 10:
            t2 = time.time()

            print('... #' + str(testCase+1) + '/' + str(numOfTestCase),
                  '{0:.2f}'.format(t2 - t1),
                  '{0:.2f}'.format(t2 - t0),
                  file=sys.stderr)
    

main()
