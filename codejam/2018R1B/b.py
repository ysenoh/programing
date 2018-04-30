#!/usr/bin/python3
#  --*-coding:utf-8-*--

# これは正答してない。

def f(DAB):
    M = [x[0]+x[1] for x in DAB]
    N = [x[0]-x[2] for x in DAB]

    x = None
    maxLen = 0
    cnt = 0
    Q = set()

    for i, m in enumerate(M):
        if x != m:
            t1 = g(M, i)
            t2 = g(N, i+t1)
            Q.add((i, t1+t2))
            
            if t1 + t2 > maxLen:
                cnt = 1
                maxLen = t1 + t2
            elif t1 + t2 == maxLen:
                cnt += 1

            x = m

    x = None
    for i, n in enumerate(N):
        if x != n:
            t1 = g(N, i)
            t2 = g(M, i+t1)
            
            if (i, t1+t2) in Q:
                continue

            if t1 + t2 > maxLen:
                cnt = 1
                maxLen = t1 + t2
            elif t1 + t2 == maxLen:
                cnt += 1

            x = n

    return (maxLen, cnt)



def g(X, n):
    if n >= len(X):
        return 0
    
    x = X[n]
    cnt = 1

    for i in range(n+1, len(X)):
        if X[i] != x:
            break

        cnt += 1

    return cnt



def main():
    T = int(input())

    for i in range(T):
        S = int(input())
        DAB = [tuple(map(int, input().split())) for i in range(S)]

        x, y = f(DAB)
        print('Case #' + str(i+1) + ':', x, y)


if __name__ == '__main__':
    main()

        
        
