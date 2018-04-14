#!/usr/bin/python3
#  --*-coding:utf-8-*--



def f(lines, R, C, H, V):
    n = sum(1 if cell == '@' else 0 for line in lines for cell in line)
    if n%((H+1)*(V+1)) > 0:
        return 'IMPOSSIBLE'

    n2 = n//((H+1)*(V+1))

    numPerLine = n2*(V+1)
    


    n3 = 0
    matrix = [[0]*C for i in range(H+1)]
    cnt = 0

    for line in lines:
        n3 += sum(1 if cell == '@' else 0 for cell in line)

        if n3 > numPerLine:
            return 'IMPOSSIBLE'

        for i, cell in enumerate(line):
            if cell == '@':
                matrix[cnt][i] += 1

        if n3 == numPerLine:
            n3 = 0
            cnt += 1

        if cnt == R:
            break

    cnts = None
    for i in range(C):
        if cnts == None:
            cnts = [0]*(H+1)

        flag = True

        for j in range(H+1):
            cnts[j] += matrix[j][i]
            if cnts[j] > n2:
                return 'IMPOSSIBLE'
            elif cnts[j] < n2:
                flag = False
                
        if flag:
            cnts = None

    return 'POSSIBLE'



def main():
    T = int(input())

    for i in range(T):
        R,C,H,V = map(int, input().split())
        lines = [input() for i in range(R)]
        
        print('Case #' + str(i+1) + ': ' + str(f(lines, R, C, H, V)))


if __name__ == '__main__':
    main()
