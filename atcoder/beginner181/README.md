# AtCoder beginner 181 F - Silver Woods
問題文 https://atcoder.jp/contests/abc181/tasks/abc181_f

提出コード [f.py](beginner181/f.py)

考え方としては、ピンまたは壁との距離がd以下のものをつないで、上と下の壁がつながれば、直径dの円は通過できない。つながっていなければ、通過できる。
つながっているかは、disjoint setを使って判定できる。
