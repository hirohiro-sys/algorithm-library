T = int(input())
N = int(input())

# 前日比を求める
A = [0] * (T+1)
for _ in range(N):
  L,R = map(int,input().split())
  A[L] += 1
  A[R] -= 1
  
# 累積和を求める
ans = 0
for i in range(T):
  ans += A[i]
  print(ans)

"""問題URL
https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_al
"""
