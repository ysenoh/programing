
def getOddDivsOf(n):
    while n%2 == 0:
        n //= 2

    divs = [1]
    p = 3

    while p**2 <= n:
        c = 0
        while n%p == 0:
            n //= p
            c += 1

        if c > 0:
            addToDivs(divs, p, c)

        p += 2
    
    if n > 1:
        addToDivs(divs, n, 1)

    return divs
    

def addToDivs(divs, p, c):
    curDivs = divs[:]

    for i in range(c):
        p2 = p**(i+1)
        divs.extend(map(lambda x: x*p2, curDivs))


def getPairs(n):
    pairs = []

    for d in getOddDivsOf(n):
        assert d%2 == 1

        x = d
        y = 2*n//d

        if x < y:
            x, y = y, x

        assert x-y+1 > 0

        pairs.append(((x-y+1)//2, (x+y+1)//2))

    return pairs


def g(n):
    pairs = getPairs(n)
    
    return bool(set(pair[0] for pair in pairs) &
                set(pair[1] for pair in pairs))


def f(n):
    n2 = 0
    i = 0

    while n2 < n:
        i += 1
        if g(i):
            n2 += 1

    return i
        

def main():
    n = int(input())
    print(f(n))


if __name__ == '__main__':
    main()

