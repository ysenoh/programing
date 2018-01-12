#  --*-coding:utf-8-*--

def getPrimes(n):
    """ n以下の素数を配列で戻す関数
    """

    if (n < 2):
        return []

    flags = [False]*(n+1)
    primes = [2]

    for p in range(3, n+1, 2):
        if not flags[p]:
            primes.append(p)
            for k in range(p**2, n+1, p):
                flags[k] = True

    return primes

