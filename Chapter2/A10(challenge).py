# 入力
N = int(input())
A = list(map(int,input().split()))
D = int(input())
query = [list(map(int,input().split())) for _ in range(D)]
for q in query:
  q[0] -= 1
  q[1] -= 1

# 左からの最大累積和
left_max = [0] * N
left_max[0] = A[0]
for i in range(1,N):
  left_max[i] = max(left_max[i-1],A[i])
  
# 右からの最大累積和
right_max = [0] * N
right_max[-1] = A[-1]
for i in range(N-2,-1,-1):
  right_max[i] = max(right_max[i+1],A[i])

# 出力
for l,r in query:
  print(max(left_max[l-1],right_max[r+1]))

"""
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_j
"""
