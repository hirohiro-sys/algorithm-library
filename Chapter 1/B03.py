n = int(input())
a = list(map(int,input().split()))

for i in range(n):
  for j in range(i+1,n):
    for k in range(j+1,n):
      if a[i]+a[j]+a[k]==1000:
        exit(print("Yes"))
print("No")

"""
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cb
"""
