#  --*-coding:utf-8-*--

import sys
import time
import heapq

INF = float('inf')

def warshall(D):
    n = len(D)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])



def dijkstra(G, st):
    n  = len(G)
    D = [INF]*n
    D[st] = 0
    prevs = [None]*n
    
    Q = [(0, st)]

    while len(Q) > 0:
        d, nodeId = heapq.heappop(Q)
        
        if d > D[nodeId]:
            continue
        
        for destId, length in G[nodeId]:
            d2 = d + length
            if D[destId] > d2:
                D[destId] = d2
                prevs[destId] = nodeId
                heapq.heappush(Q, (d2, destId))
                
    return D


def f(N, Q, ES, D, UV):
    for i in range(N):
        for j in range(N):
            d = D[i][j]
            D[i][j] = 0 if i == j else INF if d == -1 else d

    warshall(D)

    G = []
    for i, (e, s) in enumerate(ES):
        G.append([(j, d/s)  for j, d in
                  filter(lambda x: x[1]<=e, enumerate(D[i]))])
    
    
    return [dijkstra(G, u-1)[v-1] for u, v in UV]

        

def main():
    numOfTestCase = int(input())
    t0 = time.time()

    for testCase in range(numOfTestCase):
        N, Q = map(int, input().split())
        ES = [list(map(int, input().split())) for i in range(N)]
        D = [list(map(int, input().split())) for i in range(N)]
        UV = [list(map(int, input().split())) for i in range(Q)]

        t1 = time.time()
        print('Case #' + str(testCase+1) + ':', 
              ' '.join(map('{0:.6f}'.format, f(N, Q, ES, D, UV))))

        if numOfTestCase >= 10:
            t2 = time.time()

            print('... #' + str(testCase+1) + '/' + str(numOfTestCase),
                  '{0:.2f}'.format(t2 - t1),
                  '{0:.2f}'.format(t2 - t0),
                  file=sys.stderr)

    
if __name__ == '__main__':
    main()

    
