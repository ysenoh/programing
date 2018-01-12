#  --*-coding:utf-8-*--

# 全員が横一列に並んだときに、隣の人とは異なる仮装をすることにした。
# m 人が仮装をしたとき、衣装の数がちょうど n 種類である「並び方」が
# 何通りあるかを求めよ。

def memoize(f):
    cache = {}
    def helper(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return helper


@memoize
def f(m, n):
    x = n*(n-1)**(m-1)
    
    p = n
    for k in range(2, n):
        p = p*(n-k+1)
        x -= p*f(m, k)

    return x//p

def test():
    assert(f(5,3) == 7)


def main():
    m, n = map(int, input().split())
    print(f(m, n))


if __name__ == '__main__':
    main()
