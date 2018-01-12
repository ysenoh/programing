#  --*-coding:utf-8-*--

# Ford-Fulkerson algorithm

def fulkerson(graph, src, sink):
    n = len(graph)

    matrix = [[0]*n for i in range(n)]
    bothDirGraph = [[] for i in range(n)]

    for nodeId, edges in enumerate(graph):
        for nodeId2, flowLimit in edges:
            matrix[nodeId][nodeId2] = flowLimit
            bothDirGraph[nodeId].append(nodeId2)
            bothDirGraph[nodeId2].append(nodeId)

    while True:
        path = findPath(bothDirGraph, matrix, src, sink)

        if path == None:
            break

        v = min(matrix[path[i]][path[i+1]] 
                for i in range(len(path)-1))

        for i in range(len(path)-1):
            node1 = path[i]
            node2 = path[i+1]
            
            matrix[node1][node2] -= v
            matrix[node2][node1] += v

    return (sum(c for _, c in graph[src]) - 
            sum(c for c in matrix[src]))


def findPath(bothDirGraph, matrix, src, sink):
    prevs = [None]*len(matrix)
    q = set([src])
    prevs[src] = src

    while len(q) > 0:
        node = q.pop()

        for nextNode in bothDirGraph[node]:
            if prevs[nextNode] == None and matrix[node][nextNode] > 0:
                prevs[nextNode] = node
                
                if nextNode == sink:
                    path = []
                    pathNode = sink

                    while pathNode != src:
                        path.append(pathNode)
                        pathNode = prevs[pathNode]

                    path.append(src)
                    return list(reversed(path))

                q.add(nextNode)

    return None
                    

def test():
    # u -> v の容量が c 
    # graph[u] = [(v,c)]

    graph = [
        [(1, 10), (2, 5)],
        [(2, 10), (3, 9)],
        [(4, 10)],
        [(4, 9)],
        []]


    print(fulkerson(graph, 0, 4))
     

if __name__ == '__main__':
    test()
