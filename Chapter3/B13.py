N,K = map(int,input().split())
A = list(map(int,input().split()))
ans = 0
right = 0
for left in range(N):
  while right<N and sum(A[left:right+1])<=K:
    right += 1
  ans += right-left
print(ans)

"""
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cl
"""
