#  --*-coding:utf-8-*--

def getNextPrimes(n):
    nextPrimes = [None]*(n+1)
    lastPrime = 2

    for i in range(3, n+1, 2):
        if nextPrimes[i] == None:
            for j in range(lastPrime+1, i+1):
                nextPrimes[j] = i

            lastPrime = i
            for j in range(i**2, n+1, i):
                nextPrimes[j] = True
                
    for i in range(lastPrime+1, n+1):
        nextPrimes[i] = None

    return nextPrimes


def g(nextPrimes, d, n):
    assert d > 0

    cnt = 0
    p = 2

    while p != None and cnt <= n:
        cnt += 1
        p = nextPrimes[p+d] if p+d<len(nextPrimes) else None

    return cnt


def f(m, n):
    nextPrimes = getNextPrimes(m)
    dMin, dMax = 0, m
    
    while True:
        dMid = (dMin + dMax)//2
        if dMid == dMin:
            break

        n2 = g(nextPrimes, dMid, n)
        
        if n2 >= n:
            dMin = dMid
        else:
            dMax = dMid
            
    return dMin

    
def test():
    assert f(30, 4) == 8


def main():
    m,n = map(int, input().split())
    print(f(m, n))


if __name__ == '__main__':
    main()
