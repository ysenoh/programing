#  --*-coding:utf-8-*--

FACTOR = 1 + 1e-10

def f(n):
    a = [0]*(n+1)

    for x in range(1, int(n**(1/3)*FACTOR) + 1):
        m = n//x
        for y in range(x, int(m**(1/2)*FACTOR) + 1):
            for z in range(y, m//y + 1):
                s = x*y*z
                a[s] += 1

    return sum(g(a, x, y, n - x - y)
               for x in range(1, n//3+1) 
               for y in range(x, (n-x)//2+1))


def g(a, x, y, z):
    if x == y:
        p = a[x]

        if y == z:
            return p*(p+1)*(p+2)//6
        else:
            return p*(p+1)*a[z]//2
    elif y == z:
        p = a[y]
        return p*(p+1)*a[x]//2
    else:
        return a[x]*a[y]*a[z]
        

def test():
    assert f(10) == 16

def main():
    n = int(input())
    print(f(n))


if __name__ == '__main__':
    main()
