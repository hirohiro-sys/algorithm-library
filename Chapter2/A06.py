N,Q = map(int,input().split())
A = list(map(int,input().split()))

# prefixSum[L]に1が来ることもあるのでS[0]を用意
prefixSum = [0] * (N+1)

# 累積和を計算
for i in range(1,N+1):
  prefixSum[i] = prefixSum[i-1] + A[i-1]

# 区間の総和を出力
for _ in range(Q):
  L,R = map(int,input().split())
  print(prefixSum[R]-prefixSum[L-1])
  
"""問題URL
https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_ai
"""
