n,q = map(int,input().split())
a = list(map(int,input().split()))
s = [0] * (n+1)
s[0] = 0
for i in range(1,n+1):
  s[i] = s[i-1]+a[i-1]
for i in range(q):
  a,b = map(int,input().split())
  print(s[b]-s[a-1])
"""
https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_ai
"""
