# AtCoder Regular 107

## C - Shuffle Permutation
問題文 https://atcoder.jp/contests/arc107/tasks/arc107_c

提出コード [c.py](c.py)

1列目と2列目、2列目と3列目がスワップ可能なら、複数回の操作で1列目と3列目もスワップできるので、スワップ可能なグループを求めて、それらの個数で順列の組み合わせ。
