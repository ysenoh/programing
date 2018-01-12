#!/usr/bin/python3
#  --*-coding:utf-8-*--

import sys
import time

def f(R,C, lines):
    rows = [list(line.rstrip()) for line in lines]

    for cells in rows:
        lastLetter = None
        cnt = 0

        for i, cell in enumerate(cells):
            if cell == '?':
                if lastLetter != None:
                    cells[i] = lastLetter
                else:
                    cnt += 1
            else:
                if lastLetter == None:
                    for j in range(cnt):
                        cells[j] = cell
                
                lastLetter = cell

    lastRow = None
    cnt2 = 0
    for i, cells in enumerate(rows):
        if cells[0] == '?':
            if lastRow != None:
                rows[i] = lastRow
            else:
                cnt2 += 1
        else:
            if lastRow == None:
                for j in range(cnt2):
                    rows[j] = cells

            lastRow = cells

    return '\n'.join(''.join(cells) for cells in rows)



def test():
    print(f(3, 3, ['G??','?C?','??J']))
    print(f(3, 4, ['CODE','????','?JAM']))
    print(f(2, 2, ['CA','KE']))


def main():
    numOfTestCase = int(input())
    t0 = time.time()

    for testCase in range(numOfTestCase):
        R, C = map(int, input().split())
        lines = [input() for i in range(R)]

        t1 = time.time()
        print('Case #' + str(testCase+1) + ':')
        print(f(R, C, lines))

        if numOfTestCase >= 10:
            t2 = time.time()

            print('... #' + str(testCase+1) + '/' + str(numOfTestCase),
                  '{0:.2f}'.format(t2 - t1),
                  '{0:.2f}'.format(t2 - t0),
                  file=sys.stderr)
    
if __name__ == '__main__':
    main()

