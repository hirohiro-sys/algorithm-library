n = int(input())
stack = []
for i in range(n):
  a = input().split()
  if a[0]=="1":
    stack.append(a[1])
  elif a[0]=="2":
    print(stack[-1])
  else:
    stack.pop()

"""
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ay
"""
