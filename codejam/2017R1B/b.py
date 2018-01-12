#  --*-coding:utf-8-*--

import sys
import time
import re


def f(N, R, O, Y, G, B, V):
    if R == G and B == 0 and O == 0 and Y == 0 and V == 0:
        return 'RG'*R

    elif B == O and R == 0 and G == 0 and Y == 0 and V == 0:
        return 'BO'*B

    elif Y == V and R == 0 and G == 0 and B == 0 and O == 0:
        return 'YV'*Y

    if R<=G and G>0 or B<=O and O>0 or Y<=V and V>0:
        return 'IMPOSSIBLE'
        
    assert R>G or G==0
    assert B>O or O==0
    assert Y>V or V==0

    C = sorted([(R-G, 'R'), (B-O, 'B'), (Y-V, 'Y')])
    
    n3 = C[0][0] + C[1][0] - C[2][0]

    if n3 < 0:
        return 'IMPOSSIBLE'

    str = ((C[2][1] + C[1][1] + C[0][1])*n3 +
           (C[2][1] + C[1][1])*(C[1][0]-n3) +
           (C[2][1] + C[0][1])*(C[0][0]-n3))

    str = re.sub(r'R', 'RG'*G + 'R', str, 1)
    str = re.sub(r'B', 'BO'*O + 'B', str, 1)
    str = re.sub(r'Y', 'YV'*V + 'Y', str, 1)

    assert len(str) == N

    return str


def main():
    numOfTestCase = int(input())
    t0 = time.time()

    for testCase in range(numOfTestCase):
        N, R, O, Y, G, B, V = map(int, input().split())

        t1 = time.time()
        print('Case #' + str(testCase+1) + ':', f(N, R, O, Y, G, B, V))

        if numOfTestCase >= 10:
            t2 = time.time()

            print('... #' + str(testCase+1) + '/' + str(numOfTestCase),
                  '{0:.2f}'.format(t2 - t1),
                  '{0:.2f}'.format(t2 - t0),
                  file=sys.stderr)
    
if __name__ == '__main__':
    main()

