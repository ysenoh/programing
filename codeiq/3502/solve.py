#  --*-coding:utf-8-*--

def f(n):
    if n <= 3:
        return n//2 + 1

    return g(n, 2, 2, 0b11, 1, n//2 + 1)


def g(n, k, cnt, p, q, limit):
    # p 目盛りのビットイメージ
    # q 測定できる長さのビットイメージ

    assert cnt < limit
    
    if q == (1 << n//2) - 1:
        return cnt

    if cnt + 1 >= limit:
        return limit
    
    assert cnt + 1 < limit

    for i in range(k, n):
        q2 = q
        for j in range(k):
            assert i - j > 0
            assert i - j < n

            if p & (1<<j):
                q2 |= (1 << (min(i-j, n-(i-j)) - 1))

        limit2 = g(n, i+1, cnt+1, p|(1<<i), q2, limit)
        assert limit2 <= limit

        limit = limit2

        if limit == cnt+1:
            break

    return limit


def test():
    assert f(10) == 4


def main():
    n = int(input())
    print(f(n))


if __name__ == '__main__':
    main()
