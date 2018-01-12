#  --*-coding:utf-8-*--

# 自然数を 1 から順に書き並べ、3 の数字が現れる回数を数える。
# 自然数 n に対し、ちょうど n 個の 3 の数字が現れたときに
# 書いている数を求めよ。

# n 
# m 既に使用されている3の個数
# d 桁数

def g(n, m, d):
    if d == 0:
        return 0

    k = m*10**(d-1) + ((d-1)*10**(d-2) if d >= 2 else 0)

    for i in range(10):
        k2 = k + (10**(d-1) if i == 3 else 0)

        if k2 >= n:
            if i == 3:
                m += 1

            return (i*10**(d-1) + g(n, m, d-1))

        n -= k2

    assert(False)

def f(n):
    d = 1
    while d*10**(d-1) < n:
        d += 1

    return g(n, 0, d)


print(f(int(input())))

