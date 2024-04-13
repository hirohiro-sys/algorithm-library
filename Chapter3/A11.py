n,x = map(int,input().split())
a = list(map(int,input().split()))

l = 0
r = n-1
while l<=r:
  m = (l+r)//2
  if x<a[m]:
    r = m-1
  elif x>a[m]:
    l = m+1
  else:
    exit(print(m+1))

"""bisect使った簡潔な書き方
import bisect
n,x = map(int,input().split())
a = list(map(int,input().split()))
print(bisect.bisect(a,x))
"""

"""
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_k
"""
