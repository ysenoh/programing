#!/usr/bin/python3
#  --*-coding:utf-8-*--

# 間違っている。


import math

def f(N,P, WHs):
    a = sum(2*(w+h) for w, h in WHs)
    if a >= P:
        return a

    w, h = WHs[0]

    d1 = 2*min(w, h)
    d2 = 2*math.sqrt(w**2 + h**2)
    
    n2 = (P-a)//d1
    if a + n2*d2 >= P:
        return P

    return a+n2*d2



def main():
    T = int(input())

    for i in range(T):
        N,P = map(int, input().split())
        WHs = [tuple(map(int, input().split())) for i in range(N)]

        print('Case #' + str(i+1) + ': ' + '{0:.7f}'.format(f(N,P,WHs)))


if __name__ == '__main__':
    main()
