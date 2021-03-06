[CodeIQ 公開コード一覧](../README.md)

# 問題
「LCM・パレード」問題

自然数 a, b に対し、a と b の最小公倍数を LCM(a, b) と定義する。  
さらに、自然数 n, k に対し、n 以下の全ての自然数 m に対する LCM(k, m)/k の値の和を F(n, k)と定義する。  

標準出力に F(n, k) の値を出力するプログラムを書きなさい。  
1 <= n <= 108, 1 <= k <= 105とする。  


# 方針
LCM(k,m) = k*m/GCD(k,m) より LCM(k,m)/k =  m/GCD(k,m) である。  
ここで、GCD(k,m) の値はkの約数のみなので、その値が等しいものでまとめて和を求め、更にその和を求めれば良い。  

F(9,12)の場合、GCDが1であるのは、m=[1,5,7]、2であるのは [2]、3であるのは [3,9]、4であるのは [4,8]、6であるのは[6]、12であるのは[]である。  
つまり、F(9,12) = (1+5+7)/1 + (2)/2 + (3+9)/3 + (4+8)/4 + (6)/6 で求めることが出来る。  

GCD(k,m)=dであるmの値は、k/d と互いに素である値のd倍の値として求めることが出来る。  
ゆえに、GCD(k,m)=dである m/GCD(k,m) の和は、1からn/d までの自然数の内、k/dと互いに素である値の和である。  

つまり、1からxまでのyと互いに素な値の和を G(x, y) とすると、
F(9,12) = G(9, 12) + G(4, 6) + G(3, 4) + G(2, 3) + G(1, 2)   
= (1+5+7) + (1) + (1+3) + (1+2) + 1 である。

この G(x, y) の値は、1からxまでの和から、重複を考慮しながら、yの素因数の倍数の和を引くことで計算することが出来る。  

+ [コード](solve.py)

# 感想
詰めていくと、問題がするすると簡略化していくのは楽しい。  
kawazoe先生の出題はこれが最後ということで、お疲れ様でした。  













