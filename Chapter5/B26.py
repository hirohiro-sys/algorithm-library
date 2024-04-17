n = int(input())

a = [0] * (n+1)
for i in range(2,int(n**0.5)+1):
  if a[i]==0:
    for j in range(i**2,n+1,i):
      a[j] = 1
    
for i in range(2,n+1):
  if a[i]==0:
    print(i)

"""
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cy
"""
