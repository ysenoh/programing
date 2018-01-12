#  --*-coding:utf-8-*--

# CodeIQ 3460 今週のお題：スイッチを反転しても同じ数だけ点灯する？
# 1つのブレーカーは２つのスイッチとつながっており、各スイッチには
# 1つの電球がつながっている。
# 今、m 個のブレーカーがあり、n 個の電球が点灯している。
# ここで、すべてのスイッチを反転させたとき、点灯している電球の数が同じであった。
# このようなブレーカー、スイッチの状態が何通りあるか求めなさい。

def combin(n,r):
    x = 1
    for i in range(1, r+1):
        x = x*(n-i+1)//i

    return x


def f(m, n):
    # a ... ブレーカー off
    # b ... ブレーカー on スイッチ両方共on
    # c ... ブレーカー on スイッチ一方のみon
    # ブレーカー on スイッチ両方共off は bと等しい

    if m < n:
        return 0

    a = m - n
    x = 0

    for b in range(n//2 + 1):
        c = n - 2*b
        assert a + 2*b + c == m
        
        m2 = m
        p = 1

        for i in [a, b, c]:
            p *= combin(m2, i)
            m2 -= i

        x += p * 2**c

    return 4**a * x

m, n = map(int, input().split())
print(f(m, n))

