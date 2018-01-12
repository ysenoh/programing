#  --*-coding:utf-8-*--

# CODE FESTIVAL 2017 qual C
# B - Similar Arrays
# http://code-festival-2017-qualc.contest.atcoder.jp/tasks/code_festival_2017_qualc_b

def f(n, vals):
    return 3**n - 2**(sum(x%2==0 for x in vals))
    

def test():
    assert f(2, [2, 3]) == 7
    assert f(3, [3, 3, 3]) == 26
    assert f(10, [90, 52, 56, 71, 44, 8, 13, 30, 57, 84]) == 58921

def main():
    n = int(input())
    vals = map(int, input().split())
    
    print(f(n, vals))
    

if __name__ == '__main__':
    main()
