#  --*-coding:utf-8-*--

# AtCoder Beginner Contest 076
# B - Addition and Multiplication
# http://abc076.contest.atcoder.jp/tasks/abc076_b

def f(N, K):
    b = min(K.bit_length(), N)
    return 2**b + (N-b)*K


def test():
    assert f(4,3) == 10
    assert f(10,10) == 76


def main():
    N = int(input())
    K = int(input())
    print(f(N, K))


if __name__ == '__main__':
    main()
