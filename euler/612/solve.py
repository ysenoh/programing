#  --*-coding:utf-8-*--

# Project Euler Problem 612: Friend numbers
# https://projecteuler.net/problem=612

#　friendであるのは　
# 1) 0を含む数字を持つのペア
# 2) 0以外の同じ数字を持つペア
#   2.1) 一方は0を持つが、もう一方は0を持たない
#   2.2) 両方共0を持たない

MOD = 1000267129

def memoize(f):
    cache = {}
    def helper(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return helper


def modPow(x, n):
    y = 1

    while(n > 0):
        if n%2 == 1:
            y = y*x%MOD
        
        x = x**2%MOD
        n //= 2

    return y


def g1(n, m):
     """ n桁まで 0からmまでの数値が使用されているパターン数、
     先頭の数値は0ではない。
     """

     return (m*h(n-1, m, 10) + (9 - m)*h(n-1, m+1, 10))%MOD


def g2(n, m):
     """ n桁まで 1からmまでの数値が使用されているパターン数、
     先頭の数値は0ではない。
     """
     
     return (m*h(n-1, m-1, 9) + (9 - m)*h(n-1, m, 9))%MOD


@memoize
def h(n, m, r):
    """n桁までで、あるm種類の数値が使用されているパターン数。
    各桁には r種類の数字を使用できる。
    (つまり r=10の場合は0も使用できる)
    """

    a = 0

    for k in range(0, n+1):
        c = 1

        for i in range(0, m+1):
            a += (-1)**i * c * modPow(r-i, k)
            a %= MOD
            c = c*(m-i)//(i+1)

    return a


def f(n):
    n1 = g1(n, 0)

    x = n1*(n1-1)//2
    x %= MOD

    c = 1
    for i in range(1, 10):
        c = c*(10-i)//i
        n1 = g1(n, i)
        n2 = g2(n, i)

        x += (-1)**(i+1)*(n1*n2 + n2*(n2-1)//2)%MOD*c%MOD
        x %= MOD

    return x


print(f(18)) 

