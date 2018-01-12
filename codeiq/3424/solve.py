#  --*-coding:utf-8-*--

# https://codeiq.jp/q/3424
# 問題: すべて1オームの抵抗が n 個あります。
# これらを直列または並列に組み合わせて合成抵抗を作ることを考えます。
# できる合成抵抗の値が何通りあるかを求めてください。

def gcd(n, m):
    while(m > 0):
        n,m = m, n%m
    
    return n


def memoize(f):
    cache = {}
    def helper(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return helper


@memoize
def f(n, m):
    assert n >= m
    assert m >= 1

    if m == 1:
        return [set([(n,1)]), set([(1,n)])]

    assert m >= 2
    assert n >= 2
        
    s, p = f(n, m-1)

    if n == m:
        x = s | p
        return [x, x]

    assert n > m
    assert n - m >= 1

    s1, p1 = f(m, m-1)
    s2, p2 = f(n-m, min(m,n-m))

    s, p = set(s), set(p)
    
    for r1 in p1:
        for r2 in s2:
            a = r1[0]*r2[1] + r1[1]*r2[0]
            b = r1[1]*r2[1]
            c = gcd(a, b)
            s.add((a//c, b//c))

    for r1 in s1:
        for r2 in p2:
            a = r1[0]*r2[1] + r1[1]*r2[0]
            b = r1[0]*r2[0]
            c = gcd(a, b)
            p.add((b//c, a//c))
            

    return [s, p]
    

n = int(input())
print(len(f(n, n)[0]))
    
