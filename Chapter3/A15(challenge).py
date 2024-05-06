import bisect

n = int(input())
a = list(map(int,input().split()))

b = sorted(list(set(a)))
for i in a:
  ans = bisect.bisect_left(b,i)
  print(ans+1,end=" ")

"""
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_o
"""
