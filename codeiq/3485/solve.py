#  --*-coding:utf-8-*--

def C(n, m):
    x = 1
    
    for i in range(m):
        x *= (n-i)/(i+1)

    return x


def f(n, k):
    if (n-k)%2 != 0:
        return 0
    
    return int((C(n, k)* 2**k * C(n-k, (n-k)//2))/C(2*n, n)*1e6)


def test():
    assert f(1, 0) == 0
    assert f(1, 1) == int(1e6)
    assert f(2, 0) == int((1/3)*1e6)
    assert f(2, 1) == 0
    assert f(2, 2) == 666666
    assert f(4, 2) == 685714


def main():
    n, k = map(int, input().split())
    print(f(n, k))

if __name__ == '__main__':
    main()
