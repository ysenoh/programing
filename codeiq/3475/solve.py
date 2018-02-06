#  --*-coding:utf-8-*--

import sys

def dsMakeSet(ds, x):
    ds[x] = x


def dsFind(ds, x):
    while ds[x] != x:
        x = ds[x]

    return x


def dsUnion(ds, x, y):
    xRoot = dsFind(ds, x)
    yRoot = dsFind(ds, y)
    
    if xRoot != yRoot:
        ds[yRoot] = xRoot
        return True

    return False


def f(lines):
    cellss = [list(line.rstrip()) for line in lines]
    ds = {}
    cnt = 0

    for i, cells in enumerate(cellss):
        for j, cell in enumerate(cells):

            if cell == '.':
                continue

            nodeId = None

            if j > 0 and cells[j-1] != '.':
                nodeId = cells[j-1]

            else:
                cnt += 1
                nodeId = cnt
                dsMakeSet(ds, nodeId)

            cells[j] = nodeId

            if i > 0:
                prevCells = cellss[i-1]
                for j2 in range(j-1, j+2):
                    if j2 >= 0 and j2 < len(prevCells) and \
                       prevCells[j2] != '.':
                        dsUnion(ds, prevCells[j2], nodeId)
    

    roots = set(dsFind(ds, x) for x in ds)
    return len(roots)


def test():
    assert f(['.0..', '00..', '....', '...0']) == 2
    assert f(['.0..', '00..', '..0.', '...0']) == 1


def main():
    lines = [line for line in sys.stdin]
    print(f(lines))


if __name__ == '__main__':
    main()



