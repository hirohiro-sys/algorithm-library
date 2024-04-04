n = int(input())
a = [[0]*1500 for _ in range(1500)]
for i in range(n):
  x,y = map(int,input().split())
  x-=1
  y-=1
  a[x][y] += 1
q = int(input())
query = [list(map(int,input().split())) for _ in range(q)]

prefix_sum = [[0]*1501 for _ in range(1501)]
for i in range(1500):
  for j in range(1500):
    prefix_sum[i+1][j+1] = prefix_sum[i+1][j] + a[i][j]
for j in range(1500):
  for i in range(1500):
    prefix_sum[i+1][j+1] = prefix_sum[i][j+1] + prefix_sum[i+1][j+1]
for a,b,c,d in query:
  print(prefix_sum[a-1][b-1]+prefix_sum[c][d] - prefix_sum[a-1][d]-prefix_sum[c][b-1])

"""
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cg
"""
