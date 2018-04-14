#!/usr/bin/python3
#  --*-coding:utf-8-*--



def f(R,B,C,MSPs):
    t = 1
    while(g(MSPs, R, t) < B):
        t *= 2

    t0 = t//2
    t1 = t

    while(t0+1 < t1):
        t = (t0+t1)//2
        y = g(MSPs, R, t)
        
        if y < B:
            t0 = t
        else:
            t1 = t

    return t1


def g(MSPs, R, t):
    ns = sorted([max(min((t-p)//s, m),0) for m, s, p in MSPs])
    return sum(ns[-R:])




def main():
    T = int(input())

    for i in range(T):
        R,B,C = map(int, input().split())
        MSPs = [tuple(map(int, input().split())) for i in range(C)]

        print('Case #' + str(i+1) + ': ' + str(f(R,B,C,MSPs)))


if __name__ == '__main__':
    main()
