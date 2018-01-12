#  --*-coding:utf-8-*--

# AtCoder Regular Contest 085
# C - HSI
# http://arc085.contest.atcoder.jp/tasks/arc085_a

def f(n, m):
    return (1800*m + 100*n)*2**m

def test():
    assert f(1,1) == 3800
    assert f(10, 2) == 18400
    assert f(100, 5) == 608000

def main():
    n, m = map(int, input().split())
    print(f(n,m))


if __name__ == '__main__':
    main()
