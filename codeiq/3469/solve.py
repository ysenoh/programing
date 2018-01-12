#  --*-coding:utf-8-*--

def g(mat, w, h, n, x, y):
    r = (((mat[y-1][x]  if y>0 else 0) +
          (mat[y][x - 1] if x>0 else 0)) 
         if x > 0 or y > 0 else 1)
    
    if x == w-1 and y == h-1:
        return (1, False) if r == n else (0, r>n)

    x2, y2  = (x + 1, y) if x < w-1 else (0, y+1)

    mat[y][x] = r
    a, spareFlag = g(mat, w, h, n, x2, y2)

    if r != 0 and spareFlag:
        mat[y][x] = 0
        a += g(mat, w, h, n, x2, y2)[0]

    return (a, spareFlag)

def f(w, h, n):
    mat = [[None]*w for i in range(h)]
    return g(mat, w, h, n, 0, 0)[0]


def main():
    w, h, n = map(int, input().split())
    print(f(w, h, n))

if __name__ == '__main__':
    main()
