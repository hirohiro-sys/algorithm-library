H,W,N = map(int,input().split())
imos_array = [[0]*(W+2) for _ in range(H+2)]
presum_array = [[0]*(W+2) for _ in range(H+2)]
# 書籍参考に二次元の前日比とる
for i in range(N):
  a,b,c,d = map(int,input().split())
  imos_array[a][b] += 1
  imos_array[c+1][d+1] += 1
  imos_array[a][d+1] -= 1
  imos_array[c+1][b] -= 1
# 横の累積和
for i in range(H):
  for j in range(W):
    presum_array[i+1][j+1] = presum_array[i+1][j] + imos_array[i+1][j+1]
# 縦の累積和
for j in range(W):
  for i in range(H):
    presum_array[i+1][j+1] = presum_array[i+1][j+1] + presum_array[i][j+1]

for i in range(H):
  print(*presum_array[i+1][1:W+1])

"""
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_i
"""
