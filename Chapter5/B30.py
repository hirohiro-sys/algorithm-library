import math
H,W = map(int, input().split())
print(math.comb(H+W-2,W-1)%1000000007)

"""公式解説
マス(1,1)から(H,W)まで行くためにはH+W-2であり、その中のW-1が右方向である必要がある。
逆に右方向への移動回数がW-1なら必ず(H,W)でゴールできる。したがって求める移動方法の数は
H+W-2個の中からW-1個を選ぶ方法の数通りになる。
"""

"""
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_dc
"""
