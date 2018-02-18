#  --*-coding:utf-8-*--

def getPrimesAndDivs(n):
    primes = []
    divs = [1]
    p = 2

    while n >= p**2:
        c = 0
        while n%p == 0:
            c += 1
            n //= p

        if c > 0:
            primes.append(p)
            addDivsTo(divs, p, c)

        p += 2 if p>2 else 1

    if n > 1:
        primes.append(n)
        addDivsTo(divs, n, 1)

    return primes, divs



def addDivsTo(divs, p, c):
    curDivs = divs[:]
    p2 = 1

    for i in range(1, c+1):
        p2 *= p
        divs.extend(
            map(lambda x: x*p2, curDivs))



# 1からnまでのうち、mと互いに素である値の和
# primesは、少なくともmの素因数を全て含む
def g(n, m, primes, index=0):
    if n == 0:
        return 0

    s = n*(n+1)//2
    
    for i in range(index, len(primes)):
        p = primes[i]

        if m%p == 0:
            s -= g(n//p, m//p, primes, i+1)*p
    
    return s
        
            
def f(n, k):
    primes, divs = getPrimesAndDivs(k)
    return sum(g(n//d, k//d, primes) for d in divs)


def main():
    n, k  = map(int, input().split())
    print(f(n, k))


if __name__ == '__main__':
    main()
