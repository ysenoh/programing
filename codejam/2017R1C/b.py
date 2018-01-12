#  --*-coding:utf-8-*--

import sys
import time

def f(T1, T2):
    T = sorted(list(map(lambda x: x + ('A',), T1)) +
               list(map(lambda x: x + ('B',), T2)))

    AA, BB = [], []
    cnt = 0

    for i in range(len(T)):
        t1, t2 = T[i], T[(i+1)%len(T)]

        if t1[2] != t2[2]:
            cnt += 1
        elif t1[2] == 'A':
            AA.append((t2[0] - t1[1])%1440)
        else:
            BB.append((t2[0] - t1[1])%1440)

    cnt += (len(AA) + len(BB))*2

    sumOfA = sum(t[1] - t[0] for t in T1)
    sumOfB = sum(t[1] - t[0] for t in T2)

    for t in sorted(AA):
        if sumOfA + t > 720:
            break

        sumOfA += t
        cnt -= 2

    for t in sorted(BB):
        if sumOfB + t > 720:
            break

        sumOfB += t
        cnt -= 2

    return cnt
    

def main():
    numOfTestCase = int(input())
    t0 = time.time()

    for testCase in range(numOfTestCase):
        A, B = map(int, input().split())
        T1 = [tuple(map(int, input().split())) for i in range(A)]
        T2 = [tuple(map(int, input().split())) for i in range(B)]

        t1 = time.time()
        print('Case #' + str(testCase+1) + ':',f(T1, T2))

        if numOfTestCase >= 10:
            t2 = time.time()

            print('... #' + str(testCase+1) + '/' + str(numOfTestCase),
                  '{0:.2f}'.format(t2 - t1),
                  '{0:.2f}'.format(t2 - t0),
                  file=sys.stderr)
    


if __name__ == '__main__':
    main()
