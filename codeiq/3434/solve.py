#  --*-coding:utf-8-*--

def getPrimes(n):
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


def sumOfOne(n):
    """ 1 <= x < y <= n を満たす x y に対して 1 の和を求める
    """
    return n*(n-1)//2


def sumOfSum(n):
    """ 1 <= x < y <= n を満たす x y に対して x+y の和を求める
    """
    return n*(n+1)*(n-1)//2


def sumOfMult(n):
    """ 1 <= x < y <= n を満たす x y に対して x*y の和を求める
    """
    return n*(n+1)*(n-1)*(3*n+2)//24


def g(n, k):
    # 1 < b <= [n/3]   .. 2ab
    # [n/3] < b <= [n/2] .. -n^2 + 3(a+b)n - 7ab
    # [n/2] < b <= n-1 .. n^2 - (a+b)n + ab

    n1 = n//(3*k)
    n2 = n//(2*k)
    n3 = (n-1)//k

    s1 = 2*k**2*sumOfMult(n1)

    s2 = (-n**2*(sumOfOne(n2) - sumOfOne(n1))
          + 3*k*n*(sumOfSum(n2) - sumOfSum(n1))
          - 7*k**2*(sumOfMult(n2) - sumOfMult(n1)))

    s3 = (n**2*(sumOfOne(n3) - sumOfOne(n2))
          - k*n*(sumOfSum(n3) - sumOfSum(n2))
          + k**2*(sumOfMult(n3) - sumOfMult(n2)))

    return s1 + s2 + s3


def h(n, k, primes, primeIndex):
    s = 0
    
    for i in range(primeIndex, len(primes)):
        p = primes[i]
        k2 = k*p

        if k2*2 >= n:
            break

        s += g(n, k2) - h(n, k2, primes, i+1)

    return s


def f(n):
    if n == 2:
        return 6
    
    primes = getPrimes(n//2)
    return (g(n, 1) - h(n, 1, primes, 0))*4 + 4
    

def test():
    print("Test mode")
    assert f(3) == 12
    assert f(4) == 48
    assert f(5) == 108
    assert f(6) == 248
    assert f(7) == 428
    assert f(10) == 1900


def main():
    n = int(input())
    print(f(n))

if __name__ == '__main__':
    main()
