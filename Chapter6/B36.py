n,k = map(int,input().split())
s = input()

count_on = 0
for i in range(n):
  if s[i]=="1":
    count_on+=1

if count_on%2==k%2:
  print("Yes")
else:
  print("No")

"""
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_di
"""
