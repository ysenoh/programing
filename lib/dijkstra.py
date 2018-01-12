#  --*-coding:utf-8-*--

import heapq

INF = float('inf')

def dijkstra(graph, st):
    n  = len(graph)
    ds = [INF]*n
    ds[st] = 0
    prevs = [None]*n
    
    qs = [(0, st)]

    while len(qs) > 0:
        d, nodeId = heapq.heappop(qs)
        
        if d > ds[nodeId]:
            continue
        
        for destId, length in graph[nodeId]:
            d2 = d + length
            if ds[destId] > d2:
                ds[destId] = d2
                prevs[destId] = nodeId
                heapq.heappush(qs, (d2, destId))
                
    return (ds, prevs)


def test():
    # u -> v の距離が d
    # graph[u] = [(v, d)]

    graph = [[(1, 7), (2, 14), (3, 9)],
             [(3, 10), (4, 15)],
             [(3, 2), (5, 9)],
             [(4, 11)],
             [(5, 6)],
             []]

    print(dijkstra(graph, 0))


if __name__ == '__main__':
    test()
