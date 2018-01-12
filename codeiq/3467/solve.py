#  --*-coding:utf-8-*--

def memoize(f):
    cache = {}
    def helper(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return helper


@memoize
def g(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1

    return (g(n-2) + 2*g(n-3) + 3*g(n-4) + 
            2*g(n-5) + g(n-6))


def f(n):
    return sum(g(n-i-1) for i in range(3))


def test():
    assert(f(5) == 7)

if __name__ == '__main__':
    print(f(int(input())))
