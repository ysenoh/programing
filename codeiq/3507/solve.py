#  --*-coding:utf-8-*--

def memoize(f):
    cache = {}
    def helper(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return helper


prices = [
    1, 2, 3, 5, 10, 20, 30, 50, 62, 82, 92,
    100, 120, 140, 205, 280, 310, 500, 1000]


@memoize
def f(x, k):
    if x == 0:
        return 1
    if k >= len(prices) or x < prices[k]:
        return 0
    else:
        return sum(f(x - prices[i], i + 1)
                   for i in range(k, len(prices)))


def test():
    assert f(70,0) == 5


def main():
    x = int(input())
    print(f(x, 0))


if __name__ == '__main__':
    main()

    




