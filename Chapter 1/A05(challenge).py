n,k = map(int,input().split())
ans = 0
for i in range(1,n+1):
  for j in range(1,n+1):
    if 1<=k-i-j<=n:
      ans += 1
print(ans)

"""
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_e
"""
