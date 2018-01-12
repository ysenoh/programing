#  --*-coding:utf-8-*--

# 自然数 n に対し、関数 Fn(x) を次のように定義する
# Fn(x) = floor(4x(n-x)/n)
# 変換を繰り返したときに、今までに出た値が再度現れるまでの変換回数を 
# G(n, k) と定義します。
# 0 以上 n 以下の全ての整数 k に対する G(n, k) の和を H(n) と定義します。
# H(n)を求めよ

# 有向グラフのうち、参照されていない端っこから、その個数とパスの長さを
# カウントし、残ったものはループになっているはずなので、その長さを求めて
# 足し合わせている。

def g(n):
    nextNodes = [4*x*(n-x)//n for x in range(n+1)]
    refCnts = [0]*(n+1)

    for y in nextNodes:
        refCnts[y] += 1

    q = set(filter(lambda x: refCnts[x] == 0, range(n+1)))
    ss = [[0,0] for i in range(n+1)]

    while len(q) > 0:
        node = q.pop()
        nextNode = nextNodes[node]

        s1 = ss[node]
        s2 = ss[nextNode]

        s2[0] += s1[0] + 1
        s2[1] += s1[1] + s1[0] + 1

        refCnts[nextNode] -= 1

        if refCnts[nextNode] == 0:
            q.add(nextNode)

    q = set(filter(lambda x: refCnts[x] > 0, range(n+1)))
    a = 0

    while len(q) > 0:
        node = q.pop()

        numOfNodes = 0
        cnt = 0

        while True:
            s = ss[node]
            a += s[1]
            numOfNodes += s[0] + 1
            cnt += 1
            
            node = nextNodes[node]
            if not node in q:
                break
                
            q.remove(node)

        a += numOfNodes*cnt

    return a

print(g(int(input())))

        

        


    
