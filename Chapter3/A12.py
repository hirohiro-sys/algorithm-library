n,k = map(int,input().split())
a = list(map(int,input().split()))

left=0
right=10**9
while left < right:
  sum = 0
  middle = (left+right)//2
  for i in range(n):
    sum += middle//a[i]
  if k<=sum:
    right = middle
  else:
    left = middle + 1
  
print(left)

"""
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_l
"""
