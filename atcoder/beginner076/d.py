#  --*-coding:utf-8-*--

# AtCoder Beginner Contest 076
# D - AtCoder Express
# http://abc076.contest.atcoder.jp/tasks/abc076_d

def f(n, ts, vs):
    sumOfT = sum(ts)

    t = 0
    k = 0
    k1s = [k]

    for i in range(n-1):
        t += ts[i]
        k = min(k, vs[i] - t)
        k1s.append(k)

    t = sumOfT
    k = t
    k2s = [k]

    for i in range(n-1, 0, -1):
        t -= ts[i]
        k = min(k, vs[i] + t)
        k2s.insert(0, k)

    t0 = 0
    d = 0

    for t, v, k1, k2  in zip(ts, vs, k1s, k2s):
        # t0 制限速度がv である開始時刻
        # t1 加速を終わらせる時刻
        # t2 減速を始める時刻
        # t3 制限速度がv である終了時刻

        t3 = t0 + t

        t1 = v - k1
        t2 = k2 - v
        
        if t1 > t2:
            t1 = (k2 - k1)/2
            t2 = t1

        if t0 < t1:
            t12 = min(t1, t3)
            d +=  k1*(t12-t0) + (t12**2 -t0**2)/2

        dt = min(t2, t3) - max(t0, t1)
        if dt > 0:
            d += v*dt

        if t2 < t3:
            t22 = max(t2, t0)
            d +=  k2*(t3-t22) - (t3**2 - t22**2)/2

        t0 = t3
        
    return d


def test():
    assert(f(1, [100], [30]) == 2100)
    assert(f(2, [60,50], [34,38]) == 2632)
    assert(f(3, [12, 14, 2], [6, 2, 7]) == 76)
    assert(f(1, [9], [10]) == 20.25)
    assert(f(10,[64, 55, 27, 35, 76, 119, 7, 18, 49, 100],[29, 19, 31, 39, 27, 48, 41, 87, 55, 70]) == 20291)


def main():
    n = int(input())
    ts = list(map(int, input().split()))
    vs = list(map(int, input().split()))

    print('{0:.4f}'.format(f(n, ts, vs)))

if __name__ == '__main__':
    main()


