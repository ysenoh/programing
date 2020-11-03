def dsMakeSet(ds, x):
    ds[x] = x


def dsFind(ds, x):
    if ds[x] == x:
        return x

    x0 = x
    while ds[x] != x:
        x = ds[x]

    ds[x0] = x
    return x


def dsUnion(ds, x, y):
    xRoot = dsFind(ds, x)
    yRoot = dsFind(ds, y)
    
    if xRoot != yRoot:
        ds[yRoot] = xRoot
        return True

    return False



N = int(input())
XY = [tuple(map(int, input().split())) for _ in range(N)]

D =sorted([((XY[i][0] - XY[j][0])**2 + (XY[i][1] - XY[j][1])**2, i+2, j+2)
          for i in range(N) for j in range(i+1, N)] +
         [((100-XY[i][1])**2, i+2, 0) for i in range(N)] +
         [((100+XY[i][1])**2, i+2, 1) for i in range(N)] )
         
ds = [i for i in range(N+2)]

lastD = None
for d in D:
    dsUnion(ds, d[1], d[2])
    if dsFind(ds, 0) == dsFind(ds, 1):
        break;

    lastD = d[0]

print('{:.9f}'.format(d[0]**.5/2))

    








