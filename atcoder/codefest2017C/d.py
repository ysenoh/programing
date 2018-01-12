#  --*-coding:utf-8-*--

# CODE FESTIVAL 2017 qual C
# D - Yet Another Palindrome Partitioning
# http://code-festival-2017-qualc.contest.atcoder.jp/tasks/code_festival_2017_qualc_d

def f(str):
    s = {}
    s[0] = 0
    pat = 0

    bits = [2**i for i in range(26)]
    lenOfStr = len(str)

    for c in str:
        pat ^= bits[ord(c)-97]
        s[pat] = min(
            min(s.get(pat^bit, lenOfStr) + 1 for bit in bits),
            s.get(pat, lenOfStr))

    if pat == 0:
        return 1

    return s[pat]
            

def test():
    assert f('aabxyyzz') == 2
    assert f('byebye') == 1
    assert f('abcdefghijklmnopqrstuvwxyz') == 26
    assert f('abcabcxabcx') == 3


def main():
    str = input()
    print(f(str))


if __name__ == '__main__':
    main()
