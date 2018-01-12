#  --*-coding:utf-8-*--
import sys

sys.setrecursionlimit(10000)

MOD = 1000003

def memoize(f):
    cache = {}
    def helper(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return helper


def f(n, a, b):
    minOfB = max((n - a + 1)//2, 0)
    maxOfB = min(b, n//2)

    return sum(g(n-2*i, i) for i in range(minOfB, maxOfB+1))%MOD
    

@memoize
def g(a, b):
    if a == 0 or b == 0:
        return 1

    return (g(a-1, b) + g(a, b-1))%MOD


def test():
    assert f(6, 4, 2) == 11
    assert f(4, 3, 1) == 3
    assert f(4, 4, 4) == 5
    assert f(5, 2, 1) == 0
    assert f(10, 5, 3) == 35
    assert f(100, 50, 50) == 765461


def main():
    n, a, b = map(int, input().split())
    print(f(n, a, b))


if __name__ == '__main__':
    main()
