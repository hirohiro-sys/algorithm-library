N = int(input())
A = list(map(int,input().split()))
D = int(input())
Q = [list(map(int,input().split())) for _ in range(D)]

# 0idx調整
for q in Q:
  q[0] -= 1
  q[1] -= 1

# 左からの最大累積和
left_mx = [0] * N
left_mx[0] = A[0]
for i in range(1,N):
  left_mx[i] = max(left_mx[i-1],A[i])

# 右からの最大累積和
right_mx = [0] * N
right_mx[-1] = A[-1]
for i in range(N-2,-1,-1):
  right_mx[i] = max(right_mx[i+1],A[i])
  
for l,r in Q:
  print(max(left_mx[l-1],right_mx[r+1]))

"""問題URL
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_j
"""
