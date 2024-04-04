N = int(input())
D = int(input())
A = [0] * (N+2)
for i in range(D):
  L,R = map(int,input().split())
  A[L] += 1
  A[R+1] -= 1
ans = 0
for i in range(N):
  ans += A[i+1]
  print(ans)
  
"""
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_g
"""
