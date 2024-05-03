N,K = map(int,input().split())
A = list(map(int,input().split()))

right = 0
ans = 0
for left in range(N):
  while right+1<N and A[right+1]-A[left]<=K:
    right += 1
  ans += right-left

print(ans)

"""
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_m
"""
