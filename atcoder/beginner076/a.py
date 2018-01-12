#  --*-coding:utf-8-*--

# AtCoder Beginner Contest 076
# A - Rating Goal
# http://abc076.contest.atcoder.jp/tasks/abc076_a

def f(R, G):
    return 2*G-R

def test():
    assert f(2002, 2017) == 2032
    assert f(4500, 0) == -4500

def main():
    R = int(input())
    G = int(input())

    print(f(R,G))


if __name__ == '__main__':
    main()
