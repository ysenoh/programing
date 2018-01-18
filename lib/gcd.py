def gcd(n, m):
    assert n > 0
    assert m > 0

    while m > 0:
        n, m = m, n%m

    return n
