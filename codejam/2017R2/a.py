#  --*-coding:utf-8-*--

import sys
import time

def f(N, P, G):
    assert len(G) == N
    assert P >= 2
    assert P <= 4

    if P == 2:
        return g2(G)
    elif P == 3:
        return g3(G)
    elif:
        return g4(G)


def g2(G):
    n0, n1 = countMod(G, 2)
    return n0 + n1//2 + sum(G)%2


def g3(G):
    n0, n1, n2 = countMod(G, 3)
    m0 = min(n1, n2)
    m1 = n1 + n2 - 2*m0

    return n0 + m0 + m1//3 + (1 if sum(G)%3>0 else 0)


def g4(G):
    n0, n1, n2, n3 = countMod(G, 4)
    m0 = min(n1, n3)
    m1 = n1 + n3 - 2*m0

    return (n0 + m0 + n2//2 + m1//4 + 
            (1 if n2%2>0 and m1%4>=2 else 0) +
            (1 if sum(G)%4>0 else 0))
    

def countMod(G, P):
    counts = [0]*P

    for g in G:
        counts[g%P] += 1

    return counts



def main():
    numOfTestCase = int(input())
    t0 = time.time()

    for testCase in range(numOfTestCase):
        N, P = map(int, input().split())
        G = list(map(int, input().split()))
        assert len(G) == N

        t1 = time.time()
        print('Case #' + str(testCase+1) + ':', f(N, P, G))

        if numOfTestCase >= 10:
            t2 = time.time()

            print('... #' + str(testCase+1) + '/' + str(numOfTestCase),
                  '{0:.2f}'.format(t2 - t1),
                  '{0:.2f}'.format(t2 - t0),
                  file=sys.stderr)
    
if __name__ == '__main__':
    main()

