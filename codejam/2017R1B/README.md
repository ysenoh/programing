<!-- --*-coding:utf-8-*-- -->
 
[\[Google Code Jam\]](../README.md)

# コンテスト
GoogleCodeJam 2017 Round1B

スコアを見ると、Round1Bを通過する(1000位以内に入る)のに必要なのは、A B 完答 Cはsmall。  
Round1Bも敗退。(Cをやる時間が無かった)  
上位陣はRound1Aで通過したのか、ランクは1400位ぐらいに大幅アップ。  

# Problem A. Steed 2: Cruise Control
## 問題
https://code.google.com/codejam/contest/8294486/dashboard#s=p0

## 方針
要するに、最後のお馬さんがゴールする時間に合わせて、自分も到達すれば良いだけ。

+ [コード](a.py)

## 感想
ただのウォーミングアップ問題。


# Problem B. Stable Neigh-bors
## 問題
https://code.google.com/codejam/contest/8294486/dashboard#s=p1

## 方針
G O Vに対しては、それぞれ R B Y としか隣になれないので、これらで囲む必要がある。  
ただし、GとRのみ、OとBのみ、VとYのみで、その数が等しい場合は、それらを交互に設定すれば良い。

この囲まれたパターンは、その外部とのつながりにおいて、両側で使用している色が１つだけあるのと同じものとして扱える。  
例えば RGRGR のパターンは、外から見ると1つのRとして扱える。  
なので、R B Y から G O V の個数を引いて、その R B Y を同じ色がつながらないように並べる問題として考えられる。  

例えばR=5,B=4,Y=2の場合以下のように生成することが出来る。
1. Rをバラバラにした配列を作る。 ['R', 'R', 'R', 'R', 'R']
1. 先頭からB個だけBを追加する。 ['RB', 'RB', 'RB', 'RB', 'R']
1. 終端からY個だけYを追加する。 ['RB', 'RB', 'RB', 'RBY', 'RY']
1. すべてつなげる　'RBRBRBRBYRY'

実際には配列に展開せずに、個数だけ計算して、それから文字列を生成すれば良い。  
最後に、G O V を展開する。  

+ [コード](b.py)

## 感想
最初、R B Y を並べるには、 RBYRBY... の様にするしかないと考えていたのでかなり混乱した。  
整理すればどうということはないが、実装するための制限時間が厳しい。  
コンテストでも、この問題は完答できたが、これで時間を使い切ってしまった。  


# Problem C. Pony Express
## 問題
https://code.google.com/codejam/contest/8294486/dashboard#s=p2

簡単に書けば以下の通り。
+ 町と町の間の距離が全て与えられている。  
+ ただし、他の町を経由したほうが近い場合がある。  
+ 各町には馬がいて、各馬の速度と移動可能な距離がわかっている。  
+ ある町からある町まで、最速で行った場合の時間を求めよ。  

## 方針1
全ての町と町の距離は、ワーシャルフロイド法で求める。  
最大の距離の範囲でかかる時間をコストとして有向グラフを作り、ダイクストラ法で時間を求める。  

+ [コード](c.py)

## 方針2
全ての町と町の距離も、ダイクストラ法で求める。  
あとは方針1と同じ。  

+ [コード](c2.py)

## 感想
ダイクストラ法のコードを予め用意しておけば、Problem B より簡単ではないか。  
一度使い切った馬は、そのテストケースの他のルートで使用してよいのか悩んだが、それは無視して良いらしい。  
このあたりの問題文の読み方が、どうも良くわからない。  

方法1より方法2の方がLargeで4倍ほど速かった。  
テストケースによるのかも知れないが、ダイクストラ法で済むのなら、ワーシャルフロイド法は使わないほうが良いかも知れない。  
