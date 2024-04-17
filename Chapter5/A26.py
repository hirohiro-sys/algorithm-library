t = int(input())
for i in range(t):
  n = int(input())
  ans = "Yes"
  for j in range(2,int(n**0.5)+1):
    if n%j==0:
      ans = "No"
  print(ans)

"""
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_z
"""
