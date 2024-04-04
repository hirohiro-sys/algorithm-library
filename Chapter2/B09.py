N = int(input())
imos = [[0]*1503 for _ in range(1503)]
presum = [[0]*1503 for _ in range(1503)]
for i in range(N):
  a,b,c,d = map(int,input().split())
  imos[a][b] += 1
  imos[c][d] += 1
  imos[a][d] -= 1
  imos[c][b] -= 1

for i in range(1502):
  for j in range(1502):
    presum[i+1][j+1] = presum[i+1][j] + imos[i][j]
for j in range(1502):
  for i in range(1502):
    presum[i+1][j+1] = presum[i+1][j+1] + presum[i][j+1]

ans = 0
for i in range(1502):
  for j in range(1502):
    if presum[i][j] >= 1:
      ans += 1
print(ans)

"""
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ch
"""
