T = int(input())
N = int(input())
A = [0] * (T+1)
for i in range(N):
  L,R = map(int,input().split())
  A[L] += 1
  A[R] -= 1
ans = 0
for i in range(T):
  ans += A[i]
  print(ans)

"""
https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_al
"""
