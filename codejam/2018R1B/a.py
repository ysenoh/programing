#!/usr/bin/python3
#  --*-coding:utf-8-*--


def f(N, C):
    a = 100//N
    b = 100%N
    N2 = (N+1)//2

    x = a*N
    D = []

    for c in C:
        x += b*c//N
        t = b*c%N

        if t >= N2:
            x += 1
        else:
            D.append(t)

    remain = N - sum(C)

    if b >= N2:
        x += remain
    elif b > 0:
        for d in reversed(sorted(D)):
            k = (N2 - d + b - 1)//b
            if k <= remain:
                x += 1
                remain -= k

        k = (N2 + b - 1)//b
        x += remain//k

    return x


def main():
    T = int(input())

    for i in range(T):
        N, L = map(int, input().split())
        C = list(map(int, input().split()))

        print('Case #' + str(i+1) + ': ' + str(f(N, C)))


if __name__ == '__main__':
    main()

        
        
